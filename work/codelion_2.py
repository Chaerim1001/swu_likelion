from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

search = input("검색할 키워드를 입력해주세요:")
page = int(input("크롤링할 페이지를 입력해주세요. ex)1(숫자만입력):"))
print("크롤링할 페이지: ",page,"페이지")   
page_num = 0
number = 1 # 크롤링 결과 번호 매기기 위한 변수

if page == 1:
    page_num =1
elif page == 0:
    page_num =1
else:
    page_num = page+9*(page-1)
    
url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page_num)
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }
original_html = requests.get(url, headers=headers)
html = BeautifulSoup(original_html.text, "html.parser")
articles = html.select("div.group_news > ul.list_news > li div.news_area > a")

num=[]
news_title = []

for i in articles:
    news_title.append(i.attrs['title'])
    num.append(number)
    number+=1

# 엑셀에 파일 저장하는 부분
news_data={"번호": num, "제목": news_title}
df = pd.DataFrame(news_data)

df.to_excel('export_sample.xlsx', sheet_name='news_name')
news=pd.read_excel('export_sample.xlsx', names = ['번호', '제목'], nrows=10)
print(news)