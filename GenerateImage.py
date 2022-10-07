from PIL import ImageFont, Image
from pilmoji import Pilmoji
import textwrap
from fontTools.ttLib import TTFont

# Calculating Text Size
STARTING_WIDTH =    100 #starting val for 'width' in textwrap()
PIXEL_MAX =         280 #arbitrary value i found by trial/error
LINE_HEIGHT =       63 #also ^
WIDTH, HEIGHT =     1000, 1000 #of image
ODD_LINES_OFFSET =  30 #odd amt of lines need to be vertically offset

font = TTFont('OriginalFont.ttf')
cmap = font['cmap'] #cbat
t = cmap.getcmap(3,1).cmap
s = font.getGlyphSet()
units_per_em = font['head'].unitsPerEm

# Generate Image
def getTextWidth(text,pointSize):
    total = 0
    for c in text:
        if ord(c) in t and t[ord(c)] in s:
            total += s[t[ord(c)]].width
        else:
            total += s['.notdef'].width
    total = total*float(pointSize)/units_per_em;
    return total

def missed_connection():
    # Font
    font = ImageFont.truetype("OriginalFont.ttf", 40)

    #tests
    # userinput = "MMMMMMMMMMMMMD MMMMMMMMMMMMMMMMD MMMMMMMMMMMMMMD MMAAAAAMMMMMMMD MMMMMMMMMD MMMMMMD MMMMMMMMD MMMMMMMMMMMMD MMMMMMMMD MMMMMMMMMMMD"
    # userinput = "IIIIIIIIIIIIIIIIIIIIIIIIIIIII IIIIIIIIIIIIIIIIIIIIIII IIIIIIIIIIIIIII IIIIIIIIIIIIIIIIIIII IIIIIIII IIIIIIIIIII"
    # userinput = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMM MMMMMMMM MMMMMMMMMMM"
    # userinput = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM " #1 line
    # userinput = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMM IIIIIIIIIIIIIIII " #2 lines
    # userinput = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMM IIIIIIIIIIIIIIII IIIIIIIIIIIIIIII IIIIIIIIIIIIIIII " #3 lines
    # userinput = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMM IIIIIIIIIIIIIIII IIIIIIIIIIIIIIII IIIIIIIIIIIIIII IIIIIIIIII IIIIIIIIIIIIIIIII IIIIIIIIIIIIIIIIII MMMMMMMMMMM" #4 lines
    # userinput = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMM IIIIIIIIIIIIIIII IIIIIIIIIIIIIIII IIIIIIIIIIIIIII IIIIIIIIII IIIIIIIIIIIIIIIII IIIIIIIIIIIIIIIIII MMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMM IIIIIIIIIIIIIIII IIIIIIIIIIIIIIII IIIIIIIIIIIIIII IIIIIIIIII IIIIIIIIIIIIIIIII IIIIIIIIIIIIIIIIII MMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMMMMMMMM MMMMMMMMMMMMMMMMMMMMMMM IIIIIIIIIIIIIIII IIIIIIIIIIIIIIII IIIIIIIIIIIIIII IIIIIIIIII IIIIIIIIIIIIIIIII IIIIIIIIIIIIIIIIII MMMMMMMMMMM" #12 lines
    
    userinput = "hi everyone i’m nicolette alexandra (they/them) i’m a photographer 📸 and i have a literary/art review where I publish my work. i’m looking for a couple of models to shoot some themed concepts that i have. let me know if you’d be interested in being one my insta is @julietrosereview and @alexandranicolettte :)))☁️🪐"
    
    finalMsg = ""
    good = False
    width = STARTING_WIDTH
    while not good:
        good = True
        # print(f"using {width} width")
        text = textwrap.fill(userinput, width, max_lines=15, break_long_words=True) #wrap
        for line in text.split("\n"):
            lineWidth = getTextWidth(line, 12)
            if lineWidth > PIXEL_MAX: #still cutoff, decrement width and try again
                width -= 1
                good = False
                break
        if good and len(text) > 0: #not cutoff :) add to final msg
            finalMsg += '\n' + text.split("\n")[0] #line is wrapped, add it
            userinput = ' '.join(text.split("\n")[1:]) #remove line from our input
            width = STARTING_WIDTH
            good = False #keep going
    text = finalMsg.strip()

    #center by amt of lines
    lines = len(text.split('\n'))

    # Create image and put the text on it.
    with Image.new("RGB", (WIDTH, HEIGHT), 'black') as image:
        with Pilmoji(image, emoji_position_offset=(0,0),emoji_scale_factor=1.2) as pilmoji:
            heightVal = HEIGHT//2-lines//2*LINE_HEIGHT
            if (lines%2 == 1): #odd amt of lines
                heightVal -= ODD_LINES_OFFSET
            pilmoji.text((50, heightVal), text.strip(), ('white'), font, spacing=25)

        #DEBUG - show centered cross
        # for i in range(-50, 50):
        #     image.putpixel((HEIGHT//2+i, WIDTH//2), (255, 255, 255))
        # for i in range(-50, 50):
        #     image.putpixel((HEIGHT//2, WIDTH//2+i), (255, 255, 255))

    image.show()
    # img.save("missed_connection.jpg")

missed_connection()