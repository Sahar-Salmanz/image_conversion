from io import BytesIO

import PIL


def resize_image(image: "PIL.Image.Image", width: int, height: int, keep_aspect_ration: bool) -> "PIL.Image.Image":
    """
    Resize the image to the specified width and height, optionally keeping the aspect ratio.

    :param image: The image to be resized.
    :param width: The desired width of the resized image.
    :param height: The desired height of the resized image.
    :param keep_aspect_ration: Whether to maintain the original aspect ratio.
    :return: The resized image.
    """
    if keep_aspect_ration:
        image.thumbnail((width, height))
    else:
        image = image.resize((width, height))
    return image


def convert_image_type(image: "PIL.Image.Image", output_format: str) -> BytesIO:
    """
    Converts the image to the specified output format and returns it as a BytesIO object.

    :param image: The image to be converted.
    :param output_format: The desired output format (e.g., "JPEG", "PNG").
    :raises ValueError: If the output format is not supported.
    :return: The converted image as a BytesIO object.
    """
    if output_format.lower() == "jpeg":
        output_format = "JPEG"
    elif output_format.lower() == "png":
        output_format = "PNG"
    else:
        raise ValueError("Unsupported output format: {}".format(output_format))
    output_buffer = BytesIO()
    image.save(output_buffer, format=output_format)
    #output_buffer.seek(0)
    return output_buffer