European Union Funded
=========
The EU require the publication of whether a procurement has the "Partial or full financing from a European funded project". If it does then the EU requires the publication of the:

- National identifier of the project: 
- Name or other national identification of the project:

OCDS also allows for the publication of the uri of the project.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============

A tender is issued and a notice published through the EU's TED Notice Form. The procurement is part financed by European Regional Development Fund (ERDF) funds.

```json
{
  "budget": [
		{ 
		"EuropeanUnionFunding":  {
		"nationalID": "OC18R15P 0101",
		"name": "2014-2020 Priority Axis 1: Promoting Research and Innovation.",
		uri: "https://www.gov.uk/government/publications/draft-european-regional-development-fund-operational-programme-2014-to-2020"
    		 }
		 }
	]
}    
```

**This example needs adjustment. It is taken from
http://ted.europa.eu/udl?uri=TED:NOTICE:54826-2017:TEXT:EN:HTML&src=0 and the nationalID has been extracted from https://assets.publishing.service.gov.uk/media/551593f6ed915d1424000055/PA1_Humber_FINAL_27_03_15.pdf [PDF file]

Schema Extension
=======
```json
{
  "definitions": {
    "EuropeanUnionFunding": {
      "title": "European Union Funded",
      "type": "object",
      "properties": {
        "projectIdentifier": {
          "title": "Project Identifier",
          "description": "National identifier of the EU project providing partial or full funding",
          "type": [
            "string",
            "null"
          ]
        },
        "projectName": {
          "title": "Project Name",
          "description": "Name or other national identification of the project providing full or partial funding.",
          "type": [
            "string",
            "null"
          ]
        },
        "uri": {
          "title": "Project uri",
          "description": "Uri of the project providing full or partial funding.",
          "type": [
            "string",
            "null"
          ],
          "format": "uri"
        }
      }
    },
    "Budget": {
      "properties": {
        "europeanUnionFunding": {
          "title": "European Union Funded",
          "description": "Details where a procurement has partial or full financing from a European funded project",
          "$ref": "#/definitions/EuropeanUnionFunding"
        }
      }
    }
  }
}
```