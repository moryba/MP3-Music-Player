import pygame #used to create video games
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #askdirectory present user with pop up window to choose directory
import os #permit to interact with the operating system


music_player = tkr.Tk()  #it creates the interface
music_player.title("Life In Music") #title of the interface
music_player.geometry("450x350") # set the dimension of the interface

directory = askdirectory()
os.chdir(directory) #permit to change the current working direcory
song_list = os.listdir() #it returns the list containing the names of the entries in the directory given the path
#below we create the variable play_list. it diplays the list items to the user.we can specify the color and the type of file to select
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)

for item in song_list: #select each item from the song_list and insert them into the list box
    pos = 0
    play_list.insert(pos, item)
    pos += 1


#now we have to initialize paygame.mixer is used for loading and playing sounds.
pygame.init() # initailize pygame
pygame.mixer.init() # initialize the pygame.mixer

#now it is time to create the functions to control the bottom

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE)) #it is responsible for controlling streamed audio and also loads a music file for playback. ACTIVE is the state of the file when you move you mouse on it
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="blue", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="red", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="purple", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="orange", fg="white")

var = tkr.StringVar() #monitor changes to tikenter module
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")
music_player.mainloop()
