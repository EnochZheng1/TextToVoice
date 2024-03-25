import tkinter as tk
from tkinter import filedialog
import pyttsx3
import os

# Initialize the speech engine
engine = pyttsx3.init()

# Get list of voices
voices = engine.getProperty('voices')

# Set default voice, rate, and volume
default_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
default_rate = 150
default_volume = 1.0

engine.setProperty('voice', default_voice_id)
engine.setProperty('rate', default_rate)
engine.setProperty('volume', default_volume)

def open_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    with open(file_path, 'r') as file:
        text_entry.delete(0, tk.END)  # Clear the text_entry field
        text_entry.insert(tk.END, file.read())  # Insert the content of the file

def save_audio(default_name=True):
    text = text_entry.get()
    rate = int(rate_entry.get())
    volume = float(volume_entry.get())
    selected_voice = voice_var.get()

    # Find and set the selected voice
    for voice in voices:
        if voice.name == selected_voice:
            engine.setProperty('voice', voice.id)
            break

    # Set properties
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    
    # Save speech audio into a file
    file_name = 'output.mp3' if default_name else filedialog.asksaveasfilename(defaultextension='.mp3')
    engine.save_to_file(text, file_name)
    engine.runAndWait()

root = tk.Tk()

# GUI elements
text_label = tk.Label(root, text="Enter Text or open a .txt file:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

open_file_button = tk.Button(root, text="Open .txt file", command=open_text_file)
open_file_button.pack()

rate_label = tk.Label(root, text="Enter Rate (default is 150):")
rate_label.pack()

rate_entry = tk.Entry(root)
rate_entry.insert(0, str(default_rate))  # Insert default value
rate_entry.pack()

volume_label = tk.Label(root, text="Enter Volume (default is 1.0):")
volume_label.pack()

volume_entry = tk.Entry(root)
volume_entry.insert(0, str(default_volume))  # Insert default value
volume_entry.pack()

voice_label = tk.Label(root, text="Select Voice (default is Microsoft Zira):")
voice_label.pack()

voice_var = tk.StringVar(root)
voice_var.set([voice.name for voice in voices if voice.id == default_voice_id][0])  # Set default voice

# Dropdown menu with voice options
voice_dropdown = tk.OptionMenu(root, voice_var, *[voice.name for voice in voices])
voice_dropdown.pack()

convert_button = tk.Button(root, text="Convert and Save as 'output.mp3'", command=lambda: save_audio(True))
convert_button.pack()

convert_as_button = tk.Button(root, text="Convert and Save as...", command=lambda: save_audio(False))
convert_as_button.pack()

root.mainloop()



