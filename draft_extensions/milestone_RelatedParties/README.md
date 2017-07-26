Related Parties
===============
The **EU, UNCITRAL & WTO** all require the publication of the place, date and time for the opening of tenders. 

The **EU** allows for additional information to be published, for example who may participate in the opening and whether any authorisation is needed.

The **WTO** allows for the publication of the persons authorised to be present. 

**OCDS** models the opening of tenders as a milestone in the procurement procedure. This extension adds the capacity to publish "relatedParties": the organizations who are authorised to attend the opening, and "additionalInformation" which is a free text field that allows additional information about the opening to be recorded.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. yes
WTO .......................................... yes

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The tenders will be opened on 10th May 2017 at 3pm UTC at the offices of London Borough of Barnet. Officers and elected members of the London Borough of Barnet and Tenderers may be present at the opening.

```json
    {
    "id": "milestone-001",
    "type": ["Engagement"],
    "title": "Opening Of Tenders",		
    "description": "Further information about the opening of tenders such as the date, time, place and manner of the opening of the tenders",
    "dueDate": "2010-05-10T15:00:00Z",
	"dateModified": "2010-03-08T10:00:00Z",
	"status":"ZZZ",
	"documents":"",
	"relatedParties":[
        {
         	"id": "GB-COH-1234567844",
	            "name": "AnyCorp Ltd"
	    }
],
    "additionalInformation": "The opening of tenders will be in committee room 3. Officers and elected members of the London Borough of Barnet and Tenderers may be present at the opening."
     }
```
Schema Extension
=======
```json
{
  "definitions": {
    "Milestone": {
      "properties": {
        "relatedParties": {
          "title": "Related Parties",
          "description": "Parties that have a relationship with the milestone.",
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrganizationReference"
          }
        },
        "additionalInformation": {
          "title": "Additional information",
          "description": "Additional information about the milestone",
          "type": [
            "string",
            "integer"
          ]
        }
      }
    }
  }
}
```