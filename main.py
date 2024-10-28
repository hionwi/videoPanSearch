import random

import flet as ft
from flet_core import TextField


def main(page: ft.Page):
    page.title = "进制转换器"
    snack_bar = ft.SnackBar(content=ft.Text("格式错误,请重新输入"), duration=1000)

    page.overlay.append(snack_bar)

    page.fonts = {
        "NotoSansSC": "fonts/NotoSansSC-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="NotoSansSC")

    def convert_and_update(base: int, e):
        snack_bar.content.value = "格式错误,请重新输入"
        if e.data != "":
            try:
                n = int(e.data, base)
                er.value = bin(n)[2:]
                ba.value = oct(n)[2:]
                shi.value = str(n)
                shi_liu.value = hex(n)[2:].upper()
                wx.value = f"{n.bit_length()}位"
            except ValueError:
                e.data = e.data[:-1]
                wx.value = "0位"
                snack_bar.open = True
        else:
            er.value = ""
            ba.value = ""
            shi.value = ""
            shi_liu.value = ""
            wx.value = "0位"

        page.update()

    er = TextField(label="二进制", on_change=lambda e: convert_and_update(2, e))
    ba = TextField(label="八进制", on_change=lambda e: convert_and_update(8, e))
    shi = TextField(label="十进制", on_change=lambda e: convert_and_update(10, e))
    shi_liu = TextField(label="十六进制", on_change=lambda e: convert_and_update(16, e))
    wx = ft.Text(value="0位", size=18)

    def ge_random(e):
        snack_bar.content.value = "随机数过大或为空"
        try:
            n = random.getrandbits(int(sj_text.value))

            class E:
                data = str(n)

            convert_and_update(10, E)
        except ValueError:
            snack_bar.open = True
            page.update()

    sj_text = ft.TextField(label="随机数位数", on_submit=ge_random)
    sj = ft.ElevatedButton("生成随机数", on_click=ge_random)

    page.add(ft.Column([er, ba, shi, shi_liu, ft.Row([sj_text, sj]), wx]))


ft.app(main)
