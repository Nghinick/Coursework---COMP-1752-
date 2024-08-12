import tkinter as tk  
import tkinter.scrolledtext as tkst  
from tkinter import messagebox  
from video_library import library  
import font_manager as fonts  

class CreateVideoList:  
    def __init__(self, window):  
        self.window = window  
        self.window.geometry("1000x600")  
        self.window.title("Create Video List")  
        self.window.configure(bg="pink")
        self.playlist = []  
        self.played_videos = []  
        self.create_widgets()  

    def create_widgets(self):  
        header_lbl = tk.Label(self.window, text="Create Video Playlist", bg="pink")  
        header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10) 

        self.video_entry_label = tk.Label(self.window, text="Enter Video Number (01-05):")  
        self.video_entry_label.grid(row=1, column=0, padx=10, pady=5) 
        self.video_entry = tk.Entry(self.window)  
        self.video_entry.grid(row=1, column=1, padx=10, pady=5) 

        self.add_to_playlist_btn = tk.Button(self.window, text="Add to Playlist", command=self.add_to_playlist)  
        self.add_to_playlist_btn.grid(row=1, column=2, padx=10, pady=5)  

        self.playlist_text = tkst.ScrolledText(self.window, width=80, height=10)  
        self.playlist_text.grid(row=2, column=0, columnspan=4, padx=20, pady=10) 

        self.play_playlist_btn = tk.Button(self.window, text="Play Playlist", command=self.play_playlist)  
        self.play_playlist_btn.grid(row=1, column=3, padx=10, pady=5)  

        self.reset_playlist_btn = tk.Button(self.window, text="Reset Playlist", command=self.reset_playlist)  
        self.reset_playlist_btn.grid(row=1, column=4, padx=10, pady=5)  

        self.played_videos_text = tkst.ScrolledText(self.window, width=80, height=10)  
        self.played_videos_text.grid(row=3, column=0, columnspan=4, padx=20, pady=10) 
        self.played_videos_text.insert(tk.END, "Played Videos:\n")  

    def add_to_playlist(self):
        video_number = self.video_entry.get()
        if video_number in library:
            video = library[video_number]
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
            if video not in self.played_videos:
                self.played_videos.append(video)  
        self.update_playlist_text()
        self.update_played_videos_text()  

    def update_played_videos_text(self):
        self.played_videos_text.delete(1.0, tk.END)
        self.played_videos_text.insert(tk.END, "Played Videos:\n")
        for video in self.played_videos:
            info = f"{video.name}\n"
            self.played_videos_text.insert(tk.END, info)

    def reset_playlist(self): 
        self.playlist = []  
        self.playlist_text.delete(1.0, tk.END)  

if __name__ == "__main__": 
    window = tk.Tk()  
    fonts.configure()  
    CreateVideoList(window)  
    window.mainloop()
