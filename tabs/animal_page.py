import flet as ft

import commons
from base.tvshow import ShowView


def animal_page():
    animal_des_dist = {}
    cola = ShowView(commons.base_tv_url, commons.base_api_url, commons.api_key, animal_des_dist,
                    commons.animal_list_url)
    t = ft.Tab(tab_content=ft.Row([
        ft.Image(src="tv.png", width=25, height=25),
        ft.Text("动画")
    ]),
        content=ft.Container(
            cola,
            padding=8,
            expand=True,
        ),
    )
    return t
