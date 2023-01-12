# Importing necessary packages
import tkinter as tk
import ffmpeg
import os
from tkinter import *
from pytube import YouTube
# make sure pytube is updated!!!!
# python -m pip install --upgrade pytube
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def widgets():
    head_label = Label(root, text="Video Downloader", font="SegueUI 14", bg="black", fg="white")
    head_label.grid(row=1, column=0, pady=10, padx=5, columnspan=3)

    link_label = Label(root, text="Link :", bg="white", pady=5, padx=28)
    link_label.grid(row=2, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    #########################################################################
    title_label = Label(root, text="Title :", bg="white", pady=5, padx=28)
    title_label.grid(row=3, column=0, pady=5, padx=5)

    root.titleText = Entry(root, width=35, textvariable=video_Title, font="Arial 14")
    root.titleText.grid(row=3, column=1, pady=5, padx=5, columnspan=2)
    #########################################################################

    destination_label = Label(root, text="Destination :", bg="white", pady=5, padx=9)
    destination_label.grid(row=4, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
    root.destinationText.grid(row=4, column=1, pady=5, padx=5)

    browse_b = Button(root, text="browse", command=browse, width=10, bg="white", relief=GROOVE)
    browse_b.grid(row=4, column=2, pady=1, padx=1)

    download_b = Button(root, text="Download Video", command=download, width=20, bg="white", pady=10, padx=15,
                        relief=GROOVE, font="Georgia, 13")
    download_b.grid(row=5, column=1, pady=20, padx=20)


# Defining Browse() to select a
# destination folder to save the video

def browse():
    # Presenting user with a pop-up for
    # directory selection. initial-dir
    # argument is optional Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")

    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_directory)


# Defining Download() to download the video


def download():
    # getting user-input Youtube Link
    youtube_link = video_Link.get()
    print("1")

    # select the optimal location for
    # saving file's
    download_folder = download_Path.get()
    print("2")

    # Creating object of YouTube()
    get_video = YouTube(youtube_link)
    print("3")

    # Getting all the available streams of the
    # YouTube video and selecting the first
    # from the
    video_stream = get_video.streams.get_highest_resolution()
    default_video_title = get_video.streams[0].title
    video_title = video_Title.get()
    print(default_video_title)
    print("4")

    #########################################################################
    get_video.streams.filter(progressive=False).order_by('abr').desc().first().download(filename="audio.mp3")
    audio = ffmpeg.input("audio.mp3")

    get_video.streams.filter(progressive=False).order_by('resolution').desc().first().download(filename="video.mp4")
    video = ffmpeg.input("video.mp4")
    print("5")
    if video_title:
        ffmpeg.output(audio, video, filename=download_folder + video_title + ".mp4").run(overwrite_output=True)
    else:
        ffmpeg.output(audio, video, filename=download_folder + default_video_title + ".mp4").run(overwrite_output=True)
    print("6")

    os.remove("video.mp4")
    os.remove("audio.mp3")

    print("7")
    #########################################################################

    # Downloading the video to destination
    # directory
    # if video_title:
    #    video_stream.download(download_folder, filename=video_title + ".mp4")
    # else:
    #    video_stream.download(download_folder)


    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_folder)


# Creating object of tk class
root = tk.Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("520x280")
root.resizable(FALSE, FALSE)
root.title("Video Downloader")
root.config(background="black")

# Creating the tkinter Variables
video_Link = StringVar()
# default path is project folder
download_Path = StringVar()
video_Title = StringVar()

# Calling the Widgets() function
widgets()

# Defining infinite loop to run
# application
root.mainloop()
