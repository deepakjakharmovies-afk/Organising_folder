import tkinter
from tkinter import filedialog
import os
import shutil





def get_files(folder):
    files = []
    for item in os.listdir(folder):
        item_path = os.path.join(folder,item)
        if os.path.isfile(item_path):
            files.append(item_path)
    return files
    
    
    
def exetention_data():
     return {
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"],
        "Video": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
        "Image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Document": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
        "Archive": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
        "Executable": [".exe", ".msi", ".bat", ".sh"],
        "Others": []
    }
def move_file(source_path,destination_path):
    shutil.move(source_path,destination_path)
def get_extension_type(extension):
    ext_data = exetention_data()
    extension = os.path.splitext(extension)[1].lower()
    for catagory,extensions in ext_data.items():
        if extension in extensions:
            return catagory
    return "Others"
def organise(folder):
    for item in exetention_data().keys():
        if not os.path.exists(os.path.join(folder,item)):
            os.mkdir(os.path.join(folder,item))
    files = get_files(folder)
    for file in files:
        extention = get_extension_type(file)
        source_path = file
        destination = os.path.join(folder,extention)
        destination_path = os.path.join(destination,os.path.basename(file))
        move_file(source_path,destination_path)
    tk.destroy()
def ceate_ui():

    tk = tkinter.Tk()
    tk.geometry("600x400")
    tk.title("File Organiser")
    tk.bg = "#2C3E50"
    tk.config(bg=tk.bg)
    lable1 = tkinter.Label(tk, text="Welcome to File Organiser ")
    lable1.config(fg="white", bg=tk.bg, font=("Arial", 32))
    lable1.grid(row=0, column=0, padx=20, pady=20 )
    lable2 = tkinter.Label(tk, text="Select the folder you want to organise")
    lable2.config(fg="white", bg=tk.bg, font=("Arial", 16))
    lable2.grid(row=1, column=0, padx=20, pady=20)
    entry1 = tkinter.Entry(tk, width=40,font=("Arial", 18))
    entry1.grid(row=2, column=0, padx=30, pady=20)
    stringvar1 = tkinter.StringVar()
    entry1.config(textvariable=stringvar1)

    button1 = tkinter.Button(tk, text="Browse", command=lambda:  stringvar1.set(filedialog.askdirectory()))
    button1.config(fg="white",bg="#2980B9", font=("Arial", 16))
    button1.grid(row=3, column=0, padx=20, pady=20)
    button2 = tkinter.Button(tk, text="Organise", command=lambda: organise(stringvar1.get()))  
    button2.config(fg="white",bg="#27AE60", font=("Arial", 16))
    button2.grid(row=4, column=0, padx=20, pady=20)
    tk.mainloop()
if __name__== "__main__":
    ceate_ui()
    

    