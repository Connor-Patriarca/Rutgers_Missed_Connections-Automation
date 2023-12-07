# Rutgers Missed Connections Automation

Goal:
For every new entry to a missed connections page, this program will generate an image in the desired style: 
Example of a page currently using this: https://www.instagram.com/rutgers.missedconnections/

Process:
1. The script will search through the provided dataset, starting with the row indicated by the user, and  iterate through each entry until it reaches the end.
2. Each row's fields will be used to generate an image which will then be saved to the device running the script. Each photo name is the date/time the post was made.
3. Once the end it reached, the program will save the last row an image was generated from, and will start from that row the next time it is run, continuing where it left off.

# Running
1. `pip install -r requirements.txt`
2. `python main.py`
