Electronic workflows
===============
The EU require the publication of whether electronic ordering and payment methods will be used and whether electronic invoicing will be accepted

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The buyer will use electronic ordering and payment methods but electronic invoicing will not be accepted.

```json
{
	"Tender": {
		"electronicWorkflows": {
    		"useOrdering": true,
    		"usePayment": true,
    		"acceptInvoicing": false
		}
	}
}
```

Schema Extension
=======
```json
    {
      "definitions": {
        "electronicWorkflows": {
          "title": "Electronic Workflows",
          "type": "object",
          "properties": {
            "useOrdering": {
              "title": "Tender uses electronic ordering",
              "description": "A True/False field to indicate if electronic ordering will be used. Required by the EU",
              "type": [
                "boolean",
                "null"
              ]
            },
            "usePayment": {
              "title": "Tender uses electronic payment",
              "description": "A True/False field to indicate if electronic payment will be used. Required by the EU",
              "type": [
                "boolean",
                "null"
              ]
            },
            "acceptInvoicing": {
              "title": "Tender accepts electronic invoicing",
              "description": "A True/False field to indicate if electronic invoicing will be accepted. Required by the EU",
              "type": [
                "boolean",
                "null"
              ]
            }
          }
        },
        "Tender": {
          "properties": {
            "electronicWorkflows": {
              "title": "Tender economic workflows",
              "description": "Details about economic workflows: ordering, invoicing and payments and whether they will be used and/or accepted. Required by the EU",
              "$ref": "#/definitions/electronicWorkflows"
            }
          }
        }
      }
    }
```    