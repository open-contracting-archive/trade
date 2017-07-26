Is European Union Funded
===============
A True or False field to indicate whether this procurement is related to a project and/or programme financed by European Union funds.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The procurement is related to a project and/or programme financed by European Union funds

```json
{
  "budget": [
		{ 
		"isEuropeanUnionFunded": "true" 
		}
	]
}    
```

Schema Extension
=======
```json
{
  "definitions": {
    "Budget": {
      "properties": {
        "properties": {
          "isEuropeanUnionFunded": {
            "title": "Is European Union Funded",
            "description": "A True or False field to indicate whether this procurement is related to a project and/or programme financed by European Union funds.",
            "type": "boolean"
          }
        }
      }
    }
  }
}
```