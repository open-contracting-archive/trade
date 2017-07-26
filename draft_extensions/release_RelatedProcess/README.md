Related Process
===============
If this process is followed by one or more contracting processes, represented under a separate open contracting identifier (ocid) then details of the related process can be provided here. 

This is commonly used to point to subcontracts, or to renewal and replacement processes for this contract. 

This extension adds fields to satisfy the reporting requirements of the EU for subcontracting potential in a contract.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A contract is signed and a TED Contract Award Notice is published. Lot 2 may be subcontracted.

```json
"contract": { 
"relatedProcesses": [
	{
	"id": "RP001",
	"relationship": "subContract",
	"relatedLots": ["lot-2"],
	"description": "For civil engineering services delivered in the project",
	"value": {
                    "currency":"GBP",
                    "amount":600000
                }
	}
  ]
```

Schema Extension
=======
```json
  {
  "definitions": {
    "relatedProcess": {
      "description": "A link to a related contracting process in OCDS and the type of relationship.",
      "type": "object",
      "title": "Related Process",
      "properties": {
        "relatedLots": {
          "title": "Related lots",
          "description": "An array containing the lot identifiers of the lots within this contract that may be subcontracted. Required by the EU",
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          }
        },
        "description": {
          "title": "description",
          "description": "Short description of the part of the contract to be subcontracted. Required by the EU",
          "type": "string"
        },
        "value": {
          "title": "value",
          "description": "Estimated subcontracting value excluding VAT. Required by the EU",
          "$ref": "#/definitions/Value"
        }
      }
    }
  }
}
```