import tkinter as tk  

import font_manager as fonts  
from check_videos import CheckVideos  
from update_videos import UpdateVideos 
from create_video_list import CreateVideoList  


def check_videos_clicked():  
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))  
def update_videos_clicked():
    status_lbl.configure(text="Update Videos button was clicked!")
    UpdateVideos(tk.Toplevel(window))   

def add_to_playlist():
    status_lbl.configure(text="Create Video List button was clicked!")
    CreateVideoList(tk.Toplevel(window))  

window = tk.Tk()  
window.geometry("540x150")
window.title("Video Player")
window.configure(bg="pink")

fonts.configure()  
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")  
header_lbl.grid(row=0, column=0, columnspan=3, padx=15, pady=15) 
header_lbl.configure(bg="pink") 

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked) 
check_videos_btn.grid(row=1, column=0, padx=15, pady=15) 

create_video_list_btn = tk.Button(window, text="Create Video List", command=add_to_playlist) 
create_video_list_btn.grid(row=1, column=1, padx=15, pady=15) 

update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked) 
update_videos_btn.grid(row=1, column=2, padx=15, pady=15) 

status_lbl = tk.Label(window, text="", font=("Arial", 20), bg="pink") 
status_lbl.grid(row=2, column=0, columnspan=3, padx=15, pady=15) 

window.mainloop()  

