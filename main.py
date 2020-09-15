from tkinter import*
from random import randint
'''
Authors: Kiara Lane, Jenna Fischer, Jordan Morley
Date: 9-17-2020
Description: Using python to create a rock paper scissors game
'''
root = Tk()

# screen size, title,and icon
root.iconbitmap('icon.png')
root.title("Rock Paper Scissors!")
root.resizable(width=False, height=False)

click = True

# images
rock = PhotoImage(file='rocks.png')
scissors = PhotoImage(file='scissors.png')
paper = PhotoImage(file='paper.png')
tie = PhotoImage(file='score.png')
win = PhotoImage(file='win.png')
loose = PhotoImage(file='loser.png')
rock_player = PhotoImage(file='rocksPlayer.png')
rock_computer = PhotoImage(file='rocksComputer.png')
scissors_player = PhotoImage(file='scissorsPlayer.png')
scissors_computer = PhotoImage(file='scissorsComputer.png')
paper_player = PhotoImage(file='paperPlayer.png')
paper_computer = PhotoImage(file='paperComputer.png')

# buttons
rockButton = ''
paperButton = ''
scissorsButton = ''
exitButton = ''

# set up buttons actions and locations
def play():
    global rockButton, paperButton, scissorsButton
    rockButton = Button(root, image=rock,
                        command=lambda: youpick('rock'))

    paperButton = Button(root, image=paper,
                         command=lambda: youpick('paper'))

    scissorsButton = Button(root, image=scissors,
                            command=lambda: youpick('scissors'))


    exit_button = Button(root, text='Exit',
                        command=lambda: root.destroy())

    rockButton.grid(row=0, column=0)
    paperButton.grid(row=0, column=1)
    scissorsButton.grid(row=0, column=2)
    exit_button.grid(row=1, column=2)


def youpick(player):
    global click
    # options
    t = ['rock', 'paper', 'scissors']

    # assign random play to computer
    computer = t[randint(0, 2)]

    # game logic
    if click == True:
        if player == 'rock':
            rockButton.configure(image=rock_player)
            if computer == 'rock':
                paperButton.configure(image=rock_computer)
                scissorsButton.configure(image=tie)
                click = False
            elif computer == 'paper':
                paperButton.configure(image=paper_computer)
                scissorsButton.configure(image=loose)
                click = False
            else:
                paperButton.configure(image=scissors_computer)
                scissorsButton.configure(image=win)
                click = False
        elif player == 'paper':
            rockButton.configure(image=paper_player)
            if computer == 'rock':
                paperButton.configure(image=rock_computer)
                scissorsButton.configure(image=win)
                click = False
            elif computer == 'paper':
                paperButton.configure(image=paper_computer)
                scissorsButton.configure(image=tie)
                click = False
            else:
                paperButton.configure(image=scissors_player)
                scissorsButton.configure(image=loose)
                click = False
        elif player == 'scissors':
            rockButton.configure(image=scissors_player)
            if computer == 'rock':
                paperButton.configure(image=rock_computer)
                scissorsButton.configure(image=loose)
                click = False
            elif computer == 'paper':
                paperButton.configure(image=paper_computer)
                scissorsButton.configure(image=win)
                click = False
            else:
                paperButton.configure(image=scissors_computer)
                scissorsButton.configure(image=loose)
                click = False
    else:
        if player == 'rock' or player == 'paper' or player == 'scissors':
            rockButton.configure(image=rock)
            paperButton.configure(image=paper)
            scissorsButton.configure(image=scissors)
            click = True


play()


root.mainloop()
