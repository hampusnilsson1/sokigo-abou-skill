# Integrationsplattformar

Read 2026-08-21.

## Pulsen Mule

Plugin streams XML to a REST API Pulsen built. Needs Abou ≥ 3.16, Pulsen Mule, Sokigo switch-on.

## Tieto TEIS

Generic adapter:

1. **Send case** (answers, files, case PDF) via TEIS UploadWebService after submit. **Waits for medsökande** if multipelsignering.
2. **Status back** into Abou (email if login or integrated personnummer).
3. **Fråga/svar** (first: KID person/fastighet). Cannot mix Navet + QID + KID without new development.

**Not** in first version: other system’s diary/handläggare in Abou, supplements from the other system.

Builder (docs “tänkt lösning”): field arguments map e-tjänst fields → target fields; DB configuration-table by **kortnamn**. Person prefills = ordinary person fields. Other lookups = Sokigo Python method.

Sammanställning: a TEIS adapter still needs a **second** adapter to the real target system.
