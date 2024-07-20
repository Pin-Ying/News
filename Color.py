# colors = {"red": 255, "green": 127, "blue": 0}
# red = 255
# green = 127
# blue = 0

import random


# 顏色(R,G,B)，範圍 0~255 => 轉16進位字串
def RGB_hex(R=0, G=0, B=0):
    colorNum = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    red = f"{colorNum[R // 16]}{colorNum[R % 16]}"
    green = f"{colorNum[G // 16]}{colorNum[G % 16]}"
    blue = f"{colorNum[B // 16]}{colorNum[B % 16]}"

    return f"#{red}{green}{blue}"


# 自動產生指定個數(num)的顏色數字串列，規則: -255開始遞減，-遞增至一半後遞減、-遞增至255
def get_color(num=1):
    colors = []
    for i in range(num):
        gap = 190 // (num - 1)
        if i == 0:
            green = 200
        red = 255 - gap * i
        blue = gap * i
        green -= gap if i <= num // 2 else -gap
        colors.append({"red": red, "green": green, "blue": blue})

    color_hex = [
        RGB_hex(color["red"], color["green"], color["blue"]) for color in colors
    ]
    return color_hex


# 隨機產生不重複顏色，且控制亮度、飽和度(亮度:每種顏色數值不能太低or太高，飽和度:每種數值差異夠大)
def get_colorRam(num=1, order=False):
    colors = []

    while len(colors) < num:
        red, green, blue = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        colorDic = {"red": red, "green": green, "blue": blue}
        if (
            (colorDic in colors)
            or (sum(colorDic.values())) < 400
            or (max(colorDic.values()) - min(colorDic.values()) < 100)
        ):
            continue
        colors.append(colorDic)
    color_hex = [
        RGB_hex(color["red"], color["green"], color["blue"]) for color in colors
    ]
    color_hex = sorted(color_hex, reverse=True) if order == True else color_hex

    print(color_hex)
    return color_hex
