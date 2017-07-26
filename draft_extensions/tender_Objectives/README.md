Objectives
===============
The **EU** requires the objective(s) of the procurement to be published, where these are environment, social or innovation based objectives.

The **EU** also has a requirement for an additional information field to be included here.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The procurement has requirements that aim at buying an innovative work, but they do not have social or environmental objectives.

```json
{
	"Tender": {
      "Objectives": {
        "types": ["innovative"],
	    "additionalInformation": "The council is looking for innovation in the use of recycled materials when constructing the cycle route. It will also consider tenders that include tunnel construction as part of their design."
	    }
	}
}
```

Schema Extension
=======
```json
{
  "definitions": {
    "Objectives": {
      "title": "Tender objectives",
      "type": "object",
      "properties": {
        "types": {
          "title": "Tender objectives",
          "description": "Contract performance conditions with environmental, social and innovative objectives. Required by the EU.",
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "environmental",
              "social",
              "innovative"
            ]
          }
        },
        "additionalInformation": {
          "title": "Tender objectives additional information",
          "description": "Further details about the objectives of the procurement. Required by the EU",
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "Tender": {
      "properties": {
        "properties": {
          "Objectives": {
            "title": "Tender objectivess",
            "description": "Details about the tender's objectives: environmental, social and/or for innovation. Required by the EU",
            "$ref": "#/definitions/Objectives"
          }
        }
      }
    }
  }
}
```