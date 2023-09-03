from asyncio import log
import csv
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from app.views.helpers import CustomTemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.decorators import method_decorator

from app.models import FuelOrders


@method_decorator(login_required, name="dispatch")
class UserHomeView(CustomTemplateView):
    template_name = "user_home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('staff_home')
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name="dispatch")
class TicketsView(CustomTemplateView):
    template_name = "modules/tickets.html"


@method_decorator(login_required, name="dispatch")
class ExportFuelOrderCSV(View):

    def get(self, request, *args, **kwargs):
        company = self.kwargs.get('company')
        
        # Get the FuelOrder instance by operation_code
        try:
            fuel_order = FuelOrders.objects.filter(company=company).first()
        except FuelOrders.DoesNotExist:
            return HttpResponse("Operation code not found", status=404)

        # Get all FuelOrder objects belonging to the same company
        fuel_orders = FuelOrders.objects.filter(company=fuel_order.company)

        # Prepare the CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{fuel_order.company.name}_fuel_orders.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Operation Code', 'Order Date', 'Modified Date', 'Requested Date', 'Expiration Date', 
            'User Creator', 'User Last Modified', 'Company', 'Driver', 'Tractor Plate', 'Trailer Plate',
            'Tractor Fuel Type', 'Backpack Fuel Type', 'Chamber Fuel Type',
            'Tractor Liters', 'Backpack Liters', 'Chamber Liters',
            'Tractor Liters to Load', 'Backpack Liters to Load', 'Chamber Liters to Load',
            'Requires Odometer', 'Requires Kilometers',
            'Is Locked', 'Is Paused', 'Is Finished',
            'In Agreement', 'Comments'
        ])

        for order in fuel_orders:
            writer.writerow([
                f"`{order.operation_code}",
                order.order_date,
                order.modified_date,
                order.requested_date,
                order.expiration_date,
                order.user_creator.email,
                order.user_lastmod.email,
                order.company.name,
                order.driver,
                order.tractor_plate if order.tractor_plate else ' - ',
                order.trailer_plate if order.trailer_plate else ' - ',
                order.tractor_fuel_type if order.tractor_fuel_type else ' - ',
                order.backpack_fuel_type if order.backpack_fuel_type else ' - ',
                order.chamber_fuel_type if order.chamber_fuel_type else ' - ',
                order.tractor_liters if order.tractor_liters else ' - ',
                order.backpack_liters if order.backpack_liters else ' - ',
                order.chamber_liters if order.chamber_liters else ' - ',
                'Max' if order.tractor_liters_to_load == -1 else (order.tractor_liters_to_load if order.tractor_liters_to_load else ' - '),
                'Max' if order.backpack_liters_to_load == -1 else (order.backpack_liters_to_load if order.backpack_liters_to_load else ' - '),
                'Max' if order.chamber_liters_to_load == -1 else (order.chamber_liters_to_load if order.chamber_liters_to_load else ' - '),
                'No' if all(x in [0, None] for x in [order.tractor_liters_to_load, order.backpack_liters_to_load, order.chamber_liters_to_load]) else '',
                ' X ' if order.requires_odometer else ' - ',
                ' X ' if order.requires_kilometers else ' - ',
                ' X ' if order.is_locked else ' - ',
                ' X ' if order.is_paused else ' - ',
                ' X ' if order.is_finished else ' - ',
                ' X ' if order.in_agreement == 'agreed' else ' - ',
                order.comments if order.comments else ' - '
            ])

        return response

