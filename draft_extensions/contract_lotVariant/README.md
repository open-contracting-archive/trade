Lot Variant
===============
The EU require the publication of the contract id and lot identifier(s) where the successful tenderer submitted a variant.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A contract is awarded and a notice published through the EU's TED Notice Form. The successful tenderer submitted variants for "lot-1" and "lot-3".

```json
"Contract": {
		"id": "ocds-213czf-000-00001-contract-01",
		......
	    "lotVariant": ["lot-1", "lot-3"]
	    }
```	    


Schema Extension
=======
```json
{
  "definitions": {
    "Contract": {
      "properties": {
        "lotVariant": {
          "title": "Lot Variant",
          "description": "The contract was awarded to a tenderer who submitted a variant for the following lot(s)",
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string",
            "uniqueItems": true 
          }
        }
      }
    }
  }
}
```