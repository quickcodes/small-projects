import moviepy.editor
from tkinter.filedialog import *
video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio

audio.write_audiofile("What_To_Say_.mp3")
print("Completed!")
