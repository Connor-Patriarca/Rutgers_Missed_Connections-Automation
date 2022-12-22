from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

# IMPLEMENT IN FUTURE: I am pretty sure that the service does not need to be created every time I run the script, what is needed is probably the token_drive_v3_pickle file that is generated. Later I should have the script first look for the file and if it is not there, then create it. ALSO for when the file is there but you get the invalid or rejected error, it can delete then generate the file on error so I do not have to manually do it.
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def UploadImage(image_path, date):
    DatePath = date[0:date.index(" ")].replace('/','-')

    # ******************************************************
    # TODO nest this process inside of itself to handle month then day
    # does_folder_exist("Jan") .... does_folder_exist (01-01-2022) ....
    folder_path = does_folder_exist(DatePath)
    if folder_path == []:
        folder_id = create_folder(DatePath)
    else: 
        folder_id = folder_path[0]["id"]
        # TODO add safety here to validate if there is more then one folder found and handle it if there is...aka delete something...
        # service.files().delete(fileId="....file_id....").execute()
    # ******************************************************
   
    file_metadata = {
        'name': date,
        'parents': [folder_id]
    }

    mime_type = 'image/jpeg'
    media = MediaFileUpload(image_path, mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print("Successfully uploaded image to folderId=" + folder_id)


def create_folder(folder_name): 
    folder_id = '1F5WX2BonUA0ralcOGpJCJZjrL4DFytJZ'  
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [folder_id]
    }

    file = service.files().create(body=file_metadata, fields='id'
                                      ).execute()
    print(F'Creating new folder with ID="{file.get("id")}".')
    return file.get('id')


def does_folder_exist(folder_name): 
    files = []
    page_token = None
    while True:
        response = service.files().list(q="mimeType='application/vnd.google-apps.folder' and name='" + folder_name + "'",
                                        spaces='drive',
                                        fields='nextPageToken, '
                                                'files(id, name)',
                                        pageToken=page_token).execute()
        for file in response.get('files', []):
            print(F'Found file: {file.get("name")}, {file.get("id")}')
        files.extend(response.get('files', []))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break    

    print ("Folder (" + folder_name + ") was found " + str(len(files)) + " times in the drive")
    return files


def delete_mistake_folder(folder_name):
    files = []
    page_token = None
    while True:
        response = service.files().list(q="mimeType='application/vnd.google-apps.folder' and name='" + folder_name + "'",
                                        spaces='drive',
                                        fields='nextPageToken, '
                                                'files(id, name)',
                                        pageToken=page_token).execute()
        for file in response.get('files', []):
            print(F'Found file: {file.get("name")}, {file.get("id")}')
            service.files().delete(fileId=file.get("id")).execute()
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break    

delete_mistake_folder("12-21-2022")