from tkinter import *
import pygame.mixer
app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')
sound_file = "50459_M_RED_Nephlimizer.wav"
mixer = pygame.mixer
mixer.init()

#def track_start():
 #track play(loops = -1)
#def track_stop()
 #track.stop()

def shutdown():
 track.stop()
 app.destroy()

track = mixer.Sound(sound_file)

#start_button = Button(app, command = track_start, text = "Start")
#start_button.pack(side = LEFT)
#stop_button = Button(app, command = track_stop, text = "Stop")
#stop_button.pack(side = RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()
track_playing = IntVar()
track_button = Checkbutton(app, variable = track_playing,
                                            command = track_toggle,
                                            text = sound_file)
track_button.pack()

app.mainloop()