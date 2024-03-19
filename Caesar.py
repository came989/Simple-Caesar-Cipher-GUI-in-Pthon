from tkinter import *

def encrypt():
    #print(e.get())
    text = e.get()
    key = int(k.get())
    if key is not None and (text.isalpha() or char.isspace() for char in text) :
        ciphertext = ""
        for char in text.upper():
            if char == " ":
                ciphertext += " "
            else:
                ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        print(ciphertext)
    else:
        print("sadaw")   
    

def decrypt():
     text = d.get()
     key = int(k.get())
     if key is not None and (text.isalpha() or char.isspace() for char in text):
        ciphertext = ""
        for char in text.upper():
            if char == " ":
                ciphertext += " "
            else:
                ciphertext += chr((ord(char) - key - 65) % 26 + 65)
        print(ciphertext)
     else:
        pass

root = Tk()
labelEncr = Label(root,text="Encryption")
labelEncr.pack()
e = Entry(root)
e.pack()
labelDecr = Label(root,text="Decryption")
labelDecr.pack()
d = Entry(root)
d.pack()
labelKey = Label(root,text="Key")
labelKey.pack()
k = Entry()
k.pack()
encrButton = Button(root,text="Encrypt",command=encrypt)
encrButton.pack()
decrButton = Button(root,text="Decrypt",command=decrypt)
decrButton.pack()
root.geometry("800x500")

root.mainloop()