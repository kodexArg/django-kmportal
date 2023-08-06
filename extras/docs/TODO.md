# KM 1151 Enterprise Portal
Last update: 2028 07 28


## Currently in process
- Staff/qr to send FuelOrders to Refuelings on Refueling creation.

## Next up
- Refueling Crud in staff


## ToDo
- Create order 'locked'
- Save correct user that edit the model (done but not checked)
- 'Page Not found'
- Pagination on orders/
- 'About us' page
- 'Contact us' page
- show more in orders/ (like user who updated...)
- Comment in new order
- fix Migration or reset?
- Currently: views from staff filtered with "staff_member_required" instead of "Pump Operators" group.
- Staff navbar: change the 'include' call for a custom_component


## Won't
- 'Edit' order


## Candy ToDo
- 'Lock' order at top
- Flowbite animations
- Images and icons verywhere


## Done (2023 07 30 and on)
- Refueling model
- Pump Operator model or User model for staff?? --> User model and Pump Operators group.
- /order/new/
    - It's showing all the drivers instead of the drivers of the current enterprise
    - I bet it's the same with drivers and plates (not checked yet)
- check before save moved to model
- refactoring Order Model/View
- is_pauseed -> is_paused
- fixing migrations
- fixing Js in orders
- Implementing djang-compressor
