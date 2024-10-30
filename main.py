import flet as ft

from tabs.enc_page import enc_page
from tabs.random_page import random_tab


def main(page: ft.Page):
    page.title = "进制转换器"
    page.scroll = ft.ScrollMode.AUTO
    snack_bar = ft.SnackBar(content=ft.Text("格式错误,请重新输入"), duration=1000)

    page.overlay.append(snack_bar)

    page.fonts = {
        "NotoSansSC": "fonts/NotoSansSC-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="NotoSansSC")

    tabs = ft.Tabs(
        animation_duration=300,
        tabs=[
            random_tab(page, snack_bar),
            enc_page(page, snack_bar),
        ],
    )

    page.add(tabs)


ft.app(main)
