### Setting
| Field Name | Field Type |
|------------|------------|
| name       | CharField  |
| value      | TextField  |

### PumpOperators
| Field Name      | Field Type or Related Table |
|-----------------|-----------------------------|
| user            | User                        |
| short_name      | CharField                   |

### Company
| Field Name    | Field Type |
|---------------|------------|
| name          | CharField  |
| fantasy_name  | CharField  |
| cuit          | IntegerField |

### CompanySocialAccount
| Field Name      | Field Type or Related Table |
|-----------------|-----------------------------|
| social_account  | SocialAccount               |
| company         | Company                     |

### Drivers
| Field Name            | Field Type |
|-----------------------|------------|
| company               | Company    |
| first_name            | CharField  |
| last_name             | CharField  |
| identification_type   | CharField  |
| identification_number | CharField  |
| is_active             | BooleanField|
| is_deleted            | BooleanField|

### Tractors
| Field Name | Field Type |
|------------|------------|
| company    | Company    |
| domain     | CharField  |
| is_active  | BooleanField|

### Trailers
| Field Name | Field Type |
|------------|------------|
| company    | Company    |
| domain     | CharField  |
| is_active  | BooleanField|

### ExtraCash
| Field Name         | Field Type or Related Table |
|--------------------|-----------------------------|
| operation_code     | CharField                   |
| order_date         | DateTimeField               |
| modified_date      | DateTimeField               |
| requested_date     | DateField                   |
| expiration_date    | DateField                   |
| user_creator       | User                        |
| user_lastmod       | User                        |
| company            | Company                     |
| driver             | Drivers                     |
| is_locked         | BooleanField                |
| is_paused          | BooleanField                |
| is_finished        | BooleanField                |
| pause_reason       | TextField                   |
| in_agreement       | CharField                   |
| comments           | TextField                   |
| cash_amount        | PositiveIntegerField        |

### FuelOrders
| Field Name                 | Field Type or Related Table |
|----------------------------|-----------------------------|
| operation_code             | CharField                   |
| order_date                 | DateTimeField               |
| modified_date              | DateTimeField               |
| requested_date             | DateField                   |
| expiration_date            | DateField                   |
| user_creator               | User                        |
| user_lastmod               | User                        |
| company                    | Company                     |
| driver                     | Drivers                     |
| tractor_plate              | Tractors                    |
| trailer_plate              | Trailers                    |
| tractor_fuel_type          | CharField                   |
| backpack_fuel_type         | CharField                   |
| chamber_fuel_type          | CharField                   |
| tractor_liters             | PositiveIntegerField        |
| backpack_liters            | PositiveIntegerField        |
| chamber_liters             | PositiveIntegerField        |
| tractor_liters_to_load     | IntegerField                |
| backpack_liters_to_load    | IntegerField                |
| chamber_liters_to_load     | IntegerField                |
| requires_odometer          | BooleanField                |
| requires_kilometers        | BooleanField                |
| is_locked                 | BooleanField                |
| is_paused                  | BooleanField                |
| is_finished                | BooleanField                |
| in_agreement               | CharField                   |
| comments                   | TextField                   |

### Refuelings
| Field Name           | Field Type or Related Table |
|----------------------|-----------------------------|
| acceptance_date      | DateField                   |
| edited_date          | DateField                   |
| fuel_order           | FuelOrders                  |
| pump_operator        | PumpOperators               |
| status               | IntegerField                |
| tractor_pic          | ImageField                  |
| backpack_pic         | ImageField                  |
| chamber_pic          | ImageField                  |
| tractor_liters       | PositiveIntegerField        |
| backpack_liters      | PositiveIntegerField        |
| chamber_liters       | PositiveIntegerField        |
| tractor_fuel_type    | CharField                   |
| backpack_fuel_type   | CharField                   |
| chamber_fuel_type    | CharField                   |
| odometer             | PositiveIntegerField        |
| kilometers           | PositiveIntegerField        |
| dispatch_note_pic    | ImageField                  |
| observation_pic      | ImageField                  |
| observation          | CharField                   |
