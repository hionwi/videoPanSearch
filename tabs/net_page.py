import base64
import webbrowser

import aiohttp
import flet as ft
from DrissionPage import SessionPage

from commons import process_bar

p1 = SessionPage()
p3 = SessionPage()

cards = ft.GridView(runs_count=4)

cola = ft.Column(
    [
        cards
    ],
    expand=True,
    scroll=ft.ScrollMode.HIDDEN,
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

tv_start = 0
tv_count = 20
tv_des_dict = {}
first_in = True


def next_show(e, page):
    global tv_start
    tv_start += tv_count
    cola.controls.remove(more_button)
    net_show(e, page, True)


more_button = ft.Row(
    [
        ft.ElevatedButton("加载更多", expand=True)
    ], expand=True
)


class TvCard(ft.Card):

    def __init__(self, title, cover_url, rating, tv_id, subtitle, page: ft.Page):
        super().__init__()
        self.is_isolate = True
        self.page = page
        self.loading_des = ft.ProgressRing(visible=True, width=70, height=70)
        self.id = tv_id
        self.tv_url = f"https://movie.douban.com/subject/{self.id}"
        self.api_url = f"https://api.douban.com/v2/movie/subject/{self.id}"
        self.api_key = {'apikey': '0ab215a8b1977939201640fa14c66bab'}
        self.title = ft.Text(title, size=18)
        self.cover_url = cover_url
        self.rating = rating
        self.subtitle = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            expand=1,
            scroll=ft.ScrollMode.HIDDEN
        )

        self.tv_name = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            expand=1,
            scroll=ft.ScrollMode.HIDDEN
        )
        self.tv_name.controls.extend(
            ft.Text(title[i], theme_style=ft.TextThemeStyle.TITLE_LARGE) for i in range(len(title)))

        self.subtitle.controls.extend(
            ft.Text(subtitle[i], size=12) for i in range(len(subtitle)))
        self.tv_title = ft.Row(
            [
                self.tv_name,
                self.subtitle
            ], expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.tv_des = ft.Text(expand=True, text_align=ft.TextAlign.JUSTIFY, size=16)
        self.tv_summary = ft.Column(
            [
                self.title,
                self.tv_des,
            ], expand=True,
            scroll=ft.ScrollMode.HIDDEN,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            visible=False
        )

        self.tv_img = ft.Stack(
            [
                ft.Container(
                    ft.Image(fit=ft.ImageFit.FILL, visible=False),
                    width=200,
                    height=300,
                ),
                self.loading_des
            ],alignment=ft.alignment.center
        )

        self.page.run_task(self.aio_get, self.cover_url)
        self.content = ft.Container(
            ft.Stack(
                [
                    self.tv_summary,
                    ft.Row(
                        [
                            self.tv_img,
                            self.tv_title
                        ], expand=True
                    )
                ], expand=True
            ),
            on_click=lambda e: webbrowser.open(self.tv_url),
        )
        self.page.run_task(self.aio_post, self.api_url, self.api_key)

    def on_hover(self, e):
        if e.data == 'true':
            self.show_details()
        else:
            self.hide_details()

    def show_details(self):
        self.tv_img.visible = False
        self.tv_title.visible = False
        self.tv_summary.visible = False
        if self.id in tv_des_dict:
            self.tv_des.value = "剧情简介：" + tv_des_dict[self.id]
        else:
            self.fetch_tv_details()
        self.tv_summary.visible = True
        self.tv_img.visible = False
        self.tv_title.visible = False
        self.content.padding = 12
        self.update()

    def hide_details(self):
        self.content.padding = 0
        self.tv_img.visible = True
        self.tv_title.visible = True
        self.tv_summary.visible = False
        self.update()

    def fetch_tv_details(self):
        try:
            p3.post(self.api_url, data=self.api_key)
            tv_des_dict[self.id] = p3.json['summary']
            self.tv_des.value = "剧情简介：" + tv_des_dict[self.id]
        except Exception as e:
            print(e)
            self.tv_des.value = "加载失败"

    async def aio_post(self, url, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                js = await response.json()
                tv_des_dict[self.id] = js['summary']

    async def aio_get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                jsn = await response.content.read()
                self.tv_img.controls[0].content.src_base64 = base64.b64encode(jsn).decode()
                self.tv_img.controls[0].content.visible = True
                self.content.on_hover = self.on_hover
                self.loading_des.visible = False
                self.update()


def net_show(e, page: ft.Page, more=False):
    global first_in
    # try:
    #     if e.name == "change" and e.data != '2':
    #         return
    # except:
    #     pass
    if first_in or more:
        first_in = False
        process_bar.visible = True
        page.update()

        cookies = {
            "ck": "ryE4"
        }
        p1.get(
            f"https://m.douban.com/rexxar/api/v2/tv/recommend?refresh=0&start={tv_start}&count={tv_count}&selected_categories=%7B%22%E7%B1%BB%E5%9E%8B%22:%22%E5%8F%A4%E8%A3%85%22,%22%E5%BD%A2%E5%BC%8F%22:%22%E7%94%B5%E8%A7%86%E5%89%A7%22%7D&uncollect=false&tags=%E5%8F%A4%E8%A3%85&sort=R&ck=ryE4",
            cookies=cookies)
        items = p1.json['items']
        for item in items:
            cards.controls.append(
                TvCard(item['title'], item['pic']['normal'], item['rating']['value'], item['id'],
                       "".join(str(item['card_subtitle']).split("/")[4:]),
                       page))
            cards.update()
        cola.controls.append(more_button)
        more_button.controls[0].on_click = lambda e: next_show(e, page)
        process_bar.visible = False
        page.update()


def net_page(page: ft.Page):
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
