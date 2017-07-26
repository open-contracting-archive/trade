Has Previous Notice
===============
The EU requires that notices within the same procurement procedure are connected. This is done by publishing the details of the previous notice. 

This field records whether there has been a previous notice or not.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A contract award is made and a notice published through the EU's TED Contract Award Notice Form. This contract award follows a tender notice that was published through the EU's TED Contract Notice Form..
The publisher flags that this notice is connected to a previous notice.

```json
{
  "release": [
	    {
        "hasPreviousNotice": "true"
		}
	 ]
}
        
```
Schema Extension
=======
```json
{
  "properties": {
    "hasPreviousNotice": {
      "title": "Has previous notice?",
      "description": "A True or False field to indicate whether this TED notice is connected to a previous notice, either TED or national. Required by EU.",
      "type": "boolean"
    }
  }
}
```