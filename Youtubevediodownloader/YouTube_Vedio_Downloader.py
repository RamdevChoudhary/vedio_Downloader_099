import os
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from pytube import YouTube

Foldername = ""

def openloc():
    global Foldername
    Foldername = filedialog.askdirectory()
    
    if len(Foldername) > 1:
        locationnerror.config(text=Foldername, fg="green")
    else:
        locationnerror.config(text="Choose Directory", fg="red")


def Download_vid():
    url = ytdentry.get()
    
    if len(url) > 1:
        ytderror.config(text="")
        yt = YouTube(url)
        
        filenamee = yt.title

        try:
            get = messagebox.askyesno("Do You Want To Download", f"Video: {filenamee}\n\nDo you want to proceed?")
            
            if get:
                yt.streams.filter(progressive=True, file_extension='mp4').first().download(Foldername)
                ytderror.config(text="Download Completed", fg="green")
            else:
                ytderror.config(text="Download Cancelled", fg="red")
        
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred during the download:\n\n{str(e)}")
    
    else:
        ytderror.config(text="Paste the link again", fg="red")


root = Tk()
root.title("Youtube Video Downloader")
root.geometry("350x400")
root.columnconfigure(0, weight=1)

ytdlabel = Label(root, text="Enter URL:", font=("bahnschrift semilight", 15))
ytdlabel.grid()

ytdentryvar = StringVar()
ytdentry = Entry(root, width=50, textvariable=ytdentryvar)
ytdentry.grid()

ytderror = Label(root, text="Error", fg="red", font=("bahnschrift semilight", 13))
ytderror.grid()

savelabel = Label(root, text="Save the Video", font=("bahnschrift semilight", 15))
savelabel.grid()

saveEntry = Button(root, width=13, bg="red", fg="white", text="Choose Directory:", command=openloc)
saveEntry.grid()

locationnerror = Label(root, text="Directory causes Error", fg="red", font=("bahnschrift semilight", 13))
locationnerror.grid()

downloadbtn = Button(root, width=10, text="Apply", bg="green", fg="lightyellow", font=("bahnschrift semilight", 15), command=Download_vid)
downloadbtn.grid()

root.mainloop()
