Tender Review Procedure
===============
Each procurement procedure must be challengeable through a review procedure. 

**The EU** requires the publication of up to three organisations with responsibilities for this procedure: the review body, the organization where information can be obtained about the review process and a mediation service. It also requires information about deadline(s) for review procedures

**UNCITRAL** requires the publication of the review bodies as well as the standstill period when a review is requested.

**WTO** requires the publication of the details of the review procedure.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. yes
WTO .......................................... yes

Worked Example
==============
A tender is issued by a local authority for works, services or supplies. It includes

 - An organization who will act as the review body
 - An organization who will act as the mediation body
 - An organization who will act as the information service
 - The timelines for the review period and the standstill period

```json
{
		"reviewProcedure": {
			"reviewParties": [
			{
                "id": "GB-LAC-E09000003",
                "name": "London Borough of Barnet"
            }
		],
        "reviewPeriod": {
				"startDate": "2017-10-31T09:30:00Z",
				"endDate": "2017-11-10T17:30:00Z"                
			},
		"standstillPeriod": {
				"durationInDays": "10",
			}
 }
} 
``` 


Schema Extension
=======
```json
{
  "definitions": {
    "Tender": {
      "properties": {
        "reviewParties": {
          "title": "Organizations involved in the review procedure of the tender",
          "description": "The organizations involved in the review procedure for the procurement procedure. Required by the EU and UNCITRAL",
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrganizationReference"
          },
          "uniqueItems": true
        },
        "reviewPeriod": {
          "title": "Review period",
          "description": "The period during which the decision of the procuring entity to award a contract can be challenged.",
          "$ref": "#/definitions/Period"
        },
        "standstillPeriod": {
          "title": "Standstill period",
          "description": "The duration of the applicable standstill period following a challenge or appeal of decisions or actions taken by the procuring entity that are allegedly not in compliance with the provisions of the Law",
          "$ref": "#/definitions/Period"
        }
      }
    }
  }
}
```