# Missed_Connections Automation

Goal:
For every new entry at (Insert Link To Missed Connections Google Sheet Here)
this will generate an image in the style of this Instagram page: https://www.instagram.com/rutgers.missedconnections/?hl=en

Process:
1. At each new submission to the Sheet, pull the entry+time posted and generate an image.
2. Generate Image
3. Send each image to a shared Google Drive folder, each photo name being the date/time the post was made.
   Each picture in the folder will be placed in folders marked by each day, so it is easier to keep track of them.

# Running
1. `pip install -r requirements.txt`
2. `python main.py`
