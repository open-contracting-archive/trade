Recurrent Procurement
===============
The EU require the publication of whether this is a recurrent procurement and if so the estimated date(s) for subsequent call(s) for competition (date fields) and any further information (string field(s)).

WTO requirements require estimated dates and so are a subset of the EU requirements.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... yes

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. 
There are two lots, "lot-1" and "lot-2". "lot-2" is a recurrent procurement, while "lot-1" is not.
"lot-2" has one subsequent call for competition, the estimated dates of which are October, November, December 2019.

```json
{
        "Lots": {
                "recurrentProcurement": [
                  { 
                "isRecurrent": false,
                "dates": "",
                "description": "This lot is not recurrent"
                },
                { 
                "recurrentProcurement": true,
                "dates": [
	                {
		                "startDate": "2019-10-01T00:00:00Z",
		                "endDate": "2019-12-31T23:59:59Z",
		                "maxExtentDate": "",
		                "duration": ""
                "description": "This lot is recurrent. The estimated dates for the subsequent call for competition are October, November, December 2019."
                }                
            ]
```

Schema Extension
=======
```json
{
  "definitions": {
    "RecurrentProcurement": {
      "title": "Recurrent Procurement",
      "type": "object",
      "properties": {
        "isRecurrent": {
          "title": "Is recurrent?",
          "description": "A True/False field to indicate whether this is a recurrent procurement",
          "type": "boolean"
        },
        "dates": {
          "title": "Dates",
          "description": "Estimated date(s) for subsequent call(s) for competition",
          "type": "array",
	      "items": {
	      	"$ref": "#/definitions/Period"
          		 }
        },
        "description": {
          "title": "description",
          "description": "Any further information about subsequent call(s) for competition.",
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "Lots": {
      "properties": {
        "recurrentProcurement": {
          "title": "Recurrent Procurement",
          "description": "Details of possible recurrent procurements and their subsequent calls for competition.",
          "type": "array",
          "items": {
            "$ref": "#/definitions/RecurrentProcurement"
          }
        }
      }
    }
  }
}
```