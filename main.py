import flet as ft

from commons import process_bar
from tabs.anime_page import anime_page
from tabs.movie_page import movie_page
from tabs.tv_page import tv_page


def main(page: ft.Page):
    page.window.resizable = False
    page.title = "视频网盘搜索"
    page.overlay.append(process_bar)
    page.fonts = {
        "NotoSansSC": "fonts/NotoSansSC-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="NotoSansSC")

    tabs = ft.Tabs(
        animation_duration=300,
        tabs=[
            movie_page(),
            tv_page(),
            anime_page(),
        ],
        expand=True,
    )

    page.add(tabs)


ft.app(main)
