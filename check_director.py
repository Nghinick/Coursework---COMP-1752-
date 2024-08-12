import tkinter as tk  
import tkinter.scrolledtext as tkst  
from PIL import ImageTk, Image  
import font_manager as fonts  
import video_library as lib  

def set_text(text_area, content):    
    text_area.delete("1.0", tk.END)  
    text_area.insert(1.0, content)   

class CheckVideos():
    def __init__(self, window):         
        window.geometry("900x500")     
        window.title("Check Director")    
        window.configure(bg="pink")

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Video Number or Director Name:")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        self.input_txt = tk.Entry(window, width=20)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_director_btn = tk.Button(window, text="Check Director", command=self.check_director)
        check_director_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=50, height=10)
        self.list_txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.image_label = tk.Label(window, bg="pink")  
        self.image_label.grid(row=1, column=2, columnspan=6, padx=5, pady=5)  

        self.image_lib = {
            "01": "d01.jpg", "02": "d02.jpg", "03": "d03.jpg", "04": "d04.jpg", "05": "d05.jpg",
            
            "Fred Quimby": "d01.jpg", "Blake Edwards": "d02.jpg", "Michael Curtiz": "d03.jpg",
            "Robert Wise": "d04.jpg", "Victor Fleming": "d05.jpg", 
        }
    def check_director(self):
        input_value = self.input_txt.get()
        if input_value.isdigit():
            director = lib.get_director(input_value)
            if director:
                set_text(self.list_txt, f"Video {input_value} is directed by {director}.")
            else:
                set_text(self.list_txt, "No director found for this video number.")
        else:
            results = lib.search_videos(input_value, search_by='director')
            if results:
                output = "\n".join(f"{item.name} directed by {item.director}" for key, item in results)
                set_text(self.list_txt, output)
            else:
                set_text(self.list_txt, "No videos found by this director")
        image_path = self.image_lib.get(input_value)  
        if image_path:  
            try:  
                image = Image.open(image_path)  
                image = image.resize((200, 200))  
                photo = ImageTk.PhotoImage(image)  
                self.image_label.configure(image=photo)  
                self.image_label.image = photo  
            except Exception as e:  
                print(
                    f"Error loading image: {e}")  
        else:  
            print(
                "Image not found for this video.")  
    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CheckVideos(window)
    window.mainloop()
