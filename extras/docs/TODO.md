# KM 1151 Enterprise Portal
Last update: 2028 07 28


## Currently in process
- setting up HTTPS (Let's Encrypt)

## Next up


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
- i18n to STAFF!!!


## Won't
- 'Edit' order


## Candy ToDo
- 'Lock' order at top
- Flowbite animations
- Images and icons verywhere


## Done (2023 07 30 and on)
- Refueling Crud in staff
- Qr should handle the error if the Refueling order already exist (avoiding IntegrityError) or finished!
- Refueling view
- QR for real (picture reader whatever you call it)
- Staff/qr to send FuelOrders to Refuelings on Refueling creation. --> sending operation_code in GET method and handled by the Refueling view
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
