from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
im2 = Image.open('2721426.jpg')
d1 = ImageDraw.Draw(im2)
font2 = ImageFont.truetype(
    "hand2.ttf", size=57)
font1 = ImageFont.truetype("hand1.ttf", size=67)
print(random.randint(0, 1))
g = open("demofile3.txt", "r")
x = 230
y = 215

for index, si in enumerate(g):
    hello = si.strip()
    for i, ch in enumerate(hello):
        if(ch.isalpha == True or ch == '-'):
            font = font1 if(random.randint(0, 1) == 0) else font2
        else:
            font = font1
        if(ch == '*'):
            font = ImageFont.truetype('arial.ttf', size=55)
        n = round(random.uniform(0.7, 1), 2)
        w, h = font.getsize(ch)
        if(x < 1134):
            print(ch, end="")
            d1.text((x, y), str(ch), fill=(0, 0, 0),
                    font=font, spacing=2)
        else:
            try:
                if(ch == ' ' or hello[i+1] == ' '):
                    y += 53
                    x = 262 + random.randint(0, 15)
                    print(ch, end="\n")
                    d1.text((x, y), str(ch), fill=(0, 0, 0),
                            font=font, spacing=2)
                else:
                    print('-', end="\n")
                    d1.text((x, y), '-', fill=(0, 0, 0),
                            font=font, spacing=2)
                    y += 53
                    x = 262 + random.randint(0, 15)
                    print(hello[i], end="")
                    d1.text((x, y), str(ch), fill=(0, 0, 0),
                            font=font, spacing=2)
            except:
                if(ch == ' '):
                    y += 53
                    x = 262 + random.randint(0, 15)
                    print(ch, end="\n")
                    d1.text((x, y), str(ch), fill=(0, 0, 0),
                            font=font, spacing=2)
                else:
                    print('-', end="\n")
                    d1.text((x, y), '-', fill=(0, 0, 0),
                            font=font, spacing=2)
                    y += 53
                    x = 262 + random.randint(0, 15)
                    print(hello[i], end="")
                    d1.text((x, y), str(ch), fill=(0, 0, 0),
                            font=font, spacing=2)
            # d1.text((x+1, y+1), str(ch), fill=(0, 0, 0),
            #         font=font, spacing=2, stroke_width=0)
        x += w*n
        # min 0.7 max 1.2
    print("\n")
    y += 53
    yl = random.randint(0, 15)
    x = 222+yl
# im2 = im2.filter(ImageFilter.DETAIL())
im2.save("geeks.jpg")
im2.show()
