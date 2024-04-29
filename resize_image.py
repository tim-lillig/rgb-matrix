from io import BytesIO

import requests
from PIL import Image


def resize_image_and_get_pixel_values(image_url, new_size):
    # Download the image from the URL
    response = requests.get(image_url)
    image_data = BytesIO(response.content)

    # Open the image using PIL
    img = Image.open(image_data)

    # Resize the image to the new size
    resized_img = img.resize(new_size)

    # Get pixel values as a list of lists
    pixel_values = []
    for y in range(new_size[1]):
        row = []
        for x in range(new_size[0]):
            pixel = resized_img.getpixel((x, y))
            row.append(pixel)
        pixel_values.append(row)

    return pixel_values

