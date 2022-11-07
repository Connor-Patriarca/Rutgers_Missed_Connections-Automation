from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def UploadImage(image_path,date):
    folder_id = '1b1KE_71vPNoO02-JGsTH0uyEHEdVEW5N'
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