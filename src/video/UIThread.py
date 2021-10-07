import threading
from tkinter import *


class UIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        window = Tk()
        window.title("SGT Helper")
        window.geometry("1080x720")
        window.minsize(480, 360)
        window.config(background='#f4f6c8')

        label_title = Label(window, text="Bienvenue sur SGT Helper", font=("Courrier", 40), bg='#f4f6c8', fg='#101f7a')
        label_title.pack()

        label_subtitle = Label(window, text="Voici les fonctionnalité a savoir pour utiliser l'application :",
                               font=("Courrier", 30), bg='#f4f6c8', fg='#101f7a')
        label_subtitle.pack()

        label_subtitle = Label(window, text="- Appuyer sur la touche A pour activé l'application", font=("Courrier", 20),
                               bg='#f4f6c8', fg='#101f7a')
        label_subtitle.pack()

        label_subtitle = Label(window, text="- Appuyer sur la touche E pour éteindre l'application", font=("Courrier", 20),
                               bg='#f4f6c8', fg='#101f7a')
        label_subtitle.pack()

        label_subtitle = Label(window,
                               text="- Au bout de 8 clignement de yeux, l'application s'eteindra au bout de 5 secondes",
                               font=("Courrier", 20), bg='#f4f6c8', fg='#101f7a')
        label_subtitle.pack()

        label_subtitle = Label(window, text="si vous ne voulez pas que l'application s'éteigne appuyé sur la touche B ",
                               font=("Courrier", 20), bg='#f4f6c8', fg='#101f7a')
        label_subtitle.pack()

        window.mainloop()
