from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
im2 = Image.open('geeks.jpg')
d1 = ImageDraw.Draw(im2)
font2 = ImageFont.truetype(
    "hand.otf", size=57)
font1 = ImageFont.truetype("hand.otf", size=67)
print(random.randint(0, 1))
x = 262
y = 215
ch = ';'
font = font1 if(random.randint(0, 1) == 0) else font2
n = round(random.uniform(0.7, 1), 2)
w, h = font.getsize(ch)
d1.text((230, 798), str(ch), fill=(0, 0, 0),
        font=font, spacing=2)
# d1.text((x+1, y+1), str(ch), fill=(0, 0, 0),
#         font=font, spacing=2, stroke_width=0)
x += w*n

im2.save("geeks1.jpg")
im2.show()
