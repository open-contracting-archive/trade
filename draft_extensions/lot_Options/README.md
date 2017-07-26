Options
===============
EU and WTO require a description of options to be published. The EU also require a field to state whether options are allowed.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... yes

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The tender has two lots with ids "lot-1" and "lot-2". Options are not allowed for "lot-1" but they are allowed for "lot-2".

```json
{
	  "tender": [
      "options": [
      	    { 
                "hasOptions": false,
                "optionDetails": "Options are not allowed."
                "relatedLot":["lot-1"]
                },
                { 
		    "hasOptions": true,
		    "optionDetails": "ZZZ Need an example. Asked for one from EU experts"
		    "relatedLot":["lot-2"]
                }
                
            ]
        ]
}    
```

Schema Extension
=======
```json
{
  "definitions": {
    "options": {
      "title": "Options",
      "type": "object",
      "properties": {
        "hasOptions": {
          "title": "Lot Options",
          "description": "A True/False field to indicate if lot options will be accepted. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "optionDetails": {
          "title": "Lot option details",
          "description": "Further information about the lot options that will be accepted. Required by the EU",
          "type": [
            "string",
            "null"
          ]
        },
        "relatedLots": {
          "title": "Related Lots",
          "description": "ID of the related lots. Required by the EU",
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "Tender": {
      "properties": {
        "options": {
          "title": "Lot options",
          "description": "Details about lot options: if they will be accepted and what they can consist of. Required by the EU",
          "type": "array",
          "items": {
            "$ref": "#/definitions/options"
          }
        }
      }
    }
  }
}
```