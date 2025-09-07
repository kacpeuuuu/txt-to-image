from PIL import Image, ImageDraw, ImageFont


font = ImageFont.truetype("COUR.TTF", 10)

print(font.getlength("A"))
print(font.getmetrics())


ascent, descent = font.getmetrics()

text_width = font.getmask("Aedede").getbbox()
text_height = font.getmask("Aedede").getbbox()[3] + descent

print(text_width)

print(text_width, text_height)

