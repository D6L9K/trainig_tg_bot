
from bs4 import BeautifulSoup
with open('trainig_tg_bot\index.html') as file:
    src = file.read()
print(src)
# soup = BeautifulSoup(src, 'lxml')
#
# title = soup.title
# print(title)