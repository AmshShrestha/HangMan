from tkinter import*
from PIL import ImageTk,Image
import random

# Created word_list for hangman
word_list=["CAT","BEAR", "TIGER", "JACKAL", "CHEETAH","ELEPHANT","HEN", "DOVE", "CRANE", "PEACOCK", "FLAMINGO"]

#Setup score and chances
tries=6
score=0

#shows path of images in folder
image_path=["hangman6.png","hangman5.png","hangman4.png","hangman3.png","hangman2.png","hangman1.png","hangman0.png"]

#Created tkinter window
win=Tk()
win.title("Hangman")
win.geometry("600x500")
win.resizable(0,0)
win.iconbitmap("Hangman.ico")


#setup Hangman UI
def init():
    global hiddenword
    hiddenword=random.choice(word_list)
    global guessword
    guessword=[]
    for character in hiddenword:
        guessword.append("__")

    global lives
    lives=Label(win, text="Tries left : "+str(tries), font="bold")
    lives.place(x=450, y=0)

    global text_status
    text_status=Label(win, font="bold")
    text_status.place(x=250, y=100 )

    global score_status
    score_status=Label(win, text="Score : "+ str(score), font="bold")
    score_status.place(x=455, y=25)

    global word_display
    word_display=Label(win,text=guessword, font="20" "bold")
    word_display.place(x=200,y=160)

    global correct_word
    correct_word=Label(win, font="bold")
    correct_word.place(x=200, y=200)

    global button_A,button_B,button_C,button_D,button_E,button_F,button_G,button_H,button_I,button_J,button_K,button_L,button_M,button_N,button_O,button_P,button_Q,button_R,button_S,button_T,button_U,button_V,button_W,button_X,button_Y,button_Z

    button_A = Button(win, text="A", width=3, height=1, command=lambda: game_update("A"))
    button_A.place(x=10, y=400)


    button_B = Button(win, text="B", width=3, height=1, command=lambda: game_update("B"))
    button_B.place(x=60, y=400)

    button_C = Button(win, text="C", width=3, height=1, command=lambda: game_update("C"))
    button_C.place(x=110, y=400)

    button_D = Button(win, text="D", width=3, height=1, command=lambda: game_update("D"))
    button_D.place(x=160, y=400)

    button_E = Button(win, text="E", width=3, height=1, command=lambda: game_update("E"))
    button_E.place(x=210, y=400)

    button_F = Button(win, text="F", width=3, height=1, command=lambda: game_update("F"))
    button_F.place(x=260, y=400)

    button_G = Button(win, text="G", width=3, height=1, command=lambda: game_update("G"))
    button_G.place(x=310, y=400)

    button_H = Button(win, text="H", width=3, height=1, command=lambda: game_update("H"))
    button_H.place(x=360, y=400)

    button_I = Button(win, text="I", width=3, height=1, command=lambda: game_update("I"))
    button_I.place(x=410, y=400)

    button_J = Button(win, text="J", width=3, height=1, command=lambda: game_update("J"))
    button_J.place(x=460, y=400)

    button_K = Button(win, text="K", width=3, height=1, command=lambda: game_update("K"))
    button_K.place(x=510, y=400)

    button_L = Button(win, text="L", width=3, height=1, command=lambda: game_update("L"))
    button_L.place(x=560, y=400)

    button_M = Button(win, text="M", width=3, height=1, command=lambda: game_update("M"))
    button_M.place(x=10, y=430)

    button_N = Button(win, text="N", width=3, height=1, command=lambda: game_update("N"))
    button_N.place(x=60, y=430)

    button_O = Button(win, text="O", width=3, height=1, command=lambda: game_update("O"))
    button_O.place(x=110, y=430)

    button_P = Button(win, text="P", width=3, height=1, command=lambda: game_update("P"))
    button_P.place(x=160, y=430)

    button_Q = Button(win, text="Q", width=3, height=1, command=lambda: game_update("Q"))
    button_Q.place(x=210, y=430)

    button_R = Button(win, text="R", width=3, height=1, command=lambda: game_update("R"))
    button_R.place(x=260, y=430)

    button_S = Button(win, text="S", width=3, height=1, command=lambda: game_update("S"))
    button_S.place(x=310, y=430)

    button_T = Button(win, text="T", width=3, height=1, command=lambda: game_update("T"))
    button_T.place(x=360, y=430)

    button_U = Button(win, text="U", width=3, height=1, command=lambda: game_update("U"))
    button_U.place(x=410, y=430)

    button_V = Button(win, text="V", width=3, height=1, command=lambda: game_update("V"))
    button_V.place(x=460, y=430)

    button_W = Button(win, text="W", width=3, height=1, command=lambda: game_update("W"))
    button_W.place(x=510, y=430)

    button_X = Button(win, text="X", width=3, height=1, command=lambda: game_update("X"))
    button_X.place(x=560, y=430)

    button_Y = Button(win, text="Y", width=3, height=1, command=lambda: game_update("Y"))
    button_Y.place(x=10, y=460)

    button_Z = Button(win, text="Z", width=3, height=1, command=lambda: game_update("Z"))
    button_Z.place(x=60, y=460)

    try:
        global img
        img = Image.open(image_path[tries])
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        global panel
        panel = Label(win, image = img)
        panel.place(x = 0, y = 100)
    except FileNotFoundError as msg:
        print(msg)

#Updates Game when button is pressed.
def game_update(guess):
    global tries
    global hiddenword
    global score

    if guess in hiddenword:
        array=list(hiddenword)
        for i in range(0, len(hiddenword)):
            if str(array[i])==guess:
                guessword[i]=str(guess)
        word_display.configure(text=guessword)
        score = score + 1
        score_status.configure(text="Score : " + str(score))
        if not "__" in guessword:
            Win()
    else:
        tries=tries-1
        image = Image.open(image_path[tries])
        image = image.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel.configure(image=img)
        panel.image=img
        if tries==0:
            Lose()
        lives.configure(text="Tries left : "+str(tries))
        word_display.configure(text=guessword)

#Prevents reuse of same button
def game_disable():
    button_A.configure(state="disabled")
    button_B.configure(state="disabled")
    button_C.configure(state="disabled")
    button_D.configure(state="disabled")
    button_E.configure(state="disabled")
    button_F.configure(state="disabled")
    button_G.configure(state="disabled")
    button_H.configure(state="disabled")
    button_I.configure(state="disabled")
    button_J.configure(state="disabled")
    button_K.configure(state="disabled")
    button_L.configure(state="disabled")
    button_M.configure(state="disabled")
    button_N.configure(state="disabled")
    button_O.configure(state="disabled")
    button_P.configure(state="disabled")
    button_Q.configure(state="disabled")
    button_R.configure(state="disabled")
    button_S.configure(state="disabled")
    button_T.configure(state="disabled")
    button_U.configure(state="disabled")
    button_V.configure(state="disabled")
    button_W.configure(state="disabled")
    button_X.configure(state="disabled")
    button_Y.configure(state="disabled")
    button_Z.configure(state="disabled")

#Cleans-up existing UI
def game_destroy():
    button_A.destroy()
    button_B.destroy()
    button_C.destroy()
    button_D.destroy()
    button_E.destroy()
    button_F.destroy()
    button_G.destroy()
    button_H.destroy()
    button_I.destroy()
    button_J.destroy()
    button_K.destroy()
    button_L.destroy()
    button_M.destroy()
    button_N.destroy()
    button_O.destroy()
    button_P.destroy()
    button_Q.destroy()
    button_R.destroy()
    button_S.destroy()
    button_T.destroy()
    button_U.destroy()
    button_V.destroy()
    button_W.destroy()
    button_X.destroy()
    button_Y.destroy()
    button_Z.destroy()
    lives.destroy()
    panel.destroy()
    word_display.destroy()
    button_continue.destroy()
    score_status.destroy()
    text_status.destroy()
    correct_word.destroy()

#Shows win menu when game is won
def Win():

    global text_status
    text_status.configure(text="You won!")

    game_disable()

    global button_continue
    button_continue = Button(win, text="New Game", font="bold", command=lambda: new_game())
    button_continue.place(x=450, y=160)

#Shows lose menu when game is lost
def Lose():

    global text_status
    text_status.configure(text="YOU LOSE!" , font="bold")

    global correct_Word
    correct_word.configure(text="Correct Word : "+ str(hiddenword))


    game_disable()

    global button_continue
    button_continue = Button(win, text="Restart", font="bold", command=lambda: restart())
    button_continue.place(x=450, y=160)

# Starts new game after winning
def new_game():

    game_destroy()

    global score
    score=0

    global tries
    tries=6

    init()

#restarts game when game is lost
def restart():
    game_destroy()

    global score
    score=0

    global tries
    tries=6
    init()

init()
win.mainloop()
