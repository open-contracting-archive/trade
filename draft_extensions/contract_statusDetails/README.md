Status Details
===============
The EU contract award notice lists a number of reasons why an award may not be made. These can be mapped to the OCDS awardStatus codelist but information will be lost as the OCDS is more general. The awardStatus codelist is closed.

The EU require this to be published through a contract award notice and not a tender notice. In OCDS the Tender section is better placed to hold this data.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is cancelled and a Contract Award Notice is published. The tender was cancelled by the buyer. 

```json
{
  "Award": {
	"status": "unsuccessful",
	"statusDetails": "The procurement was cancelled by the buyer"
  }
}
```	

Schema Extension
=======
```json
{
  "definitions": {
    "Award": {
      "properties": {
        "statusDetails": {
          "title": "Status details",
          "description": "Additional details of a tender status.",
          "type": "string"
        }
      }
    }
  }
}
```