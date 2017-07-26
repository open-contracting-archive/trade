Design contest
===============
A design contest is a form of limited procurement with competition.

The **EU** specify the requirements for publishing the details of a design contest. 

These include: whether the contest has prizes and, where it does, the value of each prize and later its winner; whether any service contract following the contest will be awarded to one of the winners of the contest; a description of any payments that will be paid to participants; a list of the jury members; a list of any pre-selected participants and whether the decision of the jury will be binding on the buyer.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The design contest is to build new cycle lanes for the London Borough of Barnet.

The contest has prizes for the first three winners, of £500, £200 and £100 respectively. The jury members are "David Solomon", "Brigitte Reinhard" and "Malkit Kaur Dhaliwal". Their decision is binding on the buyer and will result in a service contract. Participants will not be paid. One participant, "AnyCorp Ltd" has been pre-selected.

```json
{
  "tender": {
    "designContest": {
    		"hasPrizes": "true",
    		"Prizes":[ 
    			{"id":"1",
            	"description":"First Prize",
            	"classification": {
            		"scheme": "CPV",
            		"id": "45233162-2",
            		"description": "Cycle path construction work",         		
            	      "uri":"http://simap.ted.europa.eu/cpv"
			      },
			 "additionalClassifications": "",
			 "quantity": "1",
			 "unit":{
			 	"name": "Design Contest Prize"
			 	"value": {
			 		"amount": "500",
			 		"currency": "GBP"
			     	}
			    }
		      },
		      {"id":"2",
			"description":"Second Prize",
			"classification": {
				"scheme": "CPV",
				"id": "45233162-2",
				"description": "Cycle path construction work",         		
				"uri":"http://simap.ted.europa.eu/cpv"
				},
			"quantity": "1",
			"unit":{
				"name": "Design Contest Prize"
				"value": {
					"amount": "200",
					"currency": "GBP"
					}
				}
		      },
			{"id":"3",
			"description":"Third Prize",
			"classification": {
				"scheme": "CPV",
				"id": "45233162-2",
				"description": "Cycle path construction work",         		
				"uri":"http://simap.ted.europa.eu/cpv"
				},
			"quantity": "1",
			"unit":{
				"name": "Design Contest Prize"
				"value": {
					"amount": "100",
					"currency": "GBP"
					}
				}
		      },
	      ]
		"paymentsToParticipants": "Participants will not be paid",
		"serviceContractAward": "true",
		"juryDecisionBinding": "true",
		"juryMembers": [ 
    			{"id": "0001",
    			"name": "David Solomon"
    			},
    			{"id": "0002",
			"name": "Brigitte Reinhard"
    			},
    			{"id": "0003",
			"name": "Malkit Kaur Dhaliwal"
    			}
    		]
    		"participants": [ 
    			{"id": "GB-COH-1234567844",
           "name": "AnyCorp Ltd"}
    		]    		
    }
  }
}
```


**The following is dependent on whether this is right place to record the ids of the winning participants**

When the award is made the three winners are FIRST: Selena Manning, SECOND, "Norma Amici" and THIRD, "Brigitte Reinhard".



Schema Extension
=======

```json
{
  "definitions": {
    "DesignContest": {
      "title": "Design Contests",
      "type": "object",
      "properties": {
        "hasPrizes": {
          "title": "Tender design contest has prizes",
          "description": "A True/False field to indicate if the design contest has prizes. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "Prizes": {
          "title": "Tender prizes",
          "description": "Details about the prize(s) for the winner(s) of the design contest. Required by the EU",
          "type": "array",
          "$ref": "#/definitions/Items",
          "uniqueItems": true
        },
        "paymentsToParticipants": {
          "title": "Tender payments to participants",
          "description": "Details of any payments that will be made to participants in the design contest. Required by the EU",
          "type": [
            "string",
            "null"
          ]
        },
        "serviceContractAward": {
          "title": "Tender service contract award",
          "description": "A True/False field to indicate whether a service contract will be awarded to the winner(s) of the design contest. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "juryDecisionBinding": {
          "title": "Tender design contest jury decision binding",
          "description": "A True/False field to indicate whether the jury decision of the design contest is binding. Required by the EU",
          "type": [
            "boolean",
            "null"
          ]
        },
        "juryMembers": {
          "title": "Tender design contest jury members",
          "description": "A list of the jury members for of the design contest. Required by the EU",
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrganizationReference"
          },
        "uniqueItems": true
        },
        "participants": {
          "title": "Tender design contest participants",
          "description": "A list of the pre-selected participants for the design contest. Required by the EU",
          "type": "array",
          "items": {
            "$ref": "#/definitions/OrganizationReference"
          },
        "uniqueItems": true
        }
      }
    },
    "Tender": {
      "properties": {
        "designContest": {
          "title": "Tender design contest",
          "description": "The tender takes the form of a design contest. Fields that relate specifically to the design contest are modelled here. Required by the EU",
          "$ref": "#/definitions/DesignContest"
        }
      }
    }
  }
}
```