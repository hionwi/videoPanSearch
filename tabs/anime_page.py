import flet as ft

import commons
from base.tvshow import ShowStack


def anime_page():
    tv_des_dict = {}
    cola = ShowStack(tv_des_dict, commons.anime_list_url)

    t = ft.Tab(tab_content=ft.Row([
        ft.Image(src="tv.png", width=25, height=25),
        ft.Text("动漫")
    ]),
        content=ft.Container(
            cola,
            padding=8,
            expand=True,
        ),
    )
    return t
