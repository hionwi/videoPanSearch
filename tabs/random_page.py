import random

import flet as ft
from flet_core import TextField

from commons import snack_bar


def random_tab(page: ft.Page):
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
    wx = ft.Text(value="0位", size=16)

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

    def clear_data(e):
        er.value = ""
        ba.value = ""
        shi.value = ""
        shi_liu.value = ""
        wx.value = "0位"
        sj_text.value = ""
        page.update()

    col = ft.Column(
        [
            ft.Text("", height=0),
            er, ba, shi, shi_liu,
            ft.Divider(),
            ft.Row([sj_text, sj]),
            ft.Divider(),
            wx,
            ft.ElevatedButton("清空数据", icon=ft.icons.DELETE, on_click=clear_data, color=ft.colors.RED)
        ],
    )
    t = ft.Tab(
        tab_content=ft.Row([
            ft.Image(src="shuffle.png", width=25, height=25),
            ft.Text("随机数生成与进制转换")
        ]),
        content=ft.Container(
            content=col,
            padding=8,
        )
    )
    return t
