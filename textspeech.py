# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound


#Initialized window

root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = 'black')
root.title('Convertor - TEXT TO SPEECH')


#heading
Label(root, text = 'TEXT TO SPEECH' , font='Centaur 20 bold' , bg ='white smoke').pack()
Label(root, text ='CONVERTOR' , font ='Centaur 15 bold', bg = 'white smoke').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='Centaur 15 bold', bg ='white smoke').place(x=20,y=60)


#text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20,y=100)


#define function

def TextSpeech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('chat.mp3')
    playsound('chat.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'Centaur 15 bold', command = TextSpeech, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'Centaur 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='Centaur 15 bold', command = Reset).place(x=175 , y =140)


#infinite loop to run program
root.mainloop()