import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def get_soup(page):
    resp = rq.get(url.format(page))
    resp.encoding = "utf-8"
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "lxml")
        return soup
    else:
        print("error!")
        return None


def get_dataframe(pageStart, pageEnd):
    datas = []
    for page in range(pageStart - 1, pageEnd):
        soup = get_soup(page)
        print(page, end="\n------")
        tags = soup.find("div", class_="view-content").find_all(
            "div", class_="views-row"
        )
        data = []
        for tag in tags:
            link = "https://tfc-taiwan.org.tw" + tag.find("a").get("href")
            tagsA = tag.find_all("a")
            title = tagsA[-2].text.strip()
            result = tagsA[1].text.strip()
            if len(tagsA) == 5:
                news_type = tagsA[2].text.strip()
            else:
                news_type = "其他"
            date = tag.find("div", class_="post-date").text.split("：")[-1]

            data.append([link, title, news_type, result, date])
            print([link, title, news_type, result, date], end="\n------\n")

        datas.extend(data)
    df = pd.DataFrame(datas, columns=["link", "title", "type", "result", "date"])
    return df


def get_pages(total_pages):
    pageStart, pageEnd = 1, 1
    pageCheck = input(f"總共頁數{total_pages}，請問是否要全部擷取？(y/n)")
    if pageCheck == "y":
        pageEnd = total_pages
        return pageStart, pageEnd
    else:
        while pageStart == 1:
            try:
                pageStart = eval(input("請輸入想要的起始頁數: "))
                pageEnd = eval(input("請輸入想要的結尾頁數: "))
                if pageEnd > total_pages or pageStart < 0 or pageEnd < pageStart:
                    print("輸入錯誤！請再輸入一次！")
                    pageStart = 1
                    continue
                return pageStart, pageEnd
            except Exception as e:
                print("error", e)


print("台灣事實查核中心擷取")

url = "https://tfc-taiwan.org.tw/articles/report?page={}"

soup = get_soup(0)
total_pages = int(soup.find("a", title="到最後一頁").get("href").split("=")[-1])
pageStart, pageEnd = get_pages(total_pages)

print("開始擷取資料...")
df = get_dataframe(pageStart, pageEnd)
df.to_csv(
    f"TFCnews_{datetime.now().strftime("%Y-%m-%d")}_page_{pageStart}-{pageEnd}.csv",
    encoding="utf-8-sig",
)

print(f"完成擷取！共{len(df)}筆資料")
