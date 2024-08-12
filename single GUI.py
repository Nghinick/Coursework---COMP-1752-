import tkinter as tk
from tkinter import ttk  # Import ttk for Notebook (tabs) widget
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from PIL import ImageTk, Image

import font_manager as fonts
import video_library as lib

class CheckVideos:
    def __init__(self, frame):
        self.frame = frame
        self.frame.configure(bg="pink")

        list_videos_btn = tk.Button(self.frame, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(self.frame, text="Enter Video Number: 01-05")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        self.input_txt = tk.Entry(self.frame, width=5)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(self.frame, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(self.frame, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(self.frame, width=40, height=10, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(self.frame, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.image_label = tk.Label(self.frame, bg="pink")
        self.image_label.grid(row=2, column=3, padx=10, pady=10)

        self.image_lib = {
            "01": "image01.jpg", "02": "image02.jpg", "03": "image03.jpg", "04": "image04.jpg", "05": "image05.jpg",
        }

    def set_text(self, text_area, content):
        text_area.delete("1.0", tk.END)
        text_area.insert(1.0, content)

    def check_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        director = lib.get_director(key)
        rating = lib.get_rating(key)
        play_count = lib.get_play_count(key)
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
        self.set_text(self.video_txt, video_details)
        if not key or not key.isdigit() or not (1 <= int(key) <= 10):
            messagebox.showerror("Error", "Invalid video number. Please enter a number between 01-05.")
            return

        image_path = self.image_lib.get(key)
        if image_path:
            try:
                image = Image.open(image_path)
                image = image.resize((400, 400))
                photo = ImageTk.PhotoImage(image)
                self.image_label.configure(image=photo)
                self.image_label.image = photo
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            print("Image not found for this video.")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        self.set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")


class CreateVideoList:
    def __init__(self, frame):
        self.frame = frame
        self.frame.configure(bg="pink")
        self.playlist = []
        self.played_videos = []  
        self.create_widgets()

    def create_widgets(self):
        header_lbl = tk.Label(self.frame, text="Create Video Playlist", bg="pink")
        header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.video_entry_label = tk.Label(self.frame, text="Enter Video Number (01-05):")
        self.video_entry_label.grid(row=1, column=0, padx=10, pady=5)
        self.video_entry = tk.Entry(self.frame)
        self.video_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_to_playlist_btn = tk.Button(self.frame, text="Add to Playlist", command=self.add_to_playlist)
        self.add_to_playlist_btn.grid(row=1, column=2, padx=10, pady=5)

        self.playlist_text = tkst.ScrolledText(self.frame, width=80, height=15)
        self.playlist_text.grid(row=2, column=0, columnspan=4, padx=20, pady=20)

        self.play_playlist_btn = tk.Button(self.frame, text="Play Playlist", command=self.play_playlist)
        self.play_playlist_btn.grid(row=1, column=3, padx=10, pady=5)

        self.reset_playlist_btn = tk.Button(self.frame, text="Reset Playlist", command=self.reset_playlist)
        self.reset_playlist_btn.grid(row=1, column=4, padx=10, pady=5)
 

    def add_to_playlist(self):
        video_number = self.video_entry.get()
        if video_number in lib.library:
            video = lib.library[video_number]
            if video not in self.playlist:
                self.playlist.append(video)
                self.update_playlist_text()
            else:
                messagebox.showerror("Error", "Video already in Playlist!")
        else:
            messagebox.showerror("Error", "Invalid Video Number!")

    def update_playlist_text(self):
        self.playlist_text.delete(1.0, tk.END)
        for video in self.playlist:
            info = f"{video.name}\n"
            self.playlist_text.insert(tk.END, info)

    def play_playlist(self):
        for video in self.playlist:
            video.increment_play_count()
        self.update_playlist_text()

    def reset_playlist(self):
        self.playlist = []
        self.playlist_text.delete(1.0, tk.END)


class UpdateVideos:
    def __init__(self, frame):
        self.frame = frame
        self.frame.configure(bg="pink")
        self.create_widgets()

    def create_widgets(self):
        enter_lbl = tk.Label(self.frame, text="Enter Video Number", bg="pink")
        enter_lbl.grid(row=0, column=0, padx=5, pady=5)

        self.input_txt = tk.Entry(self.frame, width=20)
        self.input_txt.grid(row=0, column=1, padx=20, pady=30)

        enter_lbl = tk.Label(self.frame, text="Rating", bg="pink")
        enter_lbl.grid(row=3, column=0, padx=10, pady=10)

        self.input_rating = tk.Entry(self.frame, width=20)
        self.input_rating.grid(row=3, column=1, padx=10, pady=10)

        update_video_btn = tk.Button(self.frame, text="Update Video", command=self.update_video_clicked, bg="white", fg="black")
        update_video_btn.grid(row=4, column=1, padx=10, pady=10)

        reset_btn = tk.Button(self.frame, text="Reset", command=self.reset_videos_clicked, bg="white", fg="black")
        reset_btn.grid(row=4, column=0, padx=10, pady=10)

        self.video_txt = tk.Text(self.frame, width=40, height=10, wrap="none")
        self.video_txt.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(self.frame, text="", font=("Arial", 10))
        self.status_lbl.grid(row=6, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(self.frame, width=60, height=12)
        self.list_txt.grid(row=7, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def set_text(self, text_area, content):
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)

    def update_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)

        if not key.isdigit() or not (1 <= int(key) <= 10):
            messagebox.showerror("Error", "Invalid Video Number!!! \n Please enter a number between 01 and 05")
            return

        try:
            change = int(self.input_rating.get())
            if not (1 <= change <= 5):
                raise ValueError("INVALID RATING! \n PLEASE ENTER RATING FROM 1 TO 5")
        except ValueError as e:
            messagebox.showerror("Error", "Invalid Rating!!! \n Please enter a rating from 1 to 5")
            return

        success = lib.set_rating(key, change)
        if success:
            self.status_lbl.configure(text="Video rating updated successfully!", fg="green")
        else:
            self.status_lbl.configure(text=f"Video rating updated successfully!", fg="green")

        self.list_videos_clicked()

    def reset_videos_clicked(self):
        result = messagebox.askyesno("Confirmation", "Are you sure you want to reset all videos?")
        if result:
            lib.reset()
            self.status_lbl.configure(text="Videos have been reset successfully!", fg="red")
            self.set_text(self.list_txt, "Reset successful!\nAll ratings set to 0\nAll play counts set to 0.")
            self.list_videos_clicked()

    def list_videos_clicked(self):
        video_list = lib.list_all()
        self.set_text(self.list_txt, video_list)


class VideoManagerApp:
    def __init__(self, root):
        root.title("Video Manager")
        root.geometry("1000x700")
        notebook = ttk.Notebook(root)

        # Create frames for each tab
        check_videos_frame = tk.Frame(notebook)
        create_video_list_frame = tk.Frame(notebook)
        update_videos_frame = tk.Frame(notebook)

        # Add frames to the notebook (as tabs)
        notebook.add(check_videos_frame, text="Check Videos")
        notebook.add(create_video_list_frame, text="Create Video List")
        notebook.add(update_videos_frame, text="Update Videos")

        # Initialize classes for each tab
        CheckVideos(check_videos_frame)
        CreateVideoList(create_video_list_frame)
        UpdateVideos(update_videos_frame)

        notebook.pack(expand=1, fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoManagerApp(root)
    root.mainloop()
