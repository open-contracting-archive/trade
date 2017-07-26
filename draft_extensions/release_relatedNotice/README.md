Related Notice
===============
Notices are public procurement notices that provide information on public procurement contracts, according to the EU rules on public procurements. Notices can be published in EU Member States, the European Economic Area (EEA) and beyond.

The EU requires that notices within the same procurement procedure are connected. This is done by publishing the details of the previous notice and can be modelled in OCDS using the ocid and the record. 

Where a notice was preceded only by a notice at the national level then information about the national notice can be provided.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A contract award is made and a notice published through the EU's TED Contract Award Notice Form. This contract award follows a tender notice that was published through a national scheme. The publisher provides the details of the previous notice in the relatedProcess field.

```json
"release": [
    {
	  "relatedProcess": {
	    "alternativeID": {
	    "uri":""http://standard.open-contracting.org/examples/",
	    "scheme": "ZZZ_NATIONAL",
	    "id": "cycling-barnet-tender" 
	    },
	  "objectOfProcurementInPIN": "ZZZcheckWithEUExperts"
		}
	]
}
```


Schema Extension
=======
```json
{
  "definitions": {
    "relatedProcess": {
      "description": "A link to a related contracting process in OCDS and the type of relationship.",
      "type": "object",
      "title": "Related Process",
      "properties": {
        "alternativeID": {
          "title": "Alternative Identifier",
          "description": "An alternative identifier for this procurement process. This can be used when a procurement process has published outside OCDS. In the case of EU Notices this field can be used when a notice was preceded only by a notice at the national level.",
          "$ref": "#/definitions/Identifier"
          },          
        "objectOfProcurementInPIN": {
	    "title": "Object of the procurement within the PIN",
	    "type": [
	      "string",
	      "null"
	      ],
	    "description": "If the related notice linked to is a planning or 'Prior Information Notice' (PIN) that describes a number of potential tenders, the identifier of the specific Object to which this current contracting process relates should be given."
          }
        }
     }
  }
}
```