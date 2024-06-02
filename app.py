import streamlit as st
from PIL import Image
import pytesseract
import requests
import os
os.environ['TESSERACT_CMD'] = '/usr/bin/tesseract'

# Function to get a response from Hugging Face's inference API
def query_huggingface_api(text):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
    headers = {"Authorization": "Bearer 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"}
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 500,
            "num_return_sequences": 1,
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def main():
    st.markdown("<h1 style='color: lightblue;'>OCR With LLM Support</h1>", unsafe_allow_html=True)
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Upload Image", "Capture Image", "Write Text"])

    if page == "Upload Image":
        upload_page()
    elif page == "Capture Image":
        capture_page()
    elif page == "Write Text":
        write_text_page()

def upload_page():
    st.header("Upload an Image")
    
    # Image Upload
    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
    
    # Display the uploaded image and extract text
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        text = pytesseract.image_to_string(image)

        st.subheader("Extracted Text from Image:")
        st.write(text)
        
        # Query the Hugging Face API with the extracted text
        if st.button("Send to API"):
            response = query_huggingface_api(text)
            st.subheader("Response from Mistral: ")
            st.write(response[0]["generated_text"])

def capture_page():
    st.header("Capture an Image with Camera")
    
    # Display camera input option and extract text
    camera_image = st.camera_input("Take a picture")
    
    if camera_image is not None:
        image = Image.open(camera_image)
        st.image(image, caption="Captured Image", use_column_width=True)
        text = pytesseract.image_to_string(image)
        st.subheader("Extracted Text from Image:")
        st.write(text)
        
        # Query the Hugging Face API with the extracted text
        if st.button("Send to API"):
            response = query_huggingface_api(text)
            st.subheader("Response from Mistral: ")
            st.write(response[0]["generated_text"])

def write_text_page():
    st.header("Write Text")
    text_input = st.text_area("Enter text here")

    if st.button("Send to API"):
        response = query_huggingface_api(text_input)
        st.subheader("Response from Mistral: ")
        st.write(response[0]["generated_text"])

if __name__ == "__main__":
    main()
