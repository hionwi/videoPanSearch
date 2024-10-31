import flet as ft

from commons import process_bar, snack_bar
from tabs.net_page import net_page, net_show


def main(page: ft.Page):
    page.window.resizable = False
    page.window.maximizable = False
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
            # random_tab(page),
            # enc_page(page),
            net_page(page)
        ],
        expand=1,
        on_change=lambda e: net_show(e, page)
    )

    page.add(tabs)
    net_show(None, page)


ft.app(main)
