Renewals
===============
The EU require the publication of whether the contract may be renewed and if so the maximum number of renewals (number) as well as the conditions for and description of renewals (string).

The WTO require the publication of whether renewals are permitted within multi-use contracts.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... yes

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. 
There are two lots, "lot-1" and "lot-2". Renewals are allowed for "lot-1" but not for "lot-2". 
The initial contract is for two years and "lot-1" can be extended a maximum of twice, each extension being for one year on the condition that the need for the service remains.

```json
{
	"Lots": {
		"renewals": [
      	    { 
                "hasRenewals": true,
                "maxNumber": "2",
                "conditionsAndDescription": "This lot can be extended a maximum of twice, each extension being for one year on the condition that the need for the service remains."
                },
                { 
                "hasRenewals": false,
                "maxNumber": "",
                "conditionsAndDescription": "This lot cannot be extended."
                }                
            ]
```

Schema Extension
=======
```json
{
  "definitions": {
    "Renewals": {
      "title": "Renewals",
      "type": "object",
      "properties": {
        "hasRenewals": {
          "title": "Has renewals?",
          "description": "A True/False field to indicate whether contract renewals are allowed.",
          "type": "boolean"
        },
        "maxNumber": {
          "title": "Maximum number",
          "description": "Maximum number of renewals of this lot",
          "type": [
            "number",
            "null"
          ]
        },
        "renewalConditions": {
          "title": "Renewal Conditions",
          "description": "Conditions for, and descriptions of, any renewals of this lot",
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "Lots": {
      "properties": {
        "renewals": {
          "title": "Renewals",
          "description": "Details of allowable contract renewals",
          "type": "array",
          "items": {
            "$ref": "#/definitions/Renewals"
          }
        }
      }
    }
  }
}
```