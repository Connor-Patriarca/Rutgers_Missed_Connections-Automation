import gspread
from datetime import datetime
from GenerateImage import generateImage
import time

# # Prompt script to start looking from when?
# dateprompt = input(str("\nWhat date/time should I start working from?\nFormat is 'mm/dd/yyyy hh:mm:ss' : "))

# # Create variables with that date
# LastImageTime = datetime.strptime(dateprompt, '%m/%d/%Y %H:%M:%S')

# Pull time of most recent post image generated
f = open("value.txt", 'r')

# Create variables with that date
most_recent_date = f. readline()
LastImageTime = datetime.strptime(most_recent_date, '%m/%d/%Y %H:%M:%S')

# Pull entries from Google Sheet
gc = gspread.service_account('service_account.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1GAGsJhb3pH9WLwLs7Kj9F_h0x0lweRL30qURPBguGfw/edit?usp=sharing')
worksheet = sh.sheet1

# Row to start pulling data from
postrow = 2
# Post and Time
post = worksheet.get('A{}'.format(postrow)).first()
posttime = worksheet.get('B{}'.format(postrow)).first()
# Translating Date
posttime_datetime_object = datetime.strptime(posttime, '%m/%d/%Y %H:%M:%S')

# Record most recent post time
most_recent_date = worksheet.get('B2'.format(postrow)).first()
with open('value.txt', 'w') as f:
    f.write(most_recent_date)

# Script chooses to continue or not based on the time of the last generated post
while posttime_datetime_object >= LastImageTime:
    print('anothuh one...')
    # Generate Image
    generateImage(post,posttime,posttime_datetime_object)
    postrow += 1
    # Post and Time
    post = worksheet.get('A{}'.format(postrow)).first()
    posttime = worksheet.get('B{}'.format(postrow)).first()
    # Translating Date
    posttime_datetime_object = datetime.strptime(posttime, '%m/%d/%Y %H:%M:%S')
    time.sleep(2)

print('Posts generated up to',most_recent_date)