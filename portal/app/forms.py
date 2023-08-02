from datetime import date

from app.models import Drivers, ExtraCash, FuelOrders, Tractors, Trailers
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import BooleanField
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from loguru import logger


# Helper function and classes
class DateSelectWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        day_choices = [(str(day), str(day).zfill(2)) for day in range(1, 32)]
        month_choices = [
            ("01", _("January")),
            ("02", _("February")),
            ("03", _("March")),
            ("04", _("April")),
            ("05", _("May")),
            ("06", _("June")),
            ("07", _("July")),
            ("08", _("August")),
            ("09", _("September")),
            ("10", _("October")),
            ("11", _("November")),
            ("12", _("December")),
        ]
        year_choices = [(str(year), str(year)) for year in range(timezone.now().year, timezone.now().year + 2)]

        widgets = [
            forms.Select(choices=day_choices),
            forms.Select(choices=month_choices),
            forms.Select(choices=year_choices),
        ]

        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [str(value.day), str(value.month).zfill(2), str(value.year)]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = [widget.value_from_datadict(data, files, f"{name}_{i}") for i, widget in enumerate(self.widgets)]
        if all(val is not None for val in [day, month, year]):
            try:
                return date(int(year), int(month), int(day))
            except ValueError:
                pass
        return None

    def format_output(self, rendered_widgets):
        return " / ".join(rendered_widgets)

    def save(self, commit=True):
        try:
            return super().save(commit)
        except Exception as e:
            logger.exception("Error occurred while saving fuel order:")
            raise


CHOICES = (
    ("0", "NO"),
    ("-1", "MAX"),
    *[(str(x), str(x) + " L.") for x in range(50, 1001, 50)],
)


# Forms
class FuelOrderForm(forms.ModelForm):
    tractor_liters_to_load = forms.ChoiceField(choices=CHOICES)
    backpack_liters_to_load = forms.ChoiceField(choices=CHOICES)
    chamber_liters_to_load = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)  # You will pass company from your view
        super().__init__(*args, **kwargs)
        
        if company is not None:
            self.fields['driver'].queryset = Drivers.objects.filter(company=company)
            self.fields['tractor_plate'].queryset = Tractors.objects.filter(company=company)
            self.fields['trailer_plate'].queryset = Trailers.objects.filter(company=company)

        for field_name, field in self.fields.items():
            # tailwind classes for fields
            field.widget.attrs["class"] = "tw-field"
            if isinstance(field, BooleanField):  # if is boolean field
                field.widget.attrs["class"] += " tw-checkbox-field"
            else:
                field.widget.attrs["class"] += " tw-input-field"
            # label tranlation:
            if field.label:
                field.widget.attrs["placeholder"] = str(field.label)
                field.widget.attrs["aria-label"] = str(field.label)
                translated_label = _(str(field.label).replace(" ", "_").lower())
                try:
                    field.label = mark_safe(f'<span class="tw-label">{translated_label}</span>')
                except KeyError:
                    field.label = mark_safe(f'<span class="tw-label">{str(field.label)}</span>')
                    logger.error(f"failing translation for {field.label}")

    class Meta:
        model = FuelOrders
        fields = [
            "driver",
            "tractor_plate",
            "trailer_plate",
            "tractor_fuel_type",
            "backpack_fuel_type",
            "chamber_fuel_type",
            "tractor_liters_to_load",
            "backpack_liters_to_load",
            "chamber_liters_to_load",
            "requires_odometer",
            "requires_kilometers",
        ]


class CreateDriverForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = [
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
        ]


class UpdateDriverForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = [
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
            "is_active",
            "is_deleted",
        ]


class DeleteDriverForm(forms.Form):
    id = forms.IntegerField()


class TractorForm(forms.ModelForm):
    class Meta:
        model = Tractors
        fields = ["domain"]


class TrailerForm(forms.ModelForm):
    class Meta:
        model = Trailers
        fields = ["domain"]


class ExtraCashForm(forms.ModelForm):
    CHOICES = ExtraCash.AGREEMENT_CHOICES

    cash_amount_confirm = forms.IntegerField(
        label="confirm_cash_amount",
        validators=[MinValueValidator(0), MaxValueValidator(999999)],  # max 6 digits
    )
    cash_amount = forms.IntegerField(
        label="cash_amount",
        validators=[MinValueValidator(0), MaxValueValidator(999999)],  # max 6 digits
    )

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)  # You will pass company from your view
        super().__init__(*args, **kwargs)

        if company is not None:
            self.fields['driver'].queryset = Drivers.objects.filter(company=company)

        for field_name, field in self.fields.items():
            # apply custom tailwind classes for fields
            field.widget.attrs["class"] = "tw-field"
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] += " tw-checkbox-field"
            else:
                field.widget.attrs["class"] += " tw-input-field"

            if field_name in ["cash_amount_confirm", "cash_amount"]:
                field.widget.attrs["class"] += " text-right"
                field.widget.attrs["step"] = "100"

            # label translation:
            if field.label:
                field.widget.attrs["placeholder"] = str(field.label)
                field.widget.attrs["aria-label"] = str(field.label)
                translated_label = _(str(field.label).replace(" ", "_").lower())
                try:
                    field.label = mark_safe(f'<span class="tw-label">{translated_label}</span>')
                except KeyError:
                    field.label = mark_safe(f'<span class="tw-label">{str(field.label)}</span>')
                    logger.error(f"failing translation for {field.label}")

        # Placeholder for cash_amount and cash_amount_confirm
        self.fields["cash_amount"].widget.attrs["placeholder"] = "ARS $"
        self.fields["cash_amount_confirm"].widget.attrs["placeholder"] = "ARS $"

        # Customizations
        # self.fields["in_agreement"].initial = "under_negotiation"

    def save(self, *args, **kwargs):
        try:
            return super().save(*args, **kwargs)
        except ValidationError as e:
            logger.exception("Error occurred while saving ExtraCash order:")
            raise

    def clean(self):
        cleaned_data = super().clean()
        cash_amount = cleaned_data.get("cash_amount")
        cash_amount_confirm = cleaned_data.get("cash_amount_confirm")

        if cash_amount != cash_amount_confirm:
            self.add_error("cash_amount_confirm", "Cash amount does not match")

    class Meta:
        model = ExtraCash
        fields = "__all__"
        exclude = [
            "company",
            "operation_code",
            "in_agreement",
            "requested_date",
            "expiration_date",
        ]
