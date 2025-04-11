from tkinter import *
from tkinter import messagebox
import base64
import os

def reset():
    code.set("")
    text1.delete(1.0,END)

# encrypt data
def encrypt():
    password= code.get()
    if password == "1234":
        screen1= Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#102E50")

        message= text1.get(1.0,END)
        encode_message= message.encode("ascii")
        base64_bytes= base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED DATA :", font=("roboto",14,"bold")).place(x=10,y=10)

        text2=Text(screen1,font="roboto 10", bg="#FAF1E6",fg="black", relief=GROOVE,wrap=WORD,bd=0)

        text2.place(x=10,y=40, width=380,height=150)
        text2.insert(END, encrypt)
    elif password=="":
        messagebox.showerror('Encryption',"Enter your key !!!")
    else:
        messagebox.showerror('Encryption',"Wrong Key !!!!!")


#decrypt data
def decrypt():
    password= code.get()
    if password == "1234":
        screen2= Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#169976")

        message= text1.get(1.0,END)
        decode_message= message.encode("ascii")
        base64_bytes= base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPTED DATA :", font=("roboto",14,"bold")).place(x=10,y=10)

        text2=Text(screen2,font="roboto 10", bg="#FAF1E6",fg="black", relief=GROOVE,wrap=WORD,bd=0)

        text2.place(x=10,y=40, width=380,height=150)
        text2.insert(END, decrypt)
    elif password=="":
        messagebox.showerror('Decryption',"Enter your key !!!")
    else:
        messagebox.showerror('Decryption',"Wrong Key !!!!!")



def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("400x400")

    logo= PhotoImage(file="logo.png")
    screen.iconphoto(True, logo)
    screen.title("LockIt")

    
    Label(text="Enter text for Encryption or decription:",fg="black" , font=("calbri", 12,"bold")).place(x=10,y=10)
    text1= Text(font=("roboto",12),bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=40,height=100,width=380)
    
    Label(text="Enter secret key for Encryption or decription:",fg="black" , font=("calbri", 12,"bold")).place(x=10,y=160)
    code= StringVar()
    Entry(textvariable=code,width=34,bd=0,font=("arial",14),show="*").place(x=10,y=190)



    Button(text="ENCRYPT",font=("roboto",10,"bold"), height="2", width=22,bg="#4F1C51" ,fg="white",bd=0, command=encrypt).place(x=10,y=230)
    Button(text="DECRYPT",font=("roboto",10,"bold"), height="2", width=22,bg="#336D82" ,fg="white",bd=0, command=decrypt).place(x=205,y=230)
    Button(text="RESET",font=("roboto",10,"bold"), height="2", width=46,bg="#EC5228" ,fg="white",bd=0, command=reset).place(x=10,y=290)
    
    screen.mainloop()

main_screen()