Procurement Method Additional Information
===============
EU and UNCITRAL have more detail in their codelists than the three elements: Open, Selective or Limited in WTO and OCDS (which also has an additional 'direct' field). 

tender/procurementMethod is used to indicate open, selective, limited or direct, while tender/procurementMethodDetails can be used to indicate EU and UNCITRAL specific categories. This is a free text field.

Additional information is required for ""Competitive procedure with negotiation"", ""Innovation partnership"" and ""Specific procedure based on national legislation"" and this will be explained in the user documentation. It can be provided in procurementMethodAdditionalInformation.


Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. yes
WTO .......................................... yes

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The procurement method is an innovation partnership. The number of solutions or tenders will be reduced in successive stages of the procedure.

```json
    {
    "Tender"  {
	"procurementMethodDetails":"innovationPartnership",
    "procurementMethodAdditionalInformation": "The number of solutions or tenders will be reduced in successive stages of the procedure"
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
        "procurementMethodAdditionalInformation": {
          "title": "Procurement method additional information",
          "description": "Additional information about the procurement method.",
          "type": [
            "string",
            "null"
          ]
        }
      }
    }
  }
}
```