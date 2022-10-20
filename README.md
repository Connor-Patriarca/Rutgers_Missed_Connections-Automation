# Missed_Connections

Goal:
For every 10 new entries at https://docs.google.com/spreadsheets/d/1oVLtL27b7W3RwxUavTboa5oyxc7tiF0uvcIbBvdpR_0/edit#gid=0
this script will generate images like the ones in previous posts at https://www.instagram.com/rutgers.missedconnections/?hl=en

This here will...
1. At each new submission to the Sheet, pull the entry+time posted and generate an image.
2. Send each image to a shared Google Drive folder, each photo name being the date/time the post was made.
   Each picture in the folder will be placed in folders marked by each day, so it is easier to keep track of them.

# Running
1. `pip install -r requirements.txt`
2. `python main.py`
