Country of origin
===============
The EU notice form asks either that the country of origin of the product or service is an EU Member State, Iceland, Liechtenstein, or Norway or that the country code of the country is recorded if it is not.

This extension adds a free text string field for the recording of the country. It is not expected that this field will be used.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A contract is awarded and a contract award notice is published through the EU's TED Notice Form. The country of origin of the service is the United Kingdom

```json
"Contract": {
            "countryOfOrigin: "United Kingdom"
            }
```            

Schema Extension
=======
```json
{
  "definitions": {
    "Contract": {
      "properties": {
        "countryOfOrigin": {
          "title": "Country of Origin",
          "description": "Country of origin of the product or service. Required by EU.",
          "type": "string"
        }
      }
    }
  }
}
```