# Named verksamhetssystem

Read 2026-08-21 from Integrationer children. These are **Sokigo-built adapters**, usually “when the e-tjänst completes, send the case”. You do not implement the SOAP/XML yourself. Confirm the plugin is on the site; then copy a working service or ask Sokigo for field mapping.

| Integration | Docs gist |
| --- | --- |
| Artvise Kundtjänst | Direct; Täby felanmälan on complete |
| Barium Live | Starts a Barium process (Lomma felanmälan) |
| CGI Treserva | Ekonomiskt bistånd: fetch stadsdelar/orsaker; send case+PDF |
| Easit BPS | XML files on disk (Lidingö) |
| EDP ByggReda via Mule | Case Abou → Mule → ByggReda (Falkenberg) |
| EDP Vision | XML per Vision XSD on submit (Falkenberg) |
| Evry Ephorte | XML on disk → Lex Talk (Karlskrona) |
| Flexeurope Flexite | One-way felanmälan to contact center (Norrtälje) |
| Ida Infront iipax/Bitsy | One-way PDF+data; not reusable |
| Prosona Castor | Create case in Castor; diary number back to Abou (direct or TEIS) |
| Seriline P-Express | Parking cards; P-Express uses Abou REST (Helsingborg) |
| Sokigo AlkT | Alcohol permits; list/edit serveringspersonal; Min sida lookups (Karlskrona) |
| Sokigo ByggR | MinutBygg / GÄHS: apply, supplement, decision, grannhöran (several kommuner) |
| Sokigo Ecos | MinutMiljö: avlopp, bergvärme, livsmedel, radon |
| Sokigo Evolution | Send case; Min sida; supplements; decisions |
| Sokigo OL2 | Folköl/tobak/e-cig (Karlskrona) |
| Sokigo Orbit | Felanmälan on complete (Huddinge) |
| Sokigo Skolskjuts | Prefill elev; send application; prelim decisions (Trelleborg) |
| Solarplexus Lex | XML on disk → Lex Talk (Upplands Väsby) |

AlkT and ByggR/Ecos are the richest Sokigo ones. No Python method tables except EDP Future ([edp-future.md](edp-future.md)).
