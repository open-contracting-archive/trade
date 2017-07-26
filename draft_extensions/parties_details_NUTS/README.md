NUTS Code
===============
The EU uses the NUTS (Classification of Territorial Units for Statistics) scheme to classify regions within the EU. In their notice forms they specify the use of NUTS-3 codes, which are regions with a population between 150 000 and 800 000 inhabitants. If the place of performance covers many NUTS 3 areas (e.g. a highway, a national network of job centres), then a less detailed NUTS code ("NUTS 2" or even "NUTS 1") can be used.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
The London Borough of Haringey issues a tender and a notice is published through the EU's TED Notice Form. The London Borough of Haringey has a NUTS Code of UKG13

```json 
  
"Organization": {
  "details": {
    "NUTSCode": "UKG13" 
  } 
} 
```

Schema Extension
=======
```json
{
  "definitions": {
    "Organization": {
      "properties": {
        "details": {
          "description": "Additional classification information about parties from the NUTS (Classification of Territorial Units for Statistics) scheme. Required by the EU.",
          "type": [
            "object",
            "null"
          ],
          "properties": {
            "NUTSCode": {
              "title": "NUTS Code",
              "description": "The most detailed level of NUTS codes, NUTS 3 should be used and it should be taken from the EU codelist linked from http://ec.europa.eu/eurostat/ramon/index.cfm?TargetUrl=DSP_PUB_WELC.",
              "type": [
                "string",
                "null"
              ]
		}
          }
        }
      }
    }
  }
}
```