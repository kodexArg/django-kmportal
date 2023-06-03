## PUMP MODELS DOCUMENTATION

### Setting Model

This table is used for the project's settings. The important values are domain, which represents the domain of the project.

| Field Name | Field Type | Description |
| ---------- | ---------- | ----------- |
| name       | CharField  | Name of the setting. |
| value      | TextField  | Value of the setting. |

---
### PumpOperators Model

This table is used for pump operator's login. To create a new user, use the proposed_email method.

| Field Name | Field Type         | Description                                |
| ---------- | ------------------ | ------------------------------------------ |
| user       | OneToOneField(User)| User object associated with this operator.|
| short_name | CharField          | Unique short name of the operator.         |

---
### Company Model

This table is used to store B2B partner company information.

| Field Name  | Field Type   | Description                                          |
| ----------- | ------------ | ---------------------------------------------------- |
| name        | CharField    | Name of the company.                                 |
| fantasy_name| CharField    | The business's trading name.                         |
| cuit        | IntegerField | Unique Tax Identification Code (CUIT) for the company|

---
### Drivers

| Field Name          | Field Type          | Description                               |
| ------------------- | ------------------- | ----------------------------------------- |
| company             | ForeignKey(Company) | The company to which the driver belongs.  |
| first_name          | CharField           | The first name of the driver.             |
| last_name           | CharField           | The last name of the driver.              |
| language            | CharField           | The preferred language of the driver.     |
| identification_type | CharField           | The type of identification used by the driver. |
| identification_number | CharField       | The identification number of the driver.  |
| is_active           | BooleanField        | Represents whether the driver is active.  |

---
### Tractors Model

| Field Name | Field Type          | Description                               |
| ---------- | ------------------- | ----------------------------------------- |
| company    | ForeignKey(Company) | The company to which the tractor belongs. |
| domain     | CharField           | The domain of the tractor.                |
| is_active  | BooleanField        | Represents whether the tractor is active. |

---
### Trailers

| Field Name | Field Type          | Description                               |
| ---------- | ------------------- | ----------------------------------------- |
| company    | ForeignKey(Company) | The company to which the trailer belongs. |
| domain     | CharField           | The domain of the trailer.                |
| is_active  | BooleanField        | Represents whether the trailer is active. |

---
### FuelOrders



| Field Name            | Field Type            | Description                              |
| --------------------- | --------------------- | ---------------------------------------- |
| order_date            | DateField             | The date the order was made.             |
| modified_date         | DateField             | The date the order was last modified.    |
| requested_date        | DateField             | The date the fuel was requested.         |
| operation_code        | CharField             | Unique operation code for the order.     |
| company               | ForeignKey(Company)   | The company placing the order.            |
| expiration_date       | DateField             | The date the order expires.              |
| driver                | ForeignKey(Drivers)   | The driver associated with the order.    |
| tractor_plate         | ForeignKey(Tractors)  | The tractor associated with the order.   |
| trailer_plate         | ForeignKey(Trailers)  | The trailer associated with the order.   |
| tractor_fuel_type     | CharField             | The fuel type for the tractor.           |
| backpack_fuel_type    | CharField             | The fuel type for the backpack.          |
| chamber_fuel_type     | CharField             | The fuel type for the chamber.           |
| tractor_liters        | PositiveIntegerField  | The liters for the tractor.              |
| backpack_liters       | PositiveIntegerField  | The liters for the backpack.             |
| chamber_liters        | PositiveIntegerField  | The liters for the chamber.              |
| tractor_liters_to_load| IntegerField          | The liters to load for the tractor.      |
| backpack_liters_to_load| IntegerField        | The liters to load for the backpack.     |
| chamber_liters_to_load | IntegerField        | The liters to load for the chamber.      |
| requires_odometer     | BooleanField          | Flag to indicate if odometer is required.|
| requires_kilometers   | BooleanField          | Flag to indicate if kilometers are required.|
| is_blocked            | BooleanField          | Represents if the order is blocked.      |
| comments              | TextField             | Any comments associated with the order.  |
| in_agreement          | IntegerField          | The agreement status of the order.       |

---
### Refuelings Model

This table is used to store refueling data.


| Field Name        | Field Type             | Description                                |
| ----------------- | ---------------------- | ------------------------------------------ |
| acceptance_date   | DateField              | The date the refueling was accepted.       |
| edited_date       | DateField              | The date the refueling was last edited.    |
| fuel_order        | ForeignKey(FuelOrders) | The fuel order associated with the refueling.|
| pump_operator     | ForeignKey(PumpOperators)| The pump operator performing the refueling. |
| status            | IntegerField           | The current status of the refueling.       |
| tractor_pic       | ImageField             | The picture of the tractor during refueling. |
| backpack_pic      | ImageField             | The picture of the backpack during refueling. |
| chamber_pic       | ImageField             | The picture of the chamber during refueling. |
| tractor_liters    | PositiveIntegerField   | The liters refueled for the tractor.       |
| backpack_liters   | PositiveIntegerField   | The liters refueled for the backpack.      |
| chamber_liters    | PositiveIntegerField   | The liters refueled for the chamber.       |
| tractor_fuel_type | CharField              | The fuel type for the tractor.             |
| backpack_fuel_type| CharField              | The fuel type for the backpack.            |
| chamber_fuel_type | CharField              | The fuel type for the chamber.             |
| odometer          | PositiveIntegerField   | The odometer reading after refueling.      |
| kilometers        | PositiveIntegerField   | The kilometers driven after refueling.     |
| dispatch_note_pic | ImageField             | The picture of the dispatch note.          |
| observation_pic   | ImageField             | The picture of any other observation.      |
| observation       | CharField              | Any additional observation during refueling. |
