import streamlit as st
from PIL import Image
import pytesseract

def main():
    st.title("OCR App")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Upload Image", "Capture Image"])

    if page == "Upload Image":
        upload_page()
    elif page == "Capture Image":
        capture_page()

def upload_page():
    st.header("Upload an Image")
    
    # Text Input
    # st.subheader("Enter Text")
    # user_text = st.text_input("Type something here:")
    # if user_text:
    #     st.write("You typed:", user_text)
    
    # Image Upload
    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
    
    # Display the uploaded image and extract text
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        text = pytesseract.image_to_string(image)
        st.header("Text from Image: ")
        st.write(text)

def capture_page():
    st.header("Capture an Image with Camera")
    
    # Text Input
    # st.subheader("Enter Text")
    # user_text = st.text_input("Type something here:")
    # if user_text:
    #     st.write("You typed:", user_text)
    
    # Display camera input option and extract text
    camera_image = st.camera_input("Take a picture")
    
    if camera_image is not None:
        image = Image.open(camera_image)
        st.image(image, caption="Captured Image", use_column_width=True)
        text = pytesseract.image_to_string(image)
        st.header("Text from Image: ")
        st.write(text)

if __name__ == "__main__":
    main()

