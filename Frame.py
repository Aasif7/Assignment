import cv2
import streamlit as st
import numpy as np

def main():
    st.title("Live Video Feed Capture")

    # Open the video capture
    cap = cv2.VideoCapture(0)  # 0 represents the default camera, change it if using an external camera

    # Check if the camera opened successfully
    if not cap.isOpened():
        st.error("Error: Could not open camera.")
        return

    while True:
        # Read a frame from the video feed
        ret, frame = cap.read()

        if not ret:
            st.error("Error: Failed to capture frame.")
            break

        # Display the captured frame
        st.image(frame, channels="BGR", use_column_width=True)

    # Release the video capture object when done
    cap.release()

if __name__ == "__main__":
    main()
    
# modify #
import cv2
import streamlit as st
import numpy as np

def main():
    st.title("Live Video Feed Capture")

    # Open the video capture
    cap = cv2.VideoCapture(0)  # 0 represents the default camera, change it if using an external camera

    # Check if the camera opened successfully
    if not cap.isOpened():
        st.error("Error: Could not open camera.")
        return

    # Create a placeholder for the captured images
    captured_images = st.empty()

    # List to store captured frames
    captured_frames = []

    # Capture button
    if st.button("Capture Image"):
        # Read a frame from the video feed
        ret, frame = cap.read()

        if ret:
            # Store the captured frame
            captured_frames.append(frame.copy())

            # Display the captured frames
            for img in captured_frames:
                captured_images.image(img, channels="BGR", use_column_width=True)
        else:
            st.error("Error: Failed to capture frame.")

    # Release the video capture object when done
    cap.release()

if __name__ == "__main__":
    main()
