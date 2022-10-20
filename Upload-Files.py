from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1F5WX2BonUA0ralcOGpJCJZjrL4DFytJZ'
file_names = ['mike1.jpg','mike2.jpg']
mime_types = ['image/jpeg','image/jpeg']

for file_name, mime_type in zip(file_names,mime_types):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload('Test Images/{0}'.format(file_name), mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()