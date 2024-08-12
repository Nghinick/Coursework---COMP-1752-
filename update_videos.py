import tkinter as tk  
import tkinter.scrolledtext as tkst  
from tkinter import messagebox  

import video_library as lib  
import font_manager as fonts  


class UpdateVideos:
    def __init__(self, window):
        self.window = window
        self.window.geometry("720x720")  
        self.window.title("Update Videos")  
        self.window.configure(bg="pink")  

        self.create_widgets()  

    def create_widgets(self):  
        enter_lbl = tk.Label(self.window, text="Enter Video Number", bg="pink")   
        enter_lbl.grid(row=0, column=0, padx=5, pady=5)  

        self.input_txt = tk.Entry(self.window, width=20)   
        self.input_txt.grid(row=0, column=1, padx=20, pady=30)  

        enter_lbl = tk.Label(self.window, text="Rating", bg="pink")  
        enter_lbl.grid(row=3, column=0, padx=10, pady=10)  

        self.input_rating = tk.Entry(self.window, width=20)  
        self.input_rating.grid(row=3, column=1, padx=10, pady=10)  

        update_video_btn = tk.Button(self.window, text="Update Video", command=self.update_video_clicked,
                                     bg="white", fg="black")  
        update_video_btn.grid(row=4, column=1, padx=10, pady=10)  

        reset_btn = tk.Button(self.window, text="Reset", command=self.reset_videos_clicked,
                              bg="white", fg="black")  
        reset_btn.grid(row=4, column=0, padx=10, pady=10)  

        self.video_txt = tk.Text(self.window, width=40, height=10, wrap="none")  
        self.video_txt.grid(row=5, column=0, columnspan=2, padx=10, pady=10)  

        self.status_lbl = tk.Label(self.window, text="", font=("Arial", 10))  
        self.status_lbl.grid(row=6, column=0, columnspan=2, sticky="W", padx=10, pady=10) 

        self.list_txt = tkst.ScrolledText(self.window, width=60, height=12)  
        self.list_txt.grid(row=7, column=0, columnspan=2, sticky="W", padx=10, pady=10) 

        self.list_videos_clicked()  

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
            messagebox.showerror("Error", "Invalid Rating!!! \n Please rating from 1 to 5")  
            return  
        success = lib.set_rating(key, change)
        if success:
            self.status_lbl.configure(text="Video rating updated successfully!", fg="green")
        else:
            self.status_lbl.configure(text=f"Video rating updated successfully!", fg="green")

        if name is not None:  
            director = lib.get_director(key)  
            play_count = lib.get_play_count(key)  
            new_set = lib.set_rating(key, change)  
            new_rate = lib.get_rating(key)  
            video_details = f"{name}\nDirector: {director}\nRating: {new_rate}"  
            self.set_text(self.video_txt, video_details)  
            self.list_videos_clicked()  
            self.status_lbl.configure(text="Update Video button was clicked!")  
        else:  
            self.set_text(self.video_txt, f"Video with key {key} not found")   
            self.status_lbl.configure(text=f"Video with key {key} not found!", bg="red")  

    def list_videos_clicked(self):
        video_list = lib.list_all()   
        self.set_text(self.list_txt, video_list)  
        self.status_lbl.configure(text="List Videos button was clicked!", bg="pink")  

    def reset_videos_clicked(self):
        self.input_txt.delete(0, tk.END)  
        self.input_rating.delete(0, tk.END)  
        self.status_lbl.configure(text="Reset Videos button was clicked!", bg="grey")  
    def set_text(self, text_area, content):  
        text_area.delete("1.0", tk.END)  
        text_area.insert(tk.END, content)  


if __name__ == "__main__":  
    window = tk.Tk()        
    fonts.configure()       
    UpdateVideos(window)     
    window.mainloop()       
