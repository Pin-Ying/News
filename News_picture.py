import matplotlib.pyplot as plt
import pandas as pd
import Color
from datetime import datetime

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False


def get_pie(datas, file_path=f"Pie_{datetime.now().strftime("%Y-%m-%d")}"):
    explo = [
        0.05 if i == max(datas.values) else 0.1 if i == min(datas.values) else 0
        for i in datas.values
    ]
    colors = Color.get_colorRam(len(datas))
    plt.figure(figsize=(6, 6))
    Pie = plt.pie(
        datas,
        labels=datas.index,
        shadow=True,
        autopct="%.2f%%",
        explode=explo,
        colors=colors,
        pctdistance=0.8,
    )

    for i in Pie[1]:
        i.set_color("black")
        i.set_fontsize(20)
    for i in Pie[2]:
        i.set_color("black")
        i.set_fontsize(12)

    plt.title("查核新聞種類", fontsize=22)
    plt.legend(loc=10)
    plt.savefig(f"./TFCnews/{file_path}.png", bbox_inches="tight")

    plt.show()


file_path = "2024-07-20_page_1-312"
df = pd.read_csv(f"./TFCnews/{file_path}.csv")
newsType = (
    df[df["result"] != "事實釐清"].groupby("type").size().sort_values(ascending=False)
)

get_pie(newsType, file_path="newsType" + file_path)
