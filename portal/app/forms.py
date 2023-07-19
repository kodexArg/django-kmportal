from datetime import date
from logging import PlaceHolder
from django import forms
from django.utils import timezone
from app.models import ExtraCash, FuelOrders, Drivers, Tractors, Trailers
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from django.forms import BooleanField
from django.core.exceptions import ValidationError
from loguru import logger


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
        year_choices = [
            (str(year), str(year))
            for year in range(timezone.now().year, timezone.now().year + 2)
        ]

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
        day, month, year = [
            widget.value_from_datadict(data, files, f"{name}_{i}")
            for i, widget in enumerate(self.widgets)
        ]
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


class FuelOrderForm(forms.ModelForm):
    CHOICES = (
        ("-1", "MAX"),
        ("0", "NO"),
        *[(str(x), str(x) + " L.") for x in range(50, 1001, 50)],
    )

    tractor_liters_to_load = forms.ChoiceField(
        choices=CHOICES,
        label="Tractor Liters to Load",
    )

    backpack_liters_to_load = forms.ChoiceField(
        choices=CHOICES,
        label="Backpack Liters to Load",
    )

    chamber_liters_to_load = forms.ChoiceField(
        choices=CHOICES,
        label="Chamber Liters to Load",
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # apply custom tailwind classes for fields
            field.widget.attrs["class"] = "tw-field"
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] += " tw-checkbox-field"
            else:
                field.widget.attrs["class"] += " tw-input-field"

            # label tranlation:
            if field.label:
                field.widget.attrs["placeholder"] = str(field.label)
                field.widget.attrs["aria-label"] = str(field.label)
                translated_label = _(str(field.label).replace(" ", "_").lower())
                try:
                    field.label = mark_safe(
                        f'<span class="tw-label">{translated_label}</span>'
                    )
                except KeyError:
                    field.label = mark_safe(
                        f'<span class="tw-label">{str(field.label)}</span>'
                    )
                    logger.error(f"failing translation for {field.label}")

        # Customizations
        self.fields["tractor_liters_to_load"].initial = 0
        self.fields["backpack_liters_to_load"].initial = 0
        self.fields["chamber_liters_to_load"].initial = 0

        ## Customizations

        self.fields["tractor_liters_to_load"].initial = 0
        self.fields["backpack_liters_to_load"].initial = 0
        self.fields["chamber_liters_to_load"].initial = 0

    def save(self, *args, **kwargs):
        try:
            return super().save(*args, **kwargs)
        except ValidationError as e:
            logger.exception("Error occurred while saving fuel order:")
            raise

    class Meta:
        model = FuelOrders
        fields = '__all__'
        exclude = [
            "company",
            "operation_code",
            "in_agreement",
            "requested_date",
            "expiration_date",
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

    in_agreement = forms.ChoiceField(
        choices=CHOICES,
        label="In Agreement",
    )
    cash_amount_confirm = forms.IntegerField(
        label="confirm_cash_amount",
        min_value=0,
    )
    requested_date = forms.DateField(
        input_formats=['%d %B, %Y'], 
        label='requested_date',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            # apply custom tailwind classes for fields
            field.widget.attrs["class"] = "tw-field"
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] += " tw-checkbox-field"
            else:
                field.widget.attrs["class"] += " tw-input-field"
                
            if field_name in ['requested_date', 'cash_amount_confirm', 'cash_amount']:
                field.widget.attrs["class"] += " text-right"
                
            # label translation:
            if field.label:
                field.widget.attrs["placeholder"] = str(field.label)
                field.widget.attrs["aria-label"] = str(field.label)
                translated_label = _(str(field.label).replace(" ", "_").lower())
                try:
                    field.label = mark_safe(
                        f'<span class="tw-label">{translated_label}</span>'
                    )
                except KeyError:
                    field.label = mark_safe(
                        f'<span class="tw-label">{str(field.label)}</span>'
                    )
                    logger.error(f"failing translation for {field.label}")


        # Placeholder for cash_amount and cash_amount_confirm
        self.fields['cash_amount'].widget.attrs['placeholder'] = 'ARS $'
        self.fields['cash_amount_confirm'].widget.attrs['placeholder'] = 'ARS $'

        # Customizations
        self.fields["in_agreement"].initial = "under_negotiation"

    # ...


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
        fields = '__all__'
        exclude = [
            "operation_code",
            "user_creator",
            "user_lastmod",
            "expiration_date",
        ]
