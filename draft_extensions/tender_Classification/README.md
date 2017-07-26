Classification
===============
The EU require the publication of a summary CPV code for all lots in the whole procurement. This field is for EU reporting purposes.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The tender is for cycle path construction work

```json
{
	"tender": {
			"classification": "45233162"
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
        "classification": {
          "title": "Classification",
          "description": "The primary classification for the tender. Required by the EU. Uses CPV Codelist See the [itemClassificationScheme](http://standard.open-contracting.org/1.1-dev/en/schema/codelists/#item-classification-scheme).",
          "$ref": "#/definitions/Classification"
        }
      }
    }
  }
}
```