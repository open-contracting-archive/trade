Purpose of Notice
===============
The EU requires the publication of various purposes for the notice. These are used to determine the fields in the notice that are required to be completed.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The purpose of the notice is to act as a call for competition. It does not reduce time limits and it is not for social or other specific services.

```json
{
  "Release": {
    "purposeOfNotice": {
	    "reducesTimeLimits": false,
	    "isACallForCompetition": true,
	    "socialOrOtherSpecificServices": false
	}
  }
}

```

Schema Extension
=======
```json
{
  "definitions": {
    "PurposeOfNotice": {
      "title": "Purpose Of Notice",
      "type": "object",
      "properties": {
        "reducesTimeLimits": {
          "title": "Reduces Time Limits?",
          "description": "A True/False field to indicate whether this notice aims at reducing time limits for the receipt of tenders ",
          "type": "boolean"
        },
        "isACallForCompetition": {
	    "title": "Is A Call For Competition?",
	    "description": "A True/False field to indicate whether this notice is a call for competition",
	    "type": "boolean"
        },
        "socialOrOtherSpecificServices": {
	    "title": "Is For Social Or Other Specific Services?",
	    "description": "A True/False field to indicate whether this notice is for social or other specific services?",
	    "type": "boolean"
        }
      }
    },
    "Tender": {
      "properties": {
        "purposeOfNotice": {
          "title": "Purpose Of Notice",
          "description": "Details about the purpose of this notice release - used to determine the fields in the notice that are required to be completed. Required by EU.",
          "$ref": "#/definitions/purposeofNotice"
        }
      }
    }
  }
}
```