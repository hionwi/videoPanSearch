import flet as ft

from commons import process_bar, snack_bar
from tabs.enc_page import enc_page
from tabs.random_page import random_tab


def main(page: ft.Page):
    page.title = "进制转换器"
    page.overlay.append(process_bar)
    page.overlay.append(snack_bar)
    page.fonts = {
        "NotoSansSC": "fonts/NotoSansSC-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="NotoSansSC")

    tabs = ft.Tabs(
        animation_duration=300,
        tabs=[
            random_tab(page),
            enc_page(page),
        ],
        expand=1
    )

    page.add(tabs)


ft.app(main)
