from datetime import date, timedelta
from django import forms
from django.utils import timezone
from .models import FuelOrders, Drivers, Tractors, Trailers
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
import logging

logger = logging.getLogger(__name__)

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


class FuelOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ## Format classes
        fields_default_classes = """
                bg-sky-100
                border 
                border-sky-500 
                text-gray-900 
                text-sm
                rounded-lg 
                focus:ring-blue-500 
                focus:border-blue-500 
                block
                w-full 
                px-2 py-1
                mb-0.5
                dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
            """
        labels_default_classes = """
                font-rubik
                text-sm
                text-sky-900
                dark:text-gray-300
                placeholder-gray-400
                """

        for _, field in self.fields.items():
            field.widget.attrs["class"] = fields_default_classes

            if field.label:
                field.widget.attrs["placeholder"] = field.label
                field.widget.attrs["aria-label"] = field.label
                field.label = mark_safe(
                    f'<span class="{labels_default_classes}">{field.label}</span>'
                )

        ## Customizations
        # Booleans
        for field in ["requires_odometer", "requires_kilometers"]:
            self.fields[field].widget.attrs["class"] += "w-1"

        self.fields["tractor_liters_to_load"].initial = 0
        self.fields["backpack_liters_to_load"].initial = 0
        self.fields["chamber_liters_to_load"].initial = 0

        # Date
    CHOICES = (
        ("-1", "MAX"),
        ("0", "NO"),
        *[(str(x), str(x) + " Liters") for x in range(50, 1001, 50)],
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

    def save(self, commit=True):
        try:
            return super().save(commit)
        except Exception as e:
            logger.exception("Error occurred while saving fuel order:")
            raise

    class Meta:
        model = FuelOrders
        exclude = ["company", "operation_code", "in_agreement", "requested_date", "expiration_date"]


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
