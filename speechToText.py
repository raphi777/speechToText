import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():
    filename = fileDialog()

    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)

    label1 = tk.Label(root, text= text, fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

def fileDialog ():
    filename = filedialog.askopenfilename(initialdir =  ".", title = "Select A File", filetype =
            (("wav files","*.wav"),("all files","*.*")) )
    return filename

button1 = tk.Button(text='Choose File',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
