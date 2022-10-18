import gspread
from datetime import datetime
from GenerateImage import generateImage

# Prompt Script to start looking from when?
dateprompt = input(str("\nWhat date/time should I start working from?\nFormat is 'mm/dd/yyyy hh:mm:ss' : "))

# Create variables with that date
lastposttime = datetime.strptime(dateprompt, '%m/%d/%Y %H:%M:%S')
placeholderposttime = datetime.strptime(dateprompt, '%m/%d/%Y %H:%M:%S')


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
currently_pulled_post_time = datetime.strptime(posttime, '%m/%d/%Y %H:%M:%S')

# Script chooses to continue or not based on the time of the last generated post
print(currently_pulled_post_time)
print(lastposttime,placeholderposttime)
print(type(lastposttime),type(placeholderposttime))

while currently_pulled_post_time > lastposttime:
    # Generate Image
    generateImage(post)
    posttime_datetime_object = placeholderposttime
    postrow += 1
    
lastposttime = placeholderposttime

# # Print Results
# print(post,'\n',type(posttime_datetime_object),posttime_datetime_object)