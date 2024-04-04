from pydub import AudioSegment
from tkinter import filedialog, messagebox
from threading import Thread

import customtkinter as ctk

root = ctk.CTk()
root.geometry('500x150')
root.title = 'Audio File Converter'

files_list = []


def get_file():
    global files_list
    # convert many of files if you want
    file_names = filedialog.askopenfilenames()
    for file in file_names:
        files_list.append(file)


def convert_audio_files(src_file, from_, to_):
    to_ = to_.lower()
    funcs_list = {
        'mp3': AudioSegment.from_mp3,
        'wav': AudioSegment.from_wav,
        'ogg': AudioSegment.from_ogg,
    }

    dist_file = src_file.replace(from_, to_)
    # call function from dict
    audio = funcs_list[from_](src_file)
    audio.export(dist_file, format = to_)

    


def convert_files():
    if len(files_list) <= 0:
        messagebox.showinfo('Info', message='Choice files to convert')

    for file_name in files_list:
        extintion = file_name.split('.')[-1]
        to_ = options.get()
        convert_audio_files(file_name, extintion, to_=to_)
        


# add title
ctk.CTkLabel(root, text = root.title, font=('san-serf', 25)).place(x = 20, y = 10)

# add get file bt
bt_1 = ctk.CTkButton(
    root,
    text = 'Choice file',
    command = get_file
)

bt_1.place(x = 20, y = 80)

# add extintions options
options = ctk.CTkOptionMenu(
    root,
    values = ('MP3', 'WAV', 'OGG')
)

options.place(x = 200, y = 80)

# add convert bt
bt_2 = ctk.CTkButton(
    root,
    text = 'Convert',
    width=80,
    command = lambda : convert_files()
)

bt_2.place(x = 350, y = 80)

root.mainloop()