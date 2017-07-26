Review Proceedings
===============
The **EU** requires the publication of whether an economic operator applied to the buyer for a review of the procedure; whether an economic operator or another party challenged the procedure before a review body and if so, the identifier of the review procedure(s)

**UNCITRAL** requires that, promptly after receipt of the application, the procuring entity shall publish a notice of the application.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. yes
WTO .......................................... no

Worked Example
==============
Following the award of a contract one of the Tenderers challenges the procedure, without first applying to the buyer for a review. 

```json
{
  "awards": [
    {
      "reviewProceedings": {
        "buyerProcedureReview": false,
        "reviewBodyChallenge": true,
        {
            "id":"Case024631",
            "title":"AnyCorp Ltd v London Borough of Barnet [2016] AC",
            "uri":"http://court-cases.gov.uk/Case024631"
          }
      }
    }
  ]
}
```

**The citation in legalProceduresID needs to be checked**

Schema Extension
=======
```json
{
  "definitions": {
    "ReviewProceedings": {
      "title": "Review Proceedings",
      "type": "object",
      "properties": {
        "buyerProcedureReview": {
          "title": "Award buyer procedure review",
          "description": "A True/False field to indicate if an economic operator applied to the buyer for a review of the procedure. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "reviewBodyChallenge": {
          "title": "Award review body challenge",
          "description": "A True/False field to indicate if an economic operator or another party challenged the procedure before a review body. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "legalProcedures": {
          "title": "Award legal procedures review",
          "description": "Legal identifier(s) of any review procedure(s) initiated. Required by the EU",
          "type": [
            "array",
            "null"
          ],
          "items": {
            "$ref": "#/definitions/LegalProceedings"
          }
        }
      }
    },
    "LegalProceedings": {
      "title": "Legal Proceeedings",
      "type": "object",
      "properties": {
        "id": {
          "title": "Legal Proceeedings id",
          "description": "Legal identifier(s) of any review procedure(s) initiated. Required by the EU",
          "type": [
            "string",
            "null"
          ]
        },
        "title": {
          "title": "Legal Proceeedings Title",
          "description": "Title(s) of any legal proceedings(s) initiated.",
          "type": [
            "string",
            "null"
          ],
          "format": "uri"
        },
        "uri": {
          "title": "Legal Proceeedings uri",
          "description": "Legal identifier(s) of any review procedure(s) initiated.",
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "Award": {
      "properties": {
        "reviewProceedings": {
          "title": "Award review proceedings",
          "description": "Details about any application for a review of the award. Required by the EU",
          "$ref": "#/definitions/ReviewProceedings"
        }
      }
    }
  }
}
```