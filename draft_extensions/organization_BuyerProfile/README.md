Buyer Profile Uri
===============
The buyer profile is an EU specific field. It is optional and allows buyers to create a profile containing some of the standard requirements to publish about their organization.

Organizations with this field
===============

European Union ........................ yes
UNCITRAL ................................. no
WTO .......................................... no

Worked Example
==============
The London Borough of Haringey issues a tender and a notice is published through the EU's TED Notice Form. The London Borough of Haringey has an online buyer profile and so they publish its uri.

```json
{
  "organization": [
	    {
		    {
    		"buyerProfile": "http://haringey.g2b.info/cgi-gen/profile.pl?action=view_profile&oid=6555"
		     }
		}
    ]
}         
```

Schema Extension
=======
```json
    {
      "definitions": {
        "Organization": {
          "properties": {
            "buyerProfile": {
              "title": "Buyer Profile uri",
              "description": "The uri of the organization's buyer profile. Specified by EU",
              "type": [
                "string",
                "null"
              ],
              "format": "uri"
            }
          }
        }
      }
    }
```