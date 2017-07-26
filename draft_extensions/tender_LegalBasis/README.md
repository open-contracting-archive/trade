Legal basis
===============
"The **EU** requires the legal basis for the procurement procedure to be published. There is a short codelist of the different directives, a regulation or national law that can be entered against this field. See below

<Directive 2014/23/EU>
<Directive 2014/24/EU>
<Directive 2014/25/EU>
<Directive 2009/81/EC>
<Regulation 966/2012>
<National procurement law>"

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. This is a standard procurement and so Directive 2014/24/EU on public procurement applies.
```json
{
		"legalBasis": "Directive 2014/24/EU"
 }
```
Schema Extension
=======
```json
    {
      "definitions": {
        "Tender": {
          "properties": {
            "legalBasis": {
              "title": "Tender legal basis",
              "description": "The legal basis of the tender based on the [legalBasis codelist](http://standard.open-contracting.org/......",
              "type": [
                "string",
                "null"
              ],
              "enum": [
                "Directive 2014/23/EU",
                "Directive 2014/24/EU",
                "Directive 2014/25/EU",
                "Directive 2009/81/EC",
                "Regulation 966/2012",
                "National procurement law",
                "null"
              ]
            }
          }
        }
      }
    }
```    