import urllib.request
from bs4 import BeautifulSoup


#네이버에 들어가서 파이썬 검색 블로그 탭
url= 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

html = urllib.request.urlopen(url).read()       #url을 가져와서 읽음

soup = BeautifulSoup(html,'html.parser')

title = soup.find_all(class_='sh_blog_title')   #class파일이 저 이름으로 된것을 찾음

print(len(title))           #찾은 파일의 갯수

for i in title:
    print(i.attrs['title'])       #attrs속성['title']
    print(i.attrs['href'])            #attrs속성['href'=url을 의미함]
    print()