import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Tabs(
            tabs=[
                ft.Tab(
                    "tab 1",
                    ft.Column(
                        [
                            ft.TextField(label="ID"),
                            ft.TextField(label="ID"),
                        ],
                        offset=ft.Offset(0,0.01)
                    )

                ),
                ft.Tab(
                    "tab 2",
                    ft.TextField(label="ID", ),
                ), ],
            expand=1,
        )
    )


ft.app(main)
