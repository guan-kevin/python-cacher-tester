from bugswarm.common.rest_api.database_api import DatabaseAPI

def get_artifact_language(image_tag):
    bugswarmapi = DatabaseAPI()
    artifact = bugswarmapi.find_artifact(image_tag)
    return artifact.json()['lang']

def get_artifact_status(image_tag):
    bugswarmapi = DatabaseAPI()
    artifact = bugswarmapi.find_artifact(image_tag)
    return artifact.json()['status']
