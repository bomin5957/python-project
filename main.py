import loading
from tkinter import *
import view
import test
loading.load() # 크롤링



window = Tk()

window.title('English_study')

button_wordview=Button(window, text = "오늘의 단어",font=("consolas",30), bg = "gray",width = 10,height = 2, command=view.wordview)
button_wordview.pack()

button_wordtest=Button(window, text = "단어 테스트",font=("consolas",30), bg = "gray",width = 10,height = 2, command=test.wordtest)
button_wordtest.pack()


window.mainloop()
