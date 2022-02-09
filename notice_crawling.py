import requests
from bs4 import BeautifulSoup

URL = 'https://www.inu.ac.kr/user/boardList.do?boardId=49211&siteId=inu&id=inu_070202000000'
raw = requests.get(URL)

html = BeautifulSoup(raw.text, 'html.parser')

target = html.find('div', {'class' : 'tbList'})
titles = target.find_all('td', {'class' : 'textAL'})
 
num = 1
print("<인천대학교 최신 공지> \n")
for title in titles[0:10]:
    title_value = title.text.strip()
    print(f'{num}번 공지 : {title_value} \n')
    num += 1




URL2 = 'https://www.inu.ac.kr/user/indexMain.do?command=&siteId=electron'
raw2 = requests.get(URL2)

html2 = BeautifulSoup(raw2.text, 'html.parser')


titles2 = html2.find_all('a', {'class' : 'mini_text'})
num = 1


print("<전자공학과 최신 공지> \n")
for title2 in titles2[4:9]:
    print(f'{num}번 공지 : {title2.text} \n')
    num +=1 