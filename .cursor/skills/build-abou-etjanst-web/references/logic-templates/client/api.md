# Klientlogik API (`PageLogic`)

This **is** the supported browser library (from builder mallar, 2026-08-21). Use it to explain and review JavaScript, not only to copy a new `PageLogic`.

How it fits with Python and fältregler: [../libraries.md](../libraries.md).

Only on **Layoutsida**. Runs when answers **on this page** change — no Nästa, no other pages, no Navet/REST.

Wrapper is always:

```javascript
PageLogic = function() {
    var self = this;
    // ...
};
```

`x.1` = current service short name + field number. Block ids like `BLOCK1`.

Hide/show in JS is **only client-side**. Pair with Python [required-when-hidden.md](../required-when-hidden.md) if the field is obligatory. Prefer **fältregler** if the rule is simple and can wait until Nästa.

## How to use

- Get a field instance when you need `When` / `WhenEvent` / split text-value: `var field = self.GetField(ffid)`.
- Batch helpers (`EmptyFields`, `SetHiddenFields`, `SetHiddenBlocks`) take **arrays**. The mall **Hantera flera** uses `ffidMoreInfo` without declaring it — declare that id first.
- `When("contains"|"notcontains", …)` is **case sensitive**. Checkboxes: `"Ja;Nej"` in **alternative order**.
- `self.When(ownFunc, value, callback)` is for a custom `(answer, compareTo) => boolean`.

## `self` (page)

| Method | Meaning |
| --- | --- |
| `GetField(ffid)` | Field instance |
| `SetAnswer(ffid, value)` | Set |
| `SetAnswerIfEmpty(ffid, value)` | Set if empty |
| `GetAnswer(ffid)` | Get |
| `SetHidden(ffid, true/false)` | Hide / show one field |
| `EmptyField(ffid)` | Clear one field |
| `EmptyFields([id, id])` | Clear several |
| `SetHiddenFields([id, id], true/false)` | Hide / show several fields |
| `SetHiddenBlock(blockId, true/false)` | One block |
| `SetHiddenBlocks([id, id], true/false)` | Several blocks |
| `When(fn, value, callback)` | Custom compare: `fn(answer, compareTo)` |

## Field instance (`var field = self.GetField(ffid)`)

| Method | Meaning |
| --- | --- |
| `SetAnswer(value)` / `SetAnswerIfEmpty(value)` | Set |
| `GetAnswer()` | Raw answer |
| `GetValueFromQuestionAlternative()` | Separated **value** |
| `GetAnswerFromQuestionAlternative()` | Separated **display text** |
| `SetHidden(true/false)` | Hide / show |
| `EmptyField()` | Clear |
| `When("equals"\|"notequals"\|"contains"\|"notcontains", value, fn)` | React to answer. Checkboxes: `"Ja;Nej"` in alternative order. contains/notcontains are **case sensitive** |
| `WhenEvent(fn, "change")` | Run on change (e.g. read split text/value) |

Mall files: [empty.md](empty.md), [handle-field.md](handle-field.md), [handle-many.md](handle-many.md), [hide-block-on-value.md](hide-block-on-value.md).
