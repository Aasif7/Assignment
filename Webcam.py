import streamlit as st
import cv2
from PIL import Image
import pytesseract

# Set up the Streamlit app title and sidebar
st.title("Receipt Details Extractor")
st.sidebar.header("Settings")

# Initialize the webcam using webrtc_streamer
image = st.image([], channels="BGR", use_container_width=True, output_format="JPEG")
webrtc_ctx = st.webrtc_streamer(key="example", video_transformer_class="webcam")

# Function to extract text from image using Tesseract OCR
def extract_text_from_image(img):
    # Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Use Tesseract OCR to extract text
    text = pytesseract.image_to_string(gray_img)
    return text

# Main app loop
while webrtc_ctx.video_receiver:
    # Get the latest frame from the webcam
    frame = webrtc_ctx.video_receiver.get_frame()

    # Display the live image
    image.image(frame, channels="BGR")

    # Check if user clicks the "Capture" button
    if st.sidebar.button("Capture"):
        # Convert the BGR frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to PIL Image
        pil_image = Image.fromarray(rgb_frame)

        # Extract text from the captured image
        extracted_text = extract_text_from_image(rgb_frame)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text(extracted_text)
