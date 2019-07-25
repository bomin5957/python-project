import time
from tkinter import *


def wordview():
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    word = open('words/word-'+str(day)+'.txt', 'r')
    meaning = open('meanings/meaning-'+str(day)+'.txt', 'r')

    word_list=[]
    meaning_list=[]
    for i in word:
        word_list.append(i.replace("\n",""))

    for i in meaning:
        meaning_list.append(i.replace("\n",""))


    window = Tk()
    window.title('wordview')

    w_l1 = Label(window,text="1. "+ word_list[0],bg = "white",font=("consolas",30))
    w_l1.pack()
    m_l1 = Label(window,text=meaning_list[0],bg="white",font=("consolas",10))
    m_l1.pack()

    w_l2 = Label(window,text="2. "+ word_list[1],bg = "white",font=("consolas",30))
    w_l2.pack()
    m_l2 = Label(window,text=meaning_list[1],bg="white",font=("consolas",10))
    m_l2.pack()

    w_l3 = Label(window,text="3. "+ word_list[2],bg = "white",font=("consolas",30))
    w_l3.pack()
    m_l3 = Label(window,text=meaning_list[2],bg="white",font=("consolas",10))
    m_l3.pack()

    w_l4 = Label(window,text="4. "+ word_list[3],bg = "white",font=("consolas",30))
    w_l4.pack()
    m_l4 = Label(window,text=meaning_list[3],bg="white",font=("consolas",10))
    m_l4.pack()

    w_l5 = Label(window,text="5. "+ word_list[4],bg = "white",font=("consolas",30))
    w_l5.pack()
    m_l5 = Label(window,text=meaning_list[4],bg="white",font=("consolas",10))
    m_l5.pack()

    window.mainloop()
