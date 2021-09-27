# importing tkinter
from tkinter import *
#python imaging library
from PIL import ImageTk, Image
# importing random from standard library
import random
#importing login from another py file
import Login



# Creating list of words for hangman
word_list = ["CAT", "BEAR", "LION", "COMPUTER", "CHINA", "NEPAL", "DENMARK", "HEN", "DOVE", "CRANE", "NAME", "PLACE",
             "FAST",
             "SLOW", "KING", "THOR", "KRATOS", "DANTE", "VIDEO", "MUSIC"]

# Setuping score and chances value
tries = 6
score = 0

# shows path of images in respective folder
image_path = ["hangman6.png", "hangman5.png", "hangman4.png", "hangman3.png", "hangman2.png", "hangman1.png",
              "hangman0.png"]

# Created tkinter window
win = Tk()
win.title("Hangman")
win.geometry("600x500")
win.resizable(0, 0)
win.iconbitmap("Hangman.ico")


# setup Hangman UI
def init():
    global hiddenword
    hiddenword = random.choice(word_list) # storing all word_list value in hiddenword randomly
    global guessword
    guessword = [] #created empty list for guessword
    for character in hiddenword:
        guessword.append("_") #adds _ for every letter in word stored in hiddenwrod

    global lives
    lives = Label(win, text="Tries left : " + str(tries), font="bold") # Shows tries left text
    lives.place(x=450, y=0)

    global text_status
    text_status = Label(win, font="bold") #creates hidden text
    text_status.place(x=250, y=100)

    global score_status
    score_status = Label(win, text="Score : " + str(score), font="bold") #shows score text and points scored after correct word
    score_status.place(x=455, y=25)

    global word_display
    word_display = Label(win, text=guessword, font="20" "bold") #display word_dsiplay text
    word_display.place(x=200, y=160)

    global correct_word
    correct_word = Label(win, font="bold") #dispaly correct word text
    correct_word.place(x=200, y=200)


    global button_A, button_B, button_C, button_D, button_E, button_F, button_G, button_H, button_I, button_J, button_K, button_L, \
        button_M, button_N, button_O, button_P, button_Q, button_R, button_S, button_T, button_U, button_V, button_W, button_X, \
        button_Y, button_Z

    button_A = Button(win, text="A", width=3, height=1, command=lambda: game_update("A"))
    button_A.place(x=10, y=400)

    button_B = Button(win, text="B", width=3, height=1, command=lambda:game_update("B"))
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
      #inserting image and customising their sizes and using anti alias to make the look smooth
        global img
        img = Image.open(image_path[tries])
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
       # using panel to display image as label
        global panel
        panel = Label(win, image = img)
        panel.place(x = 0, y = 100)
    except FileNotFoundError as msg:
        print(msg)


# Updates Game when button is pressed.
def game_update(guess):
    global tries
    global hiddenword
    global score
    try:

        if guess in hiddenword: #guess is variable sotring hiddenword value
            array = list(hiddenword) #stores all the word in hidden word  separately in a list
            for i in range(0, len(hiddenword)): # loop runs from 0 to words length in hidden word
                if str(array[i]) == guess: # using array as string to check if word is in guess or not
                    guessword[i] = str(guess) # displaying all word in letter
                    score = score + 1 #increases score by +1
                    score_status.configure(text="Score : " + str(score)) #displays score text and score points
            word_display.configure(text = guessword) #displays word in guess word
            if "_" not in guessword: #shows win menu after all the word is correctly entered
                Win()
        else:
           
            try:
                                 
                tries = tries - 1 #decreases chances for every wrong word
                # displays images of hangman step by step
                image = Image.open(image_path[tries]) #displays images of hangman step by step
                image = image.resize((200, 200), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(image)
                panel.configure(image = img)
                panel.image = img
                if tries == 0: #shows lose menu if all the tries reaches 0
                    Lose()
                lives.configure(text = "Tries left : " + str(tries)) #displays tries left text
                word_display.configure(text = guessword)  #displays word in guess word
            except FileNotFoundError as msg:
                print(msg)
    except FileNotFoundError as msg:
        print(msg)

#prevents button from being used
def button_disable():
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

# erases existing UI
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


# Shows win menu when game is won
def Win():
    global text_status
    text_status.configure(text="You won!") #shows You won text

    button_disable() #Prevents user from using any button after winning

    global button_continue
    button_continue = Button(win, text="New Game", font="bold", command=lambda: new_game()) # shows new game button to reset game
    button_continue.place(x=450, y=160)


# Shows lose menu when game is lost
def Lose():
    global text_status
    text_status.configure(text="YOU LOSE!", font="bold") # shows you lose text

    global correct_Word
    correct_word.configure(text="Correct Word : " + str(hiddenword)) #shows correct word after all chances is finished

    button_disable() # disables user from reusing any button after losing

    global button_continue
    button_continue = Button(win, text="Restart", font="bold", command=lambda: restart()) # shows restart  game button to reset game
    button_continue.place(x=450, y=160)


# Starts new game after winning
def new_game():

    try:
        game_destroy() # erases existing ui

        global score
        score = 0 #sets score to 0

        global tries
        tries = 6 # sets tries  to 6

        init()
    except:
        print("Error Occurred During Execution")
        print("Restart the game")


# restarts game when game is lost
def restart():
    game_destroy()# erases existing ui

    global score
    score = 0 #sets score to 0

    global tries
    tries = 6 # sets tries  to 6
    init()


init()
win.mainloop()
