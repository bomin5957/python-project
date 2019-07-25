import time
from tkinter import *
from random import *


def wordtest():
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    word = open('words/word-'+str(day)+'.txt', 'r')
    meaning = open('meanings/meaning-'+str(day)+'.txt', 'r')

    test_all = open('meanings/allmeanings.txt', 'r')

    word_list=[]
    meaning_list=[]
    all_list=[]
    m_list=[]
    for i in word:
        word_list.append(i.replace("\n",""))

    for i in meaning:
        meaning_list.append(i.replace("\n",""))

    for i in test_all:
        all_list.append(i.replace("\n",""))
    size = len(all_list)



    window = Tk()
    window.title('wordtest')

    num_list=[]
    for i in range(4):
        num = randrange(size)
        while num in num_list :
            num = randrange(size)
        num_list.append(num)
    ans = randrange(5)
    for i in num_list:
        m_list.append(all_list[i])
    m_list.insert(ans,meaning_list[0])
    w_l1 = Label(window,text="1. "+ word_list[0],bg = "white",font=("consolas",20))
    w_l1.pack()
    m_l1_1 = Label(window,text = "1. " + m_list[0],bg = "white",font=("consolas",10))
    m_l1_2 = Label(window,text = "2. " + m_list[1],bg = "white",font=("consolas",10))
    m_l1_3 = Label(window,text = "3. " + m_list[2],bg = "white",font=("consolas",10))
    m_l1_4 = Label(window,text = "4. " + m_list[3],bg = "white",font=("consolas",10))
    m_l1_5 = Label(window,text = "5. " + m_list[4],bg = "white",font=("consolas",10))
    m_l1_1.pack()
    m_l1_2.pack()
    m_l1_3.pack()
    m_l1_4.pack()
    m_l1_5.pack()
    e1 = Entry(window)
    e1.pack()

    def check1(t1 = ans):
        t2 = e1.get()
        if int(t1) + 1 == int(t2):
            e1.insert(0,"clear, ")
    submit_button1 = Button(window, text = "확인",font=("consolas",14), bg = "gray",command=check1)
    submit_button1.pack()

    num_list=[]
    for i in range(4):
        num = randrange(size)
        while num in num_list :
            num = randrange(size)
        num_list.append(num)
    ans = randrange(5)
    for i in num_list:
        m_list.append(all_list[i])
    m_list.insert(ans,meaning_list[1])
    w_l2 = Label(window,text="2. "+ word_list[1],bg = "white",font=("consolas",20))
    w_l2.pack()
    m_l2_1 = Label(window,text = "1. " + m_list[0],bg = "white",font=("consolas",10))
    m_l2_2 = Label(window,text = "2. " + m_list[1],bg = "white",font=("consolas",10))
    m_l2_3 = Label(window,text = "3. " + m_list[2],bg = "white",font=("consolas",10))
    m_l2_4 = Label(window,text = "4. " + m_list[3],bg = "white",font=("consolas",10))
    m_l2_5 = Label(window,text = "5. " + m_list[4],bg = "white",font=("consolas",10))
    m_l2_1.pack()
    m_l2_2.pack()
    m_l2_3.pack()
    m_l2_4.pack()
    m_l2_5.pack()
    e2 = Entry(window)
    e2.pack()

    def check2(t1 = ans):
        t2 = e2.get()
        if int(t1) + 1 == int(t2):
            e2.insert(0,"clear, ")
    submit_button2 = Button(window, text = "확인",font=("consolas",14), bg = "gray",command=check2)
    submit_button2.pack()



    num_list=[]
    for i in range(4):
        num = randrange(size)
        while num in num_list :
            num = randrange(size)
        num_list.append(num)
    ans = randrange(5)
    for i in num_list:
        m_list.append(all_list[i])
    m_list.insert(ans,meaning_list[2])
    w_l3 = Label(window,text="3. "+ word_list[2],bg = "white",font=("consolas",20))
    w_l3.pack()
    m_l3_1 = Label(window,text = "1. " + m_list[0],bg = "white",font=("consolas",10))
    m_l3_2 = Label(window,text = "2. " + m_list[1],bg = "white",font=("consolas",10))
    m_l3_3 = Label(window,text = "3. " + m_list[2],bg = "white",font=("consolas",10))
    m_l3_4 = Label(window,text = "4. " + m_list[3],bg = "white",font=("consolas",10))
    m_l3_5 = Label(window,text = "5. " + m_list[4],bg = "white",font=("consolas",10))
    m_l3_1.pack()
    m_l3_2.pack()
    m_l3_3.pack()
    m_l3_4.pack()
    m_l3_5.pack()
    e3 = Entry(window)
    e3.pack()

    def check3(t1 = ans):
        t2 = e3.get()
        if int(t1) + 1 == int(t2):
            e3.insert(0,"clear, ")
    submit_button3 = Button(window, text = "확인",font=("consolas",14), bg = "gray",command=check3)
    submit_button3.pack()

    num_list=[]
    for i in range(4):
        num = randrange(size)
        while num in num_list :
            num = randrange(size)
        num_list.append(num)
    ans = randrange(5)
    for i in num_list:
        m_list.append(all_list[i])
    m_list.insert(ans,meaning_list[3])
    w_l4 = Label(window,text="4. "+ word_list[3],bg = "white",font=("consolas",20))
    w_l4.pack()
    m_l4_1 = Label(window,text = "1. " + m_list[0],bg = "white",font=("consolas",10))
    m_l4_2 = Label(window,text = "2. " + m_list[1],bg = "white",font=("consolas",10))
    m_l4_3 = Label(window,text = "3. " + m_list[2],bg = "white",font=("consolas",10))
    m_l4_4 = Label(window,text = "4. " + m_list[3],bg = "white",font=("consolas",10))
    m_l4_5 = Label(window,text = "5. " + m_list[4],bg = "white",font=("consolas",10))
    m_l4_1.pack()
    m_l4_2.pack()
    m_l4_3.pack()
    m_l4_4.pack()
    m_l4_5.pack()
    e4 = Entry(window)
    e4.pack()

    def check4(t1 = ans):
        t2 = e4.get()
        if int(t1) + 1 == int(t2):
            e4.insert(0,"clear, ")
    submit_button4 = Button(window, text = "확인",font=("consolas",14), bg = "gray",command=check4)
    submit_button4.pack()

    num_list=[]
    for i in range(4):
        num = randrange(size)
        while num in num_list :
            num = randrange(size)
        num_list.append(num)
    ans = randrange(5)
    for i in num_list:
        m_list.append(all_list[i])
    m_list.insert(ans,meaning_list[4])
    w_l5 = Label(window,text="5. "+ word_list[4],bg = "white",font=("consolas",20))
    w_l5.pack()
    m_l5_1 = Label(window,text = "1. " + m_list[0],bg = "white",font=("consolas",10))
    m_l5_2 = Label(window,text = "2. " + m_list[1],bg = "white",font=("consolas",10))
    m_l5_3 = Label(window,text = "3. " + m_list[2],bg = "white",font=("consolas",10))
    m_l5_4 = Label(window,text = "4. " + m_list[3],bg = "white",font=("consolas",10))
    m_l5_5 = Label(window,text = "5. " + m_list[4],bg = "white",font=("consolas",10))
    m_l5_1.pack()
    m_l5_2.pack()
    m_l5_3.pack()
    m_l5_4.pack()
    m_l5_5.pack()
    e5 = Entry(window)
    e5.pack()

    def check5(t1 = ans):
        t2 = e5.get()
        if int(t1) + 1 == int(t2):
            e5.insert(0,"clear, ")
    submit_button5 = Button(window, text = "확인",font=("consolas",14), bg = "gray",command=check5)
    submit_button5.pack()
    window.mainloop()
