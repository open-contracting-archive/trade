"""
build_schema.py 

Fetches published OCDS extensions from the extensions registry and applies them to the 1.1 schema.

Applies all extensions in child folders of the current path to the schema. 

"""

import requests
import json
import json_merge_patch
from collections import OrderedDict
import glob
import os

# extensions_to_merge = ['lots']
extensions_to_merge = ['partyScale','lots','requirements','participation_fee','related_process','bids','bid_statistics']

GIT_REF = "master"
location = "http://standard.open-contracting.org/extension_registry/{}/extensions.json".format(GIT_REF)
extension_json = requests.get(location).json()

schema = requests.get("http://standard.open-contracting.org/1.1/en/release-schema.json").json()

# with open('release-schema.json') as schema_file:
#    schema = json.load(schema_file,object_pairs_hook=OrderedDict)

for extension in extension_json['extensions']:
    try:
        if extension['slug'] in extensions_to_merge:
            print("Merging " + extension['slug'] )
            extension_patch = requests.get(extension['url'].rstrip("/") + "/" + "release-schema.json").json()
            schema = json_merge_patch.merge(schema, extension_patch)
    except KeyError:
        print("Nothing")
        pass

for folder in glob.glob("*_*"):
    if(os.path.isdir(folder)):
        try:
            with open(folder + "/release-schema.json",'r') as extension_patch_file:
                print("Merging "+ folder)
                extension_patch = json.loads(extension_patch_file.read(),object_pairs_hook=OrderedDict)
                schema = json_merge_patch.merge(schema, extension_patch)
        except Exception:
            print("Problem merging from " + folder)
            pass




with open('release-schema-patched.json','w') as schema_file:
    json.dump(schema,schema_file,indent=4)
