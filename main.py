from PIL import Image, ImageDraw, ImageFont
import sys, os


def get_image(input_path="input.txt", output_path="output.png", font_size=10):
    font = ImageFont.truetype("COUR.TTF", font_size)
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
        lines = text.splitlines()

    char_width = font.getlength("M")
    ascent, descent = font.getmetrics()
    char_height = ascent + descent
    
    padding_horizontal = char_width // 2
    padding_vertical = char_height // 2
    
    max_width = int(len(lines[0]) * char_width + padding_horizontal * 2)
    max_height = int(len(lines) * char_height + padding_vertical * 2)


    img = Image.new("L", (max_width, max_height), color=255)
    draw = ImageDraw.Draw(img)

    draw.text((padding_horizontal, padding_vertical), text, font=font, fill=0)
    img.save(output_path, optimize=True, compress_level=9)



def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("USAGE: python main.py <input_text_file> ||| OPTIONAL ARGUMENTS: <output_image> <font_size>")
        print("  <output_image> - default is 'output.png'")
        print("  <font_size> - default is 10")
        print("\nExample:")
        print("  python main.py input.txt output.png 12")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.png"
    font_size = int(sys.argv[3]) if len(sys.argv) > 3 else 10

    if not os.path.exists(input_file):
        print(f"Error: input file '{input_file}' not found.")
        sys.exit(1)

    get_image(input_file, output_file, font_size)

if __name__ == "__main__":
    main()