from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

# IMPLEMENT IN FUTURE: I am pretty sure that the service does not need to be created every time I run the script, what is needed is probably the token_drive_v3_pickle file that is generated. Later I should have the script first look for the file and if it is not there, then create it. ALSO for when the file is there but you get the invalid or rejected error, it can delete then generate the file on error so I do not have to manually do it.
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def UploadImage(image_path,date):
    folder_id = '1F5WX2BonUA0ralcOGpJCJZjrL4DFytJZ'
    mime_type = 'image/jpeg'

    file_metadata = {
        'name': date,
        'parents': [folder_id]
    }

    media = MediaFileUpload(image_path, mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

print ("test2")