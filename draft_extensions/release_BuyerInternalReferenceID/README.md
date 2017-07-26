EU Procurement ID
===============
The buyer internal reference identifier is an EU specific field. It uniquely identifies a procurement process within the Buyer's internal system.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============

A tender is issued and a notice published through the EU's TED Notice Form. The buyer publishes an internal reference identifier for the procurement.

```json
{
		"buyerInternalReferenceId": "2015.cycle.barnet"
}
``` 


Schema Extension
=======
```json
{
  "properties": {
    "buyerInternalReferenceId": {
      "title": "Buyer Internal Reference Identifier",
      "description": "The buyer internal reference identifier is an EU specific field. It uniquely identifies a procurement process within the Buyer's internal system.",
      "type": [
        "string",
        "null"
      ]
    }
  }
}
```