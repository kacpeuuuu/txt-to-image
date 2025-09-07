from PIL import Image, ImageDraw, ImageFont


with open("txt.txt", "r", encoding="utf-8") as f:
    text = f.read()

img = Image.new("RGB", (800,600), color="white")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("COUR.TTF", 20)

draw.text((10,10), text, font=font, fill="black")

img.save("output.png")
