from bs4 import BeautifulSoup


with open('parsing\scrap_tutorial\lesson1\\blank\index.html',encoding='utf-8') as file:
    src = file.read()


soup = BeautifulSoup(src,'lxml')     