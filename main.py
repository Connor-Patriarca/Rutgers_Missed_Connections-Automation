import gspread
from datetime import datetime
from GenerateImage import generateImage
import time
import os

# Pull time of most recent post image generated
f = open("value.txt", 'r')

# Create variables with that date
most_recent_date = f. readline()
LastImageTime = datetime.strptime(most_recent_date, '%m/%d/%Y %H:%M:%S')

# Pull entries from Google Sheet
gc = gspread.service_account('service_account.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1GAGsJhb3pH9WLwLs7Kj9F_h0x0lweRL30qURPBguGfw/edit?usp=sharing')

# google.auth.exceptions.TransportError: HTTPSConnectionPool(host='oauth2.googleapis.com', port=443): Max retries exceeded with url: /token (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000001C4FEB76950>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

worksheet = sh.sheet1

# Row to start pulling data from
postrow = 2
# Post and Time
post = worksheet.get('A{}'.format(postrow)).first()
posttime = worksheet.get('B{}'.format(postrow)).first()
# Translating Date
posttime_datetime_object = datetime.strptime(posttime, '%m/%d/%Y %H:%M:%S')

# Script chooses to continue or not based on the time of the last generated post
while posttime_datetime_object > LastImageTime:
    # Generate Image
    generateImage(post,posttime,posttime_datetime_object)
    postrow += 1
    # Post and Time
    post = worksheet.get('A{}'.format(postrow)).first()
    posttime = worksheet.get('B{}'.format(postrow)).first()
    # Translating Date
    posttime_datetime_object = datetime.strptime(posttime, '%m/%d/%Y %H:%M:%S')
    time.sleep(2)

# Record most recent post time
most_recent_date = worksheet.get('B2'.format(postrow)).first()
with open('value.txt', 'w') as f:
    f.write(most_recent_date)

print('Posts generated up to',most_recent_date)