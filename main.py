import gspread
import time
from html2image import Html2Image
import os
import sys

# Gets absolute path to resource
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    # Paths to files/folders being updated/created
    Image_Cache = os.path.join(application_path + "/Image_Cache")
    value = os.path.join(application_path + "/value.txt")
elif __file__:
    application_path = os.path.dirname('main.py')
    # Paths to files/folders being updated/created
    Image_Cache = os.path.join(application_path + "Image_Cache")
    value = os.path.join(application_path + "value.txt")

# Path to service account    
service_account = resource_path("mcnexus-image_generation-service_account.json")

# Making sure Image_Cache is present
if not os.path.exists(Image_Cache):
    os.makedirs(Image_Cache)

# Image Generation
def generateImage(text, time):
    # Generate image parameters
    hti = Html2Image(browser="chrome")
    hti.size = (1000, 1000)
    hti.output_path = Image_Cache

    # Name File and Saving
    file_name = "{}.png".format(time).replace(":", "").replace("/", "-")

    hti.screenshot(
        html_str="<p class='post'>" + text + "<br> <br>" + time + "</p>",
        css_str=[
            "body {background: black; color: white; font-size: 40px; display: flex; align-items: center; justify-content: center;}",
            ".post {width: 90%; font-family: Helvetica; font-weight: light; line-height: 1.5;}",
        ],
        save_as=file_name,
    )


# Open file with row # of most recent image generated
try:
    f = open(value, "r+")
# If file does not exist create then open
except:
    open(value, "w")
    f = open(value, "r+")
    print("value.txt created")

# Read the most recently read row / request input
try:
    postrow = int(f.readline())
# if postrow == None or postrow == "":
except:
    postrow = input(
        str(
            "\nPlease enter the row you wish to start generating from (generating from the top down): "
        )
    )
    postrow = int(postrow)

# As this account / Please Reach out for the service account file
gc = gspread.service_account(filename=service_account)
# Open this sheet
sh = gc.open_by_url(
    "https://docs.google.com/spreadsheets/d/1gENw0k_10SGi7nOlBgodP19Zd2aFtfJvvhbkNv7UxVM/edit?usp=sharing"
)

# Make sheet easier to reference
worksheet = sh.sheet1

# Post and Time
post_time = worksheet.get("A{}".format(postrow)).first()
post_text = worksheet.get("B{}".format(postrow)).first()

# Notify user of starting row date
if post_time == None:
    print("No new posts to generate.")
    exit()
else:
    print("Starting with Missed Connection", post_time)


# Choose to continue or not based on the last generated row}
while post_time != None:
    # Print Row
    print(post_time, "Generating...")
    # Generate Image
    generateImage(post_text, post_time)
    # Onto the next row
    postrow += 1
    # Record most recent post time
    most_recent_time = post_time
    # Update Post and Time
    post_time = worksheet.get("A{}".format(postrow)).first()
    post_text = worksheet.get("B{}".format(postrow)).first()
    # Space out requests, Google doesn't like us making too many requests at once
    time.sleep(2)
else:
    # Record most recent post time
    with open(value, "w") as f:
        f.write(str(postrow))
    most_recent_postrow = postrow - 1
    print(
        "\nPosts generated up to {} on row {}".format(
            most_recent_time, most_recent_postrow
        )
    )
