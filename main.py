import gspread
from datetime import datetime

# Pull entries from Google Sheet
gc = gspread.service_account('test-project-364817-58d0da683a9b.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1GAGsJhb3pH9WLwLs7Kj9F_h0x0lweRL30qURPBguGfw/edit?usp=sharing')
worksheet = sh.sheet1

# Row to start pulling data from
postrow = 2
# Post and Time
post = worksheet.get('A{}'.format(postrow)).first()
posttime = worksheet.get('B{}'.format(postrow)).first()
# Translating Date
posttime_datetime_object = datetime.strptime(posttime, '%m/%d/%Y %H:%M:%S')

# Script chooses to continue or not based on the time of the last generated post
from PrevPostTime import lastposttime, placeholderposttime

lastposttime = datetime.strptime(lastposttime, '%m/%d/%Y %H:%M:%S')
placeholderposttime = datetime.strptime(placeholderposttime, '%m/%d/%Y %H:%M:%S')

print(lastposttime,placeholderposttime)

while posttime_datetime_object > lastposttime:
    # Generate Image
    import GenerateImage
    posttime_datetime_object = placeholderposttime
    postrow += 1
    
lastposttime = placeholderposttime

# # Print Results
# print(post,'\n',type(posttime_datetime_object),posttime_datetime_object)