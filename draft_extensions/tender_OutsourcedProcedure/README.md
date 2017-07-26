Outsourced procurement
===============
The EU requires the publication of whether the procurement procedure has been outsourced to a private company.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
A tender is issued and a notice published through the EU's TED Notice Form. The procurement procedure has been outsourced to Procurement Management Partners Ltd.

```json
{
    "procedureOutsourcing":{
        "procedureOutsourced":true,
        "outsourcedTo":{
            "id":"GB-COH-1234567",
            "name":"Procurement Management Partners Ltd"
        }
    }
}
```


Schema Extension
=======
```json
{
  "definitions": {
    "ProcedureOutsourcing": {
      "title": "Procedure Outsourcing",
      "type": "object",
      "properties": {
        "procedureOutsourced": {
          "title": "procedureOutsourced",
          "description": "A True/False field to indicate whether the procurement procedure has been outsourced",
          "type": "boolean"
        },
        "outsourcedTo": {
          "title": "Outsourced To",
          "description": "An organization reference to identify the organization that is running the outsourced procedure",
          "$ref": "#/definitions/Organization"
        }
      }
    },
    "Tender": {
      "properties": {
        "procedureOutsourcing": {
          "title": "Procedure Outsourcing",
          "description": "Whether the procurement procedure has been outsourced. If it has then a record of the organisation that is running the procedure on behalf of the buyer",
          "$ref": "#/definitions/ProcedureOutsourcing"
        }
      }
    }
  }
}
```