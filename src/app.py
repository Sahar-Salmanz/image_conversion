from io import BytesIO

import streamlit as st
from PIL import Image
from src.utils import convert_image_type, resize_image


def main():
    """
    Main function to run the Streamlit app for image processing.
    """
    st.title(':zap: Image Processing App')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is None:
        st.warning("Please upload an image file.")
        return
    
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image')
    process_type = st.radio("Select the process type:", ["Resize", "Convert Type"])

    # Process the image based on the selected type
    if process_type == "Resize":
        keep_aspect_ratio = st.checkbox("Keep Aspect Ratio", value=True)
        col1, col2 = st.columns(2)

        if keep_aspect_ratio:
            width = col1.number_input("Width", value=image.width)
            aspect_ration = image.width / image.height
            height = int(width / aspect_ration)
            height = col2.number_input("Height", value=height, disabled=True)
        else:
            width = col1.number_input("Width", value=image.width)
            height = col2.number_input("Height", value=image.height)

        if st.button("Resize Image"):
            resized_image = resize_image(image, width, height, keep_aspect_ratio)
            st.image(resized_image, caption='Resized Image')
            result_buffer = BytesIO()
            resized_image.save(result_buffer, format="PNG")
            #result_buffer.seek(0)
            st.download_button(
                label="Download Resized Image",
                data=result_buffer.getvalue(),
                file_name="resized_image.png",
                mime="image/png"
            )

    # Convert image type
    elif process_type == "Convert Type":
        output_format = st.selectbox("Select Output Format", ["JPEG", "PNG"])
        if st.button("Convert Image Type"):
            try:
                converted_image_buffer = convert_image_type(image, output_format)
                st.image(Image.open(converted_image_buffer), caption='Converted Image')
                st.download_button(
                    label="Download Converted Image",
                    data=converted_image_buffer.getvalue(),
                    file_name=f"converted_image.{output_format.lower()}",
                    mime=f"image/{output_format.lower()}"
                )
            except ValueError as e:
                st.error(str(e))



if __name__ == "__main__":
    main()