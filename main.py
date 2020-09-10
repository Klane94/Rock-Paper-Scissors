import pygame
from tkinter import*
from random import randint

root = Tk()

root.iconbitmap('icon.png')
root.title("Rock Paper Scissors!")
root.resizable(width=False, height=False)

click = True

rock = PhotoImage(file='rocks.png')
scissors = PhotoImage(file='scissors.png')
paper = PhotoImage(file='paper.png')
tie = PhotoImage(file='score.png')
win = PhotoImage(file='win.png')
loose = PhotoImage(file='loser.png')

rockButton = ''
paperButton = ''
scissorsButton = ''


def play():
    global rockButton, paperButton, scissorsButton
    rockButton = Button(root, image=rock,
                        command=lambda: youpick('rock'))

    paperButton = Button(root, image=paper,
                         command=lambda: youpick('paper'))

    scissorsButton = Button(root, image=scissors,
                            command=lambda: youpick('scissors'))

    rockButton.grid(row=0, column=0)
    paperButton.grid(row=0, column=1)
    scissorsButton.grid(row=0, column=2)


def youpick(player):
    global click
    # options
    t = ['rock', 'paper', 'scissors']

    # assign random play to computer
    computer = t[randint(0, 2)]

    # game logic
    if click == True:
        if player == 'rock':
            rockButton.configure(image=rock)
            if computer == 'rock':
                paperButton.configure(image=rock)
                scissorsButton.configure(image=tie)
                click = False
            elif computer == 'paper':
                paperButton.configure(image=paper)
                scissorsButton.configure(image=loose)
                click = False
            else:
                paperButton.configure(image=scissors)
                scissorsButton.configure(image=win)
                click = False
        elif player == 'paper':
            paperButton.configure(image=paper)
            if computer == 'rock':
                rockButton.configure(image=rock)
                scissorsButton.configure(image=win)
                click = False
            elif computer == 'paper':
                rockButton.configure(image=paper)
                scissorsButton.configure(image=tie)
                click = False
            else:
                rockButton.configure(image=scissors)
                scissorsButton.configure(image=loose)
                click = False
        elif player == 'scissors':
            scissorsButton.configure(image=scissors)
            if computer == 'rock':
                paperButton.configure(image=rock)
                rockButton.configure(image=loose)
                click = False
            elif computer == 'paper':
                paperButton.configure(image=paper)
                rockButton.configure(image=win)
                click = False
            else:
                paperButton.configure(image=scissors)
                rockButton.configure(image=loose)
                click = False
        else:
            if player == 'rock' or player == 'paper' or player == 'scissors':
                rockButton.configure(image=rock)
                paperButton.configure(image=paper)
                scissorsButton.configure(image=scissors)
                click = True


play()

root.mainloop()
