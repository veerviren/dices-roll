from tkinter import *
from random import *
root = Tk()
root.geometry("550x650")
root.title("Dice roll simulator")
root.config(bg="black")
intro_label = Label(root, text = "Welcome to the dice roll simulator", fg="purple", bg="black", font=("calibri",20)).pack(pady=20)
rule_label= Label(root, text = " You win if you roll an even number ", fg = "cyan", bg = "black",font=("calibri",17) )
rule_label.pack(pady= 10)
# get the dice value
def get_number(x):
    if x=='\u2680':
        return(1)
    elif x=='\u2681':
        return(2)
    elif x=='\u2682':
        return(3)
    elif x=='\u2683':
        return(4)
    elif x=='\u2684':
        return(5)
    else :
        return(6)
    
       
#roll the dice
def roll_dice():
    d1 = choice(dice_list)
    d2 = choice(dice_list)

    v1 = get_number(d1)
    v2 = get_number(d2)

    #update labels
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)

    #update value labels
    value_label1.config(text=f"Dice 1 = {v1}")
    value_label2.config(text=f"Dice 2 = {v2}")

    #update total label
    total = v1 + v2
    if total%2==0:
     total_label.config(text =f"You won!! ({total})", fg="blue")
     dice_label1.config(fg = "blue")
     dice_label2.config(fg="blue")
    else:
        total_label.config(text =f"Try again ({total})", fg = "red")
        dice_label1.config(fg = "red")
        dice_label2.config(fg="red")


#create a dice list
dice_list = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
#create a frame
dice_frame = Frame(root, bg="black", highlightbackground="green", highlightthickness=3)
dice_frame.pack(pady = 20)

#create a total frame
total_frame = Frame(root, bg="black", highlightbackground="green", highlightthickness=3)
total_frame.pack(pady=40)

#create button frame
button_frame = Frame(root,bg="black" )
button_frame.pack(pady = 20)
#create dice labels
dice_label1 = Label(dice_frame, text  = "", font=("Helvetica", 100), bg="black", fg = "lightblue")
dice_label1.grid(row=0,column=0, padx = 30, pady = 8)
value_label1 = Label(dice_frame, text = "", bg="black", fg="lightblue", font=("calibri", 15))
value_label1.grid(row=1,column=0, padx = 5,pady=8)

dice_label2 = Label(dice_frame, text  = "", font=("Helvetica", 100), bg="black", fg = "lightblue")
dice_label2.grid(row=0,column=1, padx = 30, pady=8)
value_label2 = Label(dice_frame, text = "", bg="black", fg="lightblue",font=("calibri", 15))
value_label2.grid(row=1,column=1, padx = 5, pady=8)

# print total on screen
total_label = Label(total_frame, text = "", font=("calibri", 24), bg = "black", fg="lightblue")
total_label.pack(padx=72, pady=20)

#call roll_dice function
roll_dice()

#create a button
roll_button = Button(button_frame, text = "Roll dice", command=roll_dice, font=("calibri",20), padx=10, pady=10,bg = "green",fg="white", activebackground="lightblue")
roll_button.pack(side=LEFT, padx = 10)
exit_button = Button(button_frame, text = "Exit", command=quit, font=("calibri",20), padx=20, pady=10,bg = "red",fg="white", activebackground="lightblue")
exit_button.pack(side=RIGHT, padx = 10)

# Initial state 
total_label.config(text =f"Start", fg = "lightblue")
dice_label1.config(fg="yellow")
dice_label2.config(fg="yellow")
root.mainloop()
