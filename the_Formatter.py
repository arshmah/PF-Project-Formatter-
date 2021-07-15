#importing all the necessaries
import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x400")
root.title("The Formatter")
root.minsize(400,400)
root.maxsize(400,400)
root.configure(bg="orange")


def tab_1():
    def tab_2():
        label1.destroy()
        label_info.destroy()
        next_btn.destroy()
    
        label2 = tk.Label(root , text ="Enter Text Below To Format...", fg="#20bebe", font=('Copperplate Gothic Bold',17))
        label2.pack()
        #creating a text box to get user input
        my_box = tk.Entry(root, width=21,bg="silver",fg="black", font=('amaze',17))
        my_box.pack(pady=6)
        #creating a function for removing extra spaces from the user's text
#global text_without_spaces
        def remove_extra_space():
            text = str(my_box.get())
            text1 = text.strip()
            text_without_spaces = ""

            for character in text1:
                if character != " ":
                    text_without_spaces = text_without_spaces + character
            print(text_without_spaces)

            if not text:
                tk.messagebox.showinfo('Error', 'WRITE TEXT FIRST...')
            else:
                ans_box = tk.Text(root, width=30, height=0.5)
                ans_box.insert(0.1,text_without_spaces)
                ans_box.pack()
        btn1 = tk.Button(root, text="Remove Spaces", command=remove_extra_space, width=26, bg="#20bebe", fg="white", font=('ethnocentric',15))
        btn1.pack(pady=3)
        #crreating function for counting characters
        def char_count():
            text2 = str(my_box.get())
            counted = len(text2)
            ans = str(counted)
            print(ans)
            if not text2:
                tk.messagebox.showinfo('Error', 'WRITE TEXT FIRST...')
            else:
                ans_box = tk.Text(root, width=30, height=0.5)
                ans_box.insert(0.1,ans)
                ans_box.pack()
#global ans
        my_button2 = tk.Button(root , text ="Charactor Count", command = char_count, width=26, bg="#20bebe", fg="white", font=('ethnocentric',15)) 
        my_button2.pack(pady=3)
        #creating another funtion for removing punctuation from user's text
        def remove_punctuation():
            text3 = str(my_box.get())
            punc_list = ["," , "." , "!" , ";" , ":" , "?"]
            text_without_punctuations = ""

            for character in text3:
                if character not in punc_list:
                    text_without_punctuations += character
            print(text_without_punctuations)
            if not text3:
                tk.messagebox.showinfo('Error', 'WRITE TEXT FIRST...')
            elif character not in text3:
                tk.messagebox.showinfo('Error', 'TEXT IS WITHOUT PUNCTUATIONS ALREDY...')
            else:
                ans_box = tk.Text(root, width=30, height=0.5)
                ans_box.insert(0.1,text_without_punctuations)
                ans_box.pack()
#global text_without_punctuations

        btn3 = tk.Button(root, text="Remove Punctuations", command=remove_punctuation, width=26, bg="#20bebe", fg="white", font=('ethnocentric',15))
        btn3.pack(pady=3)

        #Creating another function to capitalize all letters
        def Capital():
            text4 = str(my_box.get())
            upper_case = text4.upper()
            print(upper_case)
            if not text4:
                tk.messagebox.showinfo('Error', 'WRITE TEXT FIRST...')
            else:
                ans_box = tk.Text(root, width=30, height=0.5)
                ans_box.insert(0.1,upper_case)
                ans_box.pack()
#global uppercase
        btn4 = tk.Button(root, text="Capitalize All Letters", command=Capital ,width=26, bg="#20bebe", fg="white", font=('lucidia handwritting',15))
        btn4.pack(pady=3)


#Creating a function for page connection   
        def back():
            label2.destroy()
            back_btn.destroy()
            my_box.destroy()
            #ans_box.destroy()
            btn1.destroy()
            my_button2.destroy()
            btn3.destroy()
            btn4.destroy()
            tab_1()

        back_btn = tk.Button(root, text="Back", width=10, height=2,command=back,bg="#20bebe", activebackground="blue")
        back_btn.pack(side=BOTTOM)
        


    label1 = tk.Label(root, text="Welcome Users!", bg="orange",fg="#FF1493",font=('Copperplate Gothic Bold', 26))
    label1.pack()
    label_info = tk.Label(root, text="Click on the \n below button \n to \n Explore More :)",bg="orange", fg="#FF1493",font=('Copperplate Gothic Bold', 26))
    label_info.pack(pady=6)
    next_btn = tk.Button(root, text="Lets Start",width=10, height=4,command=tab_2,bg="#20bebe",activebackground="blue")
    next_btn.pack(side=BOTTOM)
    





tab_1()
root.mainloop()