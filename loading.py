from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

def load() :
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    word = open('words/word-'+str(day)+'.txt', 'w')
    meaning = open('meanings/meaning-'+str(day)+'.txt', 'w')

    allword = open('words/allwrods.txt','r')
    allmeaning = open('meanings/allmeanings.txt','r')
    tmpword = allword.read()
    tmpmeaning = allmeaning.read()
    allword.close()
    allmeaning.close()

    allword = open('words/allwrods.txt','a')
    allmeaning = open('meanings/allmeanings.txt','a')

    req = Request('https://learn.dict.naver.com/m/endic/today/words.nhn')
    res = urlopen(req)
    html = res.read().decode('utf-8')
    bs = BeautifulSoup(html,'html.parser')


    tags = bs.findAll('p',attrs={'class': 'txt_ct'})
    words=[]
    meanings=[]
    for tag in tags :
        words.append(tag.a.text)
    tags = bs.findAll('p',attrs={'class': 'txt_ct2'})
    for tag in tags :
        meanings.append(tag.text.replace(';', "").replace("    "," ").replace("\t","").replace('\n',""))
    for i in words :
        word.write(i+'\n')
        if i not in tmpword :
            allword.write(i+'\n')
    for i in meanings :
        meaning.write(i+'\n')
        if i not in tmpmeaning :
            allmeaning.write(i+'\n')

    word.close()
    meaning.close()
    allword.close()
    allmeaning.close()
