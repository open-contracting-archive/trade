Submisson Method Rationale
===============
The EU requires a rationale for non-electronic submission, from the following list

- Tools, devices, or file formats not generally available 
- Intellectual property right issues 
- Buyer would need specialised office equipment    
- Submission of a physical model 
- Protection of particularly sensitive information

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. Electronic submissions are not permitted as tenderers need to submit a physical model.

```json
    {
    "Tender": {
	    "submissionMethodRationale": "PHYSICAL_MODEL"
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
        "submissionMethodRationale": {
          "title": "Submisson Method Rationale",
          "description": "A value from the [submissionValueRationale codelist](http://standard.open-contracting.org/1.1-dev/en/schema/codelists/#ZZZ) that identifies the rationale where electronic submission method is not to be allowed. Required by EU.",
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "Tools, devices, or file formats not generally available",
              "Intellectual property right issues",
              "Buyer would need specialised office equipment",
              "Submission of a physical model",
              "Protection of particularly sensitive information",
              null
            ]
          }
        }
      }
    }
  }
}
```