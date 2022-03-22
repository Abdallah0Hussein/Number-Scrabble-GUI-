# Faculty of Computers and Artificial Intelligence
# Name: Abdallah Hussein Ibrahim Hussein
# My Account: abiza2013@gmail.com
# Date: March 2022

from tkinter import*
from tkinter import messagebox # to show messagebox as info
list1 = []          # list for player1's choices
list2 = []          # list for player2's choices
clicked = True      # Player1's Turn when clicked = True
counter = 0         # counter to check if there is a tie game or not
root = Tk()
root.title("Number Scrabble")
root.geometry('1200x500+150+150')


def disable_all_button():
    myButton1.config(state=DISABLED)
    myButton2.config(state=DISABLED)
    myButton3.config(state=DISABLED)
    myButton4.config(state=DISABLED)
    myButton5.config(state=DISABLED)
    myButton6.config(state=DISABLED)
    myButton7.config(state=DISABLED)
    myButton8.config(state=DISABLED)
    myButton9.config(state=DISABLED)

def check_winner():         # all cases of winning for player1 and player2
    global Winner, list1, list2, counter
    Winner = False
    if "1" in list1 and "5" in list1 and "9" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    elif "1" in list1 and "6" in list1 and "8" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    elif "2" in list1 and "4" in list1 and "9" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    elif "2" in list1 and "5" in list1 and "8" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    elif "2" in list1 and "6" in list1 and "7" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    elif "3" in list1 and "4" in list1 and "8" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    elif "3" in list1 and "5" in list1 and "7" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    elif "4" in list1 and "5" in list1 and "6" in list1:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player One Wins ^_^")
        disable_all_button()
        
    if "1" in list2 and "5" in list2 and "9" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
        
    elif "1" in list2 and "6" in list2 and "8" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
        
    elif "2" in list2 and "4" in list2 and "9" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
        
    elif "2" in list2 and "5" in list2 and "8" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
        
    elif "2" in list2 and "6" in list2 and "7" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
        
    elif "3" in list2 and "4" in list2 and "8" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
        
    elif "3" in list2 and "5" in list2 and "7" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
        
    elif "4" in list2 and "5" in list2 and "6" in list2:
        Winner = True
        messagebox.showinfo("Number Scrabble", "Congratulations, Player Two Wins ^_^")
        disable_all_button()
    

def button_click(b):
    global clicked, counter, list1, list2, Winner
    
    if b["text"] == "1" and clicked == True: # player1's turn because clicked = True
        b['text'] = 'X'
        myButton1.config(bg = 'red',state=DISABLED)     # change the colur and make this button disabled to avoid clicking on it again
        list1.append("1")       # add the number to the list of player 1 
        myLabel6.config(text=list1)     # show the number that player1 has chosen
        clicked = False         # to make player2 play
        counter += 1
        check_winner()
    elif b["text"] == "2" and clicked == True: 
            b['text'] = 'X'
            myButton2.config(bg = 'red',state=DISABLED)
            list1.append("2")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "3" and clicked == True: 
            b['text'] = 'X'
            myButton3.config(bg = 'red',state=DISABLED)
            list1.append("3")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "4" and clicked == True: 
            b['text'] = 'X'
            myButton4.config(bg = 'red',state=DISABLED)
            list1.append("4")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "5" and clicked == True: 
            b['text'] = 'X'
            myButton5.config(bg = 'red',state=DISABLED)
            list1.append("5")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "6" and clicked == True: 
            b['text'] = 'X'
            myButton6.config(bg = 'red',state=DISABLED)
            list1.append("6")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "7" and clicked == True:
            b['text'] = 'X'
            myButton7.config(bg = 'red',state=DISABLED)
            list1.append("7")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "8" and clicked == True:
            b['text'] = 'X'
            myButton8.config(bg = 'red',state=DISABLED)
            list1.append("8")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "9" and clicked == True:
            b['text'] = 'X'
            myButton9.config(bg = 'red',state=DISABLED)
            list1.append("9")
            myLabel6.config(text=list1)
            clicked = False
            counter += 1
            check_winner()
    elif b["text"] == "1" and clicked == False:     # player2's turn because clicked = False
            b['text'] = 'X'                                 
            myButton1.config(bg = 'purple',state=DISABLED)  # change the colur and make this button disabled to avoid clicking on it again
            clicked = True          # to make player1 play
            list2.append("1")           # add the number to the list of player 2
            myLabel7.config(text=list2)     # show the number that player2 has chosen
            counter += 1
            check_winner()
    elif b["text"] == "2" and clicked == False: 
            b['text'] = 'X'
            myButton2.config(bg = 'purple',state=DISABLED)
            list2.append("2")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    elif b["text"] == "3" and clicked == False: 
            b['text'] = 'X'
            myButton3.config(bg = 'purple',state=DISABLED)
            list2.append("3")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    elif b["text"] == "4" and clicked == False: 
            b['text'] = 'X'
            myButton4.config(bg = 'purple',state=DISABLED)
            list2.append("4")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    elif b["text"] == "5" and clicked == False: 
            b['text'] = 'X'
            myButton5.config(bg = 'purple',state=DISABLED)
            list2.append("5")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    elif b["text"] == "6" and clicked == False:
            b['text'] = 'X'
            myButton6.config(bg = 'purple',state=DISABLED)
            list2.append("6")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    elif b["text"] == "7" and clicked == False: 
            b['text'] = 'X'
            myButton7.config(bg = 'purple',state=DISABLED)
            list2.append("7")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    elif b["text"] == "8" and clicked == False:
            b['text'] = 'X'
            myButton8.config(bg = 'purple',state=DISABLED)
            list2.append("8")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    elif b["text"] == "9" and clicked == False: 
            b['text'] = 'X'
            myButton9.config(bg = 'purple',state=DISABLED)
            list2.append("9")
            myLabel7.config(text=list2)
            clicked = True
            counter += 1
            check_winner()
    if counter == 9 and Winner == False:        # checking if the game is Tie or not
        messagebox.showinfo("Number Scrabble","Tie Game")
        
root.config(bg="#fcedf1")
    
myButton1 = Button(root, text="1", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton1), border=5)
myButton2 = Button(root, text="2", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton2), border=5)
myButton3 = Button(root, text="3", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton3), border=5)
myButton4 = Button(root, text="4", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton4), border=5)
myButton5 = Button(root, text="5", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton5), border=5)
myButton6 = Button(root, text="6", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton6), border=5)
myButton7 = Button(root, text="7", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton7), border=5)
myButton8 = Button(root, text="8", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton8), border=5)
myButton9 = Button(root, text="9", font=("Helvetica", 20), width=3, height=2, command=lambda: button_click(myButton9), border=5)

myLabel1 = Label(root, text = "Choose A Number", font=("Helvetica", 20), bg= '#fcedf1', fg='black')
myLabel2 = Label(root, text = "Player One: ", font=("Helvetica", 20), bg= 'red')
myLabel3 = Label(root, text = "Player Two: ", font=("Helvetica", 20), bg = 'purple')
myLabel4 = Label(root, text = "Your Numbers: ", font=("Helvetica", 20), bg= '#fcedf1', fg='black')
myLabel5 = Label(root, text = "Your Numbers: ", font=("Helvetica", 20), bg= '#fcedf1', fg='black')
myLabel6 = Label(root, text = "", font=("Helvetica", 20), bg= '#fcedf1', fg='black')
myLabel7 = Label(root, text = "", font=("Helvetica", 20), bg= '#fcedf1', fg='black')

myButton1.place(x = 150, y=200)
myButton2.place(x = 250, y=200)
myButton3.place(x = 350, y=200)
myButton4.place(x = 450, y=200)
myButton5.place(x = 550, y=200)
myButton6.place(x = 650, y=200)
myButton7.place(x = 750, y=200)
myButton8.place(x = 850, y=200)
myButton9.place(x = 950, y=200)

myLabel1.place(x= 450, y=100)
myLabel2.place(x = 100, y=300)
myLabel3.place(x = 800, y=300)
myLabel4.place(x = 100, y=400)
myLabel5.place(x = 800, y=400)
myLabel6.place(x = 100, y=450)
myLabel7.place(x = 800, y=450)

root.mainloop()             #  To make the window of the game always run
