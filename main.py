import cv2
import numpy as np
from model import FacialExpressionModel
import random
import os
from glob import  glob
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
top=tk.Tk()
top.geometry("400x250")
top.title("Play_your_song")
top.config(bg="blue")
pred=""


model=FacialExpressionModel("model.json","model_weights.h5")
EMOTIONS_LIST = ["Frustated", "Disgust","Fear", "Happy","Neutral", "Sad","Surprise"]


def fname():
    return lb.get(lb.curselection())


def play():
    os.startfile(fname())

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        fc = gray[y:y + h, x:x + w]
        roi = cv2.resize(fc, (48, 48))
        pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
        cv2.putText(frame, pred, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.putText(frame,'Press Q to quit', (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(255,216, 20), thickness=2)
    cv2.imshow('frame', frame)
    if pred == "Happy":
        x = random.randint(0, 2)
        w1 = Label(top, text=f'we are playing {pred} songs for you', font="50", fg='black',bg='blue')
        w1.pack()
        lb = tk.Listbox(top,bg='blue')
        lb.pack()
        music_dir = 'song\Happy'
        songs = os.listdir(music_dir)
        fl = glob("song\Happy\*.mp3")
        for f in fl:
            lb.insert(0, f)
        print('the songs are',songs)
        os.startfile(os.path.join(music_dir,songs[x]))
        lb.bind("<Double-Button>", lambda x: play())
        la = tk.Label(top, text="Select a Song to play of our choice",fg='black',bg='blue')
        la.pack()
        top.mainloop()
    if pred == "Sad":
        x=random.randint(0,4)
        w1 = Label(top, text=f'we are playing {pred} songs for you', font="50", fg='black', bg='blue')
        w1.pack()
        lb = tk.Listbox(top)
        lb.pack()
        music_dir = 'song\sad'
        songs = os.listdir(music_dir)
        fl = glob("song\sad\*.mp3")
        for f in fl:
            lb.insert(0, f)
        os.startfile(os.path.join(music_dir, songs[x]))
        lb.bind("<Double-Button>", lambda x: play())
        la = tk.Label(top, text="Select a Song to play of your choice",fg='black',bg='blue')
        la.pack()
        top.mainloop()
    if pred == "Frustated":
        x=random.randint(0,2)
        w1 = Label(top, text=f'we are playing Relaxing songs for you', font="50",fg='white',bg='black')
        w1.pack()
        lb = tk.Listbox(top)
        lb.pack()
        music_dir = 'song/Frustated'
        songs = os.listdir(music_dir)

        fl = glob("song/Frustated\*.mp3")
        for f in fl:
            lb.insert(0, f)
        os.startfile(os.path.join(music_dir, songs[x]))
        lb.bind("<Double-Button>", lambda x: play())
        la = tk.Label(top, text="Select a Song to play of your choice",fg='black',bg='blue')
        la.pack()
        top.mainloop()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


