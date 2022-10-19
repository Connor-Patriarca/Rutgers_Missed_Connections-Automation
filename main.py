import gspread
from datetime import datetime
from GenerateImage import generateImage

# Prompt Script to start looking from when?
dateprompt = input(str("\nWhat date/time should I start working from?\nFormat is 'mm/dd/yyyy hh:mm:ss' : "))

# Create variables with that date
LastImageTime = datetime.strptime(dateprompt, '%m/%d/%Y %H:%M:%S')

# Pull entries from Google Sheet
gc = gspread.service_account('rutgers-missed-connections-b4bf6b9aa508.json')
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
print(posttime_datetime_object)

while posttime_datetime_object >= LastImageTime:
    # Generate Image
    generateImage(post)
    postrow += 1
    # Post and Time
    post = worksheet.get('A{}'.format(postrow)).first()
    posttime = worksheet.get('B{}'.format(postrow)).first()
    # Translating Date
    posttime_datetime_object = datetime.strptime(posttime, '%m/%d/%Y %H:%M:%S')

# For when script is put on timer    
posttime_datetime_object = LastImageTime