import tkinter as tk  # Import the Tkinter module for GUI creation
import tkinter.scrolledtext as tkst  # Import scrolled text widget for text areas with scrollbars
from tkinter import messagebox  # Import messagebox for error dialogs

from PIL import ImageTk, Image  # Import PIL for image processing and display
import font_manager as fonts  # Import custom font manager for configuring fonts
import video_library as lib  # Import custom video library for video data handling


def set_text(text_area, content):    # Create a section for updating Tkinter `Text` widgets with new content.
    text_area.delete("1.0", tk.END)  # Removes any existing text.
    text_area.insert(1.0, content)   # Inserts the updated content.


class CheckVideos():
    def __init__(self, window):         # Initializing and configuring the GUI window and its widgets.
        window.geometry("1080x720")     # Configuring the initial size and layout of the main GUI window.
        window.title("Check Videos")    # Setting the title text that displays in the title bar of the main GUI window.
        window.configure(bg="pink")     # Set the background color of the main window.

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)  # Creating a button widget and setting it up to call a method when clicked.
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) # configuring the geometry of the "List All Videos" button widget using the grid layout manager

        enter_lbl = tk.Label(window, text="Enter Video Number: 01-05") # Creating and setting up a `Label` widget to display text in the GUI.
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) # Setting up the layout of the label widget using the grid manager.
        self.input_txt = tk.Entry(window, width=5) # Creating and setting up an `Entry` widget to enable user input in the GUI.
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) # Setting up the layout of the `Entry` widget using the grid manager.

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked) # Creating an additional `Button` widget to invoke a method when clicked.
        check_video_btn.grid(row=0, column=3, padx=10, pady=10) # Placing the "Check Video" button within the grid layout.

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") # Creating a scrolled text widget to display output within the GUI.
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) # Setting up the layout of the scrolled text widget using the grid manager.

        self.video_txt = tk.Text(window, width=40, height=10, wrap="none") # Creating a `Text` widget to show video details.
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) # Configuring the grid layout for the `video_txt` widget.

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # creating a Label widget to display status messages
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) # Setting up the grid layout for the status label widget.

        self.image_label = tk.Label(window, bg="pink")  # Create a `Label` widget to display images within the Tkinter window or frame.
        self.image_label.grid(row=2, column=3, padx=10, pady=10) # Place the `image_label` widget in the specified row and column using the grid manager.


        self.list_videos_clicked()                                        # Defining a method for the class without providing its functionality.
        self.image_lib = {
            "01": "image01.jpg", "02": "image02.jpg", "03": "image03.jpg", "04": "image04.jpg", "05": "image05.jpg",
            
        }

    def check_video_clicked(self):  # This method is activated when the 'Check Video' button is pressed.
        key = self.input_txt.get()   # The variable 'key' captures and holds the value inputted in the 'input_txt' Entry widget.
        name = lib.get_name(key)    # Get the name of the video using the specified key.
        director = lib.get_director(key) # Obtain the director of the video using the given key.
        rating = lib.get_rating(key)    # Retrieve the rating of the video using the provided key.
        play_count = lib.get_play_count(key)    # Obtain the play count of the video based on the given key.
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}" # Combine the video details into one string, including the name, director, rating, and play
                                                                                     # count.
        set_text(self.video_txt, video_details) # Display video details in the text widget
        if not key or not key.isdigit() or not (1 <= int(key) <= 10):  # If any of these conditions are met, the error handling mechanism is activated.
            messagebox.showerror("Error", "Invalid video number. Please enter a number between 01-05.")  # This line displays an error message box to inform the user that the
                                                                                                         # provided video number is invalid and must be between 01 and 10.
            return  # This 'return' statement terminates the method if invalid input is detected, stopping any additional code from running.

        name = lib.get_name(key)
        image_path = self.image_lib.get(key) # Retrieve the image file path corresponding to the video key from the image library
        if image_path: # Check if the image path exists
            try:  # code that may raise an exception
                image = Image.open(image_path)  # Open the image file
                image = image.resize((400, 400))  # Resize image to fit the display area
                photo = ImageTk.PhotoImage(image)  # Convert image to Tkinter-compatible format
                self.image_label.configure(image=photo)  # Update the image label widget
                self.image_label.image = photo  # Keep a reference to the image
            except Exception as e:  # handle the exception
                print(f"Error loading image: {e}")  # print an error message if the image cannot be loaded
        else:  # Check if no the image path exists
            print("Image not found for this video.")  # print a message if the image path is not found



    def list_videos_clicked(self):  # defining a method called list_videos_clicked on the class
        video_list = lib.list_all() # retrieve the list of all videos
        set_text(self.list_txt, video_list) # Display the list of videos in the scrolled text widget
        self.status_lbl.configure(text="List Videos button was clicked!")  # update status label


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create the main Tkinter window
    fonts.configure()       # configure fonts using the custom font manager
    CheckVideos(window)     # initialize the CheckVideos class with the main window
    window.mainloop()       # start the Tkinter event loop

    
