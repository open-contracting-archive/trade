Variants
===============
The **EU** require a field that states whether lot variants will be accepted. Where this is the case there is a free text field for further information about variants.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The tender has two lots with ids "lot-1" and "lot-2". Variants are allowed for "lot-1" but not for "lot-2".

```json
{
	  "tender": [
      "variants": [
      	    { 
                "hasVariants": true,
                "variantDetails": "Bids may be supported by variant bids going beyond any core proposal included in the project documentation, to cover additional operation and maintenance of existing cycle lane services and equipment as makes sense."
                "relatedLot":["lot-1"]
                },
                { 
		    "hasVariants": false,
		    "variantDetails": "Variants are not allowed"
		    "relatedLot":["lot-2"]
                }
                
            ]
        ]
}    
```
** This example has been modified for OCDS purposes from http://ted.europa.eu/udl?uri=TED:NOTICE:35480-2017:TEXT:EN:HTML&src=0 **

Schema Extension
=======
```json
{
  "definitions": {
    "variants": {
      "title": "Variants",
      "type": "object",
      "properties": {
        "hasVariants": {
          "title": "Lot Variants",
          "description": "A True/False field to indicate if lot variants will be accepted. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "variantDetails": {
          "title": "Lot variant details",
          "description": "Further information about the lot variants that will be accepted. Required by the EU",
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
        "variants": {
          "title": "Lot variants",
          "description": "Details about lot variants: if they will be accepted and what they can consist of. Required by the EU",
          "type": "array",
          "items": {
            "$ref": "#/definitions/variants"
          }
        }
      }
    }
  }
}
```