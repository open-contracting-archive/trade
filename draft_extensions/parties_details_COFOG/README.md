Organization Classification
===============
The EU have a number of specific requirements to publish details about organizations. Here there are requirements to publish whether an organization is a central purchasing body and whether an organization is an SME. Additionally, the fields ""Type of buyer"", ""Main general activity"", ""Main sectoral activity"" use the UN's Classification of the Functions of Government (COFOG) codes to further categorize government organizations.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice is published through the EU's TED Notice Form. The buyer is a local authority and is not a central purchasing body.

```json
{
    "Organization": {
	    "details": {
	      "typeOfBuyer": "Local Government Authority",
	      "mainGeneralActivity": "General public services",
	      "mainSectoralActivity": "",
	      "isACentralPurchasingBody": false
    }
  }
}	    
```   

Schema Extension
=======

```json
{
  "definitions": {
    "Organization": {
      "properties": {
        "details": {
          "description": "Additional classification information about parties can be provided using partyDetail extensions that define particular properties and classification schemes.",
          "type": [
            "object",
            "null"
          ],
          "properties": {
            "typeOfBuyer": {
              "title": "Type of Buyer",
              "description": "The type of buyer taken from the EU's specified list in its TED forms.",
              "type": [
                "string",
                "null"
              ],
              "enum": [
                "Central government authority",
                "Regional government authority",
                "Local government authority",
                "Body governed by public law",
                "Buyer awarding a contract subsidized by a contracting authority",
                "Public undertaking",
                "Buyer operating on the basis of a special or exclusive right",
                "International organisation",
                "Other",
                ""
              ]
            },
            "mainGeneralActivity": {
              "title": "Main General Activity",
              "description": "The main general activity of the buyer taken from the EU's specified list in its TED forms which is taken from the United Nations Classification of the Functions of Government (COFOG) codelist.",
              "type": [
                "string",
                "null"
              ],
              "enum": [
                "General public services",
                "Defence",
                "Public order and safety",
                "Economic and financial affairs",
                "Environment",
                "Housing and community amenities",
                "Health",
                "Recreation, culture and religion",
                "Education",
                "Social protection"
              ]
            },
            "mainSectoralActivity": {
              "title": "Main Sectoral Activity",
              "description": "The main sectoral activity of the buyer taken from the EU's specified list in its TED forms which is taken from the United Nations Classification of the Functions of Government (COFOG) codelist.",
              "type": [
                "string",
                "null"
              ],
              "enum": [
                "Production, transport and distribution of gas or heat",
                "Electricity-related activities",
                "Extraction of gas or oil",
                "Exploration and extraction of coal or other solid fuels",
                "Water-related activities",
                "Postal services",
                "Railway services",
                "Urban railway, tramway, trolleybus or bus services",
                "Port-related activities",
                "Airport-related activities"
              ]
            },
            "isACentralPurchasingBody": {
              "title": "Is the organization a central purchasing body?",
              "description": "A true/false field to indicate whether the organization is a central purchasing body.",
              "type": [
                "boolean",
                "null"
              ]
            }
          }
        }
      }
    }
  }
}
```