Submission Languages
===============
EU, UNCITRAL and WTO all specify a requirement to publish the language or languages that tenders or requests for participation may be submitted in. The EU specifies the publication of a language code.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. yes
WTO .......................................... yes

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. Tenderers can submits their responses in English or Spanish.

```json
"Tender": {
        "submissionLanguages": ["en", "es"]
        }
```   

Schema Extension
=======
```json
{
  "definitions": {
    "Tender": {
      "properties": {
        "submissionLanguages": {
          "title": "Submission Languages",
          "description": "Language(s) in which tenderers may submit, drawn from the [submissionLanguages codelist](http://standard.open-contracting.org/1.1-dev/en/schema/codelists/#submission-languages ZZZ Needs to be obtained)",
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          },
          "enum": [
            "ZZZ Needs to be obtained",
            null
          ],
          "codelist": "submissionLanguages.csv",
          "openCodelist": false
        }
      }
    }
  }
}
```