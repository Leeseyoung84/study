import urllib.request
from bs4 import BeautifulSoup


#네이버에 들어가서 파이썬 검색 블로그 탭
baseUrl= 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl=input('검색어를 입력하세요')

#검색어를 한글로 입력하면 한글url을 변환하지 못해 에러가 발생
#한글의 검색어를 asc2코드로 변환해줄것






url=baseUrl+plusUrl


html = urllib.request.urlopen(url).read()       #url을 가져와서 읽음

soup = BeautifulSoup(html,'html.parser')

title = soup.find_all(class_='sh_blog_title')   #class파일이 저 이름으로 된것을 찾음

print(len(title))           #찾은 파일의 갯수

for i in title:
    print(i.attrs['title'])       #attrs속성['title']
    print(i.attrs['href'])            #attrs속성['href'=url을 의미함]
    print()