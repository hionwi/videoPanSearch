import flet as ft

import commons
from base.tvshow import ShowStack


def tv_page():
    tv_des_dict = {}
    cola = ShowStack(tv_des_dict, commons.tv_list_url)

    t = ft.Tab(tab_content=ft.Row([
        ft.Image(src="tv.png", width=25, height=25),
        ft.Text("电视剧")
    ]),
        content=ft.Container(
            cola,
            padding=8,
            expand=True,
        ),
    )
    return t
