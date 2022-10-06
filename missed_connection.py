from PIL import ImageFont, Image, ImageDraw
from pilmoji import Pilmoji
import textwrap

def missed_connection():
    # Font
    font = ImageFont.truetype("OriginalFont.ttf", 40)
    # font = ImageFont.truetype("arial.ttf", 40)

    # Source text, and wrap it. 500 character limit
    userinput = "hi everyone i’m nicolette alexandra (they/them) i’m a photographer 📸 and i have a literary/art review where I publish my work. i’m looking for a couple of models to shoot some themed concepts that i have. let me know if you’d be interested in being one my insta is @julietrosereview and @alexandranicolettte :)))☁️🪐"
    text = textwrap.fill(userinput, 48, max_lines=15)

    # Create image and put the text on it.
    with Image.new("RGB", (1000,1000), 'black') as image:
        with Pilmoji(image, emoji_position_offset=(0,0),emoji_scale_factor=1.2) as pilmoji:
            pilmoji.text((50, 500), text.strip(), ('white'), font, spacing=25)
            # pilmoji.text((50, 500), text, ('white'), font, anchor='lm', spacing=25)

    # # Create image and put the text on it. (Without Pilmoji)
    # img = Image.new("RGB", (1000,1000), 'black')
    # draw = ImageDraw.Draw(img)
    # # draw = Pilmoji(img, emoji_position_offset=(0,-20))
    # draw.text((50, 500), text, fontcolor, font, anchor='lm', spacing=25)

    image.show()
    # img.save("missed_connection.jpg")

#test change
missed_connection()