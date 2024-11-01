import flet as ft

from commons import process_bar, snack_bar
from tabs.animal_page import animal_page
from tabs.test_page import test_page
from tabs.tv_page import tv_page


def main(page: ft.Page):
    page.window.resizable = False
    page.title = "工具箱"
    page.overlay.append(process_bar)
    page.overlay.append(snack_bar)
    page.fonts = {
        "NotoSansSC": "fonts/NotoSansSC-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="NotoSansSC")

    tabs = ft.Tabs(
        animation_duration=300,
        tabs=[
            test_page(),
            # animal_page(),
        ],
        expand=True,
    )

    page.add(tabs)


ft.app(main)
