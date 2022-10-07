# Missed_Connections

Goal:
For every 10 new entries at https://docs.google.com/spreadsheets/d/1oVLtL27b7W3RwxUavTboa5oyxc7tiF0uvcIbBvdpR_0/edit#gid=0
Generate images like the ones in previous posts at https://www.instagram.com/rutgers.missedconnections/?hl=en



Ideally I want to be able to...
1. At every update to the missed connections google sheet, have a script take the entry and generate an image.

2. After 10 images are created, either 
  send them to whoever will post them (EASY) 
    or 
  send to be vetted, then, if approved, post the pictures on the account using Graph API (HARD) 

3. Will have to figure out a way to properly generate a description based on the time of posting/entry date, but that is for later.

# Running
1. `pip install -r requirements.txt`
2. `python missed_connection.py`