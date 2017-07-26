Joint Procurement
===============
The EU notice form includes a checkbox for joint procurement, indicating a Boolean field, and then requires the country code for where the law applies. There is no indication how the country should be represented.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. This is a joint procurement with the law of the United Kingdom being applied.

```json
{
	  "tender": [
                { 
                "isJointProcurement": "true",
                "country": "GBR"
                }
        ]
}    
```


Schema Extension
=======
```json
{
  "definitions": {
    "jointProcurement": {
      "title": "Joint procurement",
      "type": "object",
      "properties": {
        "isJointProcurement": {
          "title": "Is A Joint Procurement",
          "description": "A True/False field to indicate if this is a joint procurement or not. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "country": {
          "title": "country",
          "description": "ISO Country Code of the country where the law applies. See the [countryCode codelist](http://standard.open-contracting.org/latest/en/schema/codelists/#ZZZ ADD CODELIST) for codes",
          "type": [
	            "string",
	            "null"
	          ],
	            "enum": [
            		"INCLUDE OR NOT?"
            ]
        }
      }
    },
    "Tender": {
      "properties": {
        "jointProcurement": {
          "title": "Joint Procurement details",
          "description": "Details about a joint procurement. Required by the EU",
          "$ref": "#/definitions/JointProcurement"
        }
      }
    }
  }
}
```