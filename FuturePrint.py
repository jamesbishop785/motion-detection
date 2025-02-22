# Importing libaries.
import cv2
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
import datetime
import logging

# Function for front enterance camera.
def Front_CCTV():
    front = cv2.VideoCapture(0)
    
# Code to prompt the user that the camera has failed to open using ret.  
    while True:
        ret, frame = front.read()
        if not ret:
            print("Failed to open the Front Enterance CCTV camera :(")
            break

# Put the date and time Text on the live CCTV footage, changed position, font, font-size, colour, and font thickness
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, time, (10, 60), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)
        
# Display the Camera Frame.
        cv2.imshow('FuturePrint Front Enterance Camera', frame)
        
# Allow the user to close the camera to pick a different one by pressing 'q'.
        if cv2.waitKey(1) == ord('q'):
            break
        
# Releasing front camera window for other proccesses and destroying OpenCV windows.
    front.release()
    cv2.destroyAllWindows()

# Function for Warehouse Camera.
def Warehouse_CCTV():
    warehouse = cv2.VideoCapture(1)
    ret, frame1 = warehouse.read()
    ret, frame2 = warehouse.read()
    
# Default for video writer and recording    
    video_writer = None
    recording = False
    last_motion = datetime.datetime.now()
    
# Logging
    logging.basicConfig(
        filename="warehouse_motion_log.txt",  # Log file path
        level=logging.INFO,                    # Telling logging libary that it is a log
        format="%(message)s",    # Log format to display message
    )

    while warehouse.isOpened():
# Calculate difference between frames.
        diff = cv2.absdiff(frame1, frame2)

# Convert to grayscale for processing.
        grayscale = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise.
        blur = cv2.GaussianBlur(grayscale, (5,5), 0)

# Apply threshold to highlight motion.
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

# Dilate image to make motion areas more visible.
        dilated = cv2.dilate(thresh, None, iterations=3)

# Find contours of motion detected.
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Default motion status.
        motion_detected = False

# Draw Rectangles for detected motion.
        for contour in contours:
            if cv2.contourArea(contour) < 10000:  # Ignore small movements below 10,000 pixels.
                continue

            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            motion_detected = True  # Motion detected

# Overlay "Motion Detected" text if motion is detected.
        if motion_detected:
            cv2.putText(frame1, "Detected: Motion", (10, 1070), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

# Log motion detection
            time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            logging.info(f"Motion detected in the Warehouse at {time}")

# Start recording if not already recording
            if not recording:
                filename = f"Warehouse_Motion_{time}.mp4"
                
# Compressing video using fourCC
                fourcc = cv2.VideoWriter_fourcc(*'avc1') # H.264 compression for mp4 format
                video_writer = cv2.VideoWriter(filename, fourcc, 20.0, (frame1.shape[1], frame1.shape[0]))
                recording = True
                
        else:
            # Check if 10 seconds have passed since last motion
            if recording and (datetime.datetime.now() - last_motion).total_seconds() > 10:
                video_writer.release()
                video_writer = None
                recording = False
                
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame1, time, (10, 60), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)
        
# Write frame if recording is active
        if recording and video_writer is not None:
            video_writer.write(frame1)

# Display Video Feed
        cv2.imshow("FuturePrint Warehouse", frame1)

# Update Frames
        frame1 = frame2
        ret, frame2 = warehouse.read()

# Allow the user to close the camera by pressing 'q'
        if cv2.waitKey(1) == ord('q'):
            break

# Release video writer if it was used.
    if recording and video_writer is not None:
        video_writer.release()

# Release camera and close OpenCV windows
    warehouse.release()
    cv2.destroyAllWindows()
    
def Surveillance():
    front = cv2.VideoCapture(0)
    warehouse = cv2.VideoCapture(1)

# If cameras cannot connect display error message    
    while True:
        ret, frame = front.read()
        ret1, frame1 = warehouse.read()
        
        if not ret or not ret1:
            print("Failed to open one of the CCTV cameras :(")
            break
        
# Overlay the date and time on both camera windows.
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, time, (10, 60), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)
        cv2.putText(frame1, time, (10, 60), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 4)
        
# Display Cameras.        
        cv2.imshow('Front Enterance Camera', frame)
        cv2.imshow('Warehouse Camera', frame1)

# Allow the user to close the camera to pick a different one by pressing 'q'.        
        if cv2.waitKey(1) == ord('q'):
            break

# Release frames and OpenCV windows.        
    front.release()
    warehouse.release()
    cv2.destroyAllWindows()

def CCTV_GUI():
# Main UI Window of Camera Choice Programme.
    root = Tk()
    root.title("FuturePrint CCTV Dashboard") # Window Title.
    root.geometry("1451x761")    # Window Size to fit image

# Adding a title to the GUI prompting the user to choose a camera.
    title_label = Label(
    root, 
    text="Welcome to FuturePrint CCTV Dashboard! Please Choose a Camera", # Title Text.
    font=("Arial", 24, "bold"),  # Font and font size of title.
    fg="white"                   # Text color for the title.
    )
    title_label.pack(pady=20)  # Padding to separate the camera choice title from the buttons.

# Converting Image into red, green, blue and alpha (transparency).
    image = Image.open("FuturePrint_Outside.jpeg").convert("RGBA")
    
# Uses the alpha channel (3) to set the absolute pixel value to 55 out of 255 to make image more transparent 
    image.putalpha(image.split()[3].point(lambda p: 55))
    
# Converts PIL into format TK can use for GUI
    photo = ImageTk.PhotoImage(image)

# Create a label widget to display the image
    label = Label(root, image=photo)
    
# Display the label widget
    label.pack()

    button_style = {
    "font": ("Arial", 16),      # Font and font size of text in button.
    "width": 40,                # Width size of button.
    "height": 4,                # Height size of button.
    "bg": "lightblue",          # Colour of button background.
    "fg": "black",              # Colour of button text.
    }

# Buttons for CCTV GUI
    Button(root, text="Front Enterance Camera", command=Front_CCTV, **button_style).place(x=200, y=450)
    Button(root, text="Warehouse Camera", command=Warehouse_CCTV, **button_style).place(x=870, y=450)
    Button(root, text="Surveillance", command=Surveillance, **button_style).place(x=540, y=550)

    root.mainloop()
    
CCTV_GUI()
