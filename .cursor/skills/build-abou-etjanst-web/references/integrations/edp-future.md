# EDP Future (VA / avfall)

Docs: [EDP Future](https://dok.sokigo.com/pages/viewpage.action?pageId=58524206) and [anropsmetoder](https://dok.sokigo.com/display/ABOU/EDP+Future-adapter+Anropsmetoder). Read 2026-08-21.

Abou ↔ EDP Webb. E-tjänster in docs: invoices, subscriptions, water meter history/reading, applications, collection schedule/history, new/change subscription, contacts, reklamation.

Python methods take a **Request** object. Only use if this adapter is on the site. This file **is** the method documentation (Sokigo publishes this list). There is no builder mall — clone a working Future e-tjänst for the exact Python types. How it fits: [libraries.md](../logic-templates/libraries.md).

| Method | Request fields |
| --- | --- |
| GetCustomersByIdentity | UserIdentity |
| GetCustomerContacts | CustomerId |
| GetKundAterbetalningskontoTypList | (none) |
| GetApplicationsByCustomers | CustomerIDs |
| GetApplicationById | ApplicationId |
| GetVAServicesByBuilding | BuildingId, EServiceType |
| GetVAServiceEventsByService | ServiceId, CustomerId |
| GetBuildingsByCustomerIDs | CustomerIDs, EServiceType |
| GetAllServicesByBuildingID | BuildingId (active RH/VA/other) |
| CheckMeterReadingReliability | (meter reading check) |
| GetServicesByBuildingIdForOrder | BuildingId |
| CalculateOrderCost | OrderType (serialized), BuildingId, CustomerId, ServiceId, IncVat (from 2022.11 V2) |
| CalculateOrderRows | same |

Request properties listed: UserIdentity, CustomerId, CustomerIDs[], ApplicationId, BuildingId, ServiceId, MeterId, ReadingValue, ReadingDate, Comment, EServiceType, Parameters, OrderType, EmptyPerYear, Choice, IncVat, BinNumber, FeeCode, FeeChangeDate.

Clone a working Future e-tjänst for the exact Python types.
