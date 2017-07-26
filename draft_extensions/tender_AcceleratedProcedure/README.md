Accelerated Procedure
===============
The EU require the publication of whether an accelerated procurement is being used and the justification for doing so

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. An accelerated procurement procedure is being used "for reasons of extreme urgency brought about by events unforeseeable by the contracting authority" (Article 32: 2(c))

```json
{
  "tender": [
		{ 
		"acceleratedProcedure":  {
		"isAcceleratedProcedure": "true",
		"acceleratedProcedureJustification": "for reasons of extreme urgency brought about by events unforeseeable by the contracting authority.",		
    		 }
		 }
	]
}    
```

Schema Extension
=======
```json
{
  "definitions": {
    "AcceleratedProcedure": {
      "title": "Accelerated Procedure",
      "type": "object",
      "properties": {
        "isAcceleratedProcedure": {
          "title": "is Accelerated Procedure?",
          "description": "A True/False field to indicate whether an accelerated procedure has been used for this procurement",
          "type": "boolean"
        },
        "acceleratedProcedureJustification": {
          "title": "Accelerated Procedure Justification",
          "description": "Justification for using an accelerated procedure",
          "type": [
            "string",
            "null"
          ]
        }
      }
    },
    "Tender": {
      "properties": {
        "acceleratedProcedure": {
          "title": "Accelerated Procedure",
          "description": "Details about whether an accelerated procurement is being used and the justification for doing so.",
          "$ref": "#/definitions/AcceleratedProcedure"
        }
      }
    }
  }
}
```