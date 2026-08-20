# IronPython PageNode

Use PageNode only when linear `PageOrder` is not enough (skip pages, call Bolagsverket, prefill tables).

Simple services should omit `pageNodeXml`. The packager then writes ordinary block pages.

## Shape

Inside `<Page>`:

```xml
<PageNode>
  <Xml><![CDATA[<ObjectFactory Activator="ironpython">
  <ObjectActivator IronPythonType="PageClassName"><![CDATA[
import clr
from System import *
from Abou.Calamare.Web import *

class PageClassName(PageNode):
    def Initialize(self):
        pass

    def GetNextPage(self):
        return None
]]]]><![CDATA[></ObjectActivator>
</ObjectFactory>]]></Xml>
  <Id>123</Id>
  <IsDeleted>false</IsDeleted>
</PageNode>
```

`IronPythonType` and the Python class name must match. `GetNextPage` returning `None` continues with default order.

## APIs seen in exports

```python
self.GetAnswer('KORTNAMN.10')
self.SetAnswer('KORTNAMN.10', '…')
self.GetPage('PageName')
self.SetHidden('', True)
self.Resolve[IBolagsverketServiceFactory]().Create(self.IntegrationContext)
```

Company lookup uses `Abou.Calamare.Framework.Integration.Bolagsverket` and JSON deserialization of Bolagsverket engagement data into a `TableField`.

Payment flows add PageNodes on `Sign`, `payment` (`PaymentPage.aspx`), and `ThankYou` (`PaymentThankYou.aspx`). The thank-you script talks to the payment provider over HTTP/JSON.

Those scripts are environment-specific. **Copy them from a working export the user supplies** rather than rewriting. Integrations fail at runtime if the target site lacks the module, certificates, Bolagsverket agreement, or payment config.

## Nested CDATA

The Python source is CDATA nested inside the ObjectFactory CDATA. Close the inner CDATA before `</ObjectActivator>` using the split-token `]]]]><![CDATA[>`.

If you set `pageNodeXml` in JSON, supply the **inner XML** starting at `<ObjectFactory …>` (the packager CDATA-wraps the `Xml` element). Include the nested CDATA split yourself.

## Guidance

- Prefer extra always-visible fields over custom Python
- Prefer `requiredWhen` for mandatory-if
- Use `GetNextPage` when a whole page should be skipped
- Keep Python 2-style `unicode()` only when cloning old scripts; do not modernize cloned integration code
