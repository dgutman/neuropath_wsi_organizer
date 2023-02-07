"""David A Gutman
2/7/2023
imageOrgFolderTagger

This will walk through a collection/base Folder and add special tags (metadata)
to specific folders so they are collapsed by default in image organizer

"""

import girder_client, os
from dotenv import load_dotenv

load_dotenv()

gc = girder_client.GirderClient(apiUrl=os.environ.get("dsaApiUrl"))

gc.authenticate(apiKey=os.environ.get("dsaApiToken"))


## Loop through a collection and then find folders that are digits (i.e. years)
## Then add the appropriate key to the folder

for yr in gc.listFolder("63d98235e08050e0a7a8d75d", parentFolderType="collection"):
    if yr["name"].isdigit():
        print(yr["name"])
        ## Now loop through all the folders and add the metadata that makes IO happy
        ## Now roll through the patients
        for pt in gc.listFolder(yr["_id"]):
            gc.addMetadataToFolder(pt["_id"], {"isLinear": True})
