import sys
from PIL import Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def convert_to_grayscale(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        if pixel_value == 255:
            ascii_str += " "
        else:
            ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def main(image_path):
    try:
        image = Image.open(image_path)
        image = scale_image(image)
        image = convert_to_grayscale(image)
        ascii_str = map_pixels_to_ascii(image)
        for i in range(0, len(ascii_str), image.width):
            print(ascii_str[i:i+image.width])

    except Exception as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_to_ascii.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)
