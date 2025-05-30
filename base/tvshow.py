import asyncio
import base64
import webbrowser

import aiohttp
import flet as ft

import commons
from utils import extract_https_links, extract_code


class ShowCard(ft.Card):

    def did_mount(self):
        super().did_mount()
        self.page.run_task(self.get_img, self.cover_url)
        self.page.run_task(self.get_summary, self.api_url, commons.api_key)
        self.get_tv()

    def __init__(self, title, cover_url, tv_id, subtitle, tv_des_dict):
        super().__init__()
        self.tv_url_dict = {}
        self.tv_des_dict = tv_des_dict
        self.loading_des = ft.ProgressRing(visible=True, width=70, height=70)
        self.id = tv_id
        self.api_url = commons.base_api_url + self.id
        self.title = ft.Text(title, size=18)
        self.cover_url = cover_url
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
            ], alignment=ft.alignment.center
        )

        self.content = ft.Container(
            ft.Stack(
                [
                    self.tv_summary,
                    ft.Row(
                        [
                            self.tv_img,
                            self.tv_title
                        ], expand=True
                    ),
                    ft.GestureDetector(
                        on_secondary_tap=lambda e: webbrowser.open(commons.base_tv_url + self.id)
                    )
                ], expand=True
            ),
            on_click=self.tv_url_show,
        )

    def on_hover(self, e):
        if e.data == 'true':
            self.show_details()
        else:
            self.hide_details()

    def show_details(self):
        self.tv_img.visible = False
        self.tv_title.visible = False
        self.tv_summary.visible = False
        if self.id in self.tv_des_dict:
            self.tv_des.value = "剧情简介：" + self.tv_des_dict[self.id]
        else:
            self.tv_des.value = "剧情简介：暂无数据"
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

    async def get_summary(self, url, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                js = await response.json()
                self.tv_des_dict[self.id] = js['summary']

    async def get_img(self, url):
        for i in range(3):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        jsn = await response.content.read()
                        self.tv_img.controls[0].content.src_base64 = base64.b64encode(jsn).decode()
                        self.tv_img.controls[0].content.visible = True
                        self.content.on_hover = self.on_hover
                        self.loading_des.visible = False
                        self.update()
                        break
            except:
                await asyncio.sleep(1)

    async def get_tv_url(self, url, name):
        data = {
            'name': name,
            'token': 'i69'
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                js = await response.json()
                self.tv_url_dict[url] = js

    def get_tv(self):
        getJuzi = "http://m.kkqws.com/v/api/getJuzi"
        search = "http://m.kkqws.com/v/api/search"
        getXiaoyu = "http://m.kkqws.com/v/api/getXiaoyu"

        if getJuzi not in self.tv_url_dict.keys():
            self.page.run_task(self.get_tv_url, getJuzi, self.title.value)
        if getXiaoyu not in self.tv_url_dict.keys():
            self.page.run_task(self.get_tv_url, getXiaoyu, self.title.value)
        if search not in self.tv_url_dict.keys():
            self.page.run_task(self.get_tv_url, search, self.title.value)

    def tv_url_show(self, e):
        urls = ft.Column()
        for k, v in self.tv_url_dict.items():
            try:
                for ita in v['list']:
                    if "夸克" in ita['question'] or "迅雷" in ita['question']:
                        continue
                    p_urls = extract_https_links(ita['answer'])
                    if len(p_urls) == 0:
                        continue
                    for url in p_urls:
                        if "baidu" not in url:
                            continue
                        if "?pwd=" not in url:
                            url += "?pwd=" + extract_code(ita['answer'])
                        urls.controls.append(
                            ft.Text(ita['question'], selectable=True)
                        )
                        urls.controls.append(
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text=url,
                                        url=url,
                                        style=ft.TextStyle(color=ft.colors.BLUE),
                                    )
                                ]
                                ,
                                selectable=True
                            )
                        )
            except:
                pass
        if len(urls.controls) == 0:
            urls.controls.append(
                ft.Text("没有数据")
            )
        commons.tv_show_dialog.title = ft.Text(f"《{self.title.value}》")
        commons.tv_show_dialog.content = urls
        self.page.open(commons.tv_show_dialog)


class ShowView(ft.Column):
    def __init__(self, tv_des_dict, format_url):
        super().__init__()
        self.format_url = format_url
        self.tv_des_dict = tv_des_dict
        self.cards = ft.GridView(runs_count=4, expand=True)
        self.controls.append(self.cards)
        self.scroll = ft.ScrollMode.HIDDEN,
        self.alignment = ft.MainAxisAlignment.CENTER,
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.more_button = ft.Row(
            [
                ft.ElevatedButton("加载更多", expand=True)
            ]
        )

    def did_mount(self):
        super().did_mount()
        self.net_show()

    def next_show(self, e):
        commons.tv_start += commons.tv_count
        self.controls.remove(self.more_button)
        self.net_show()

    def net_show(self):
        commons.process_bar.visible = True
        self.page.update()
        commons.p1.get(
            self.format_url.format(commons.tv_start, commons.tv_count),
            cookies=commons.cookies)
        items = commons.p1.json['items']

        for item in items:
            self.cards.controls.append(
                ShowCard(
                    item['title'],
                    item['pic']['normal'],
                    item['id'],
                    "".join(str(item['card_subtitle']).split("/")[4:]),
                    self.tv_des_dict,
                )
            )
            self.cards.update()
        self.controls.append(self.more_button)
        self.more_button.controls[0].on_click = self.next_show
        commons.process_bar.visible = False
        self.page.update()


class ShowStack(ft.Column):
    def __init__(self, tv_des_dict, format_url):
        super().__init__()
        self.scroll = ft.ScrollMode.HIDDEN
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.format_url = format_url
        self.tv_des_dict = tv_des_dict
        self.search_result = TvSearchResult(tv_des_dict)
        self.show_view = ShowView(tv_des_dict, format_url)
        self.search_load = ft.ProgressRing(visible=False)
        self.search_bar = TvSearchBar(tv_des_dict, self.search_result, self.show_view, self.search_load)
        self.controls.append(ft.Row(
            [
                self.search_bar,
                self.search_load
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ))
        self.controls.append(
            ft.Stack(
                [
                    self.show_view,
                    self.search_result
                ]
            )
        )


class TvSearchResult(ft.Column):
    def __init__(self, tv_des_dict):
        super().__init__()
        self.tv_des_dict = tv_des_dict
        self.cards = ft.GridView(runs_count=4, expand=True)
        self.controls.append(self.cards)
        self.scroll = ft.ScrollMode.HIDDEN,
        self.alignment = ft.MainAxisAlignment.CENTER,
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.expand = True
        self.visible = False

    def add_card(self, title, cover_url, tv_id, subtitle):
        self.cards.controls.append(
            ShowCard(
                title,
                cover_url,
                tv_id,
                subtitle,
                self.tv_des_dict
            )
        )
        self.cards.update()


class TvSearchBar(ft.SearchBar):
    def __init__(self, tv_des_dict, ls: TvSearchResult, show_view: ShowView, load: ft.ProgressRing):
        super().__init__()
        self.autofocus = True
        self.load = load
        self.show_view = show_view
        self.tv_des_dict = tv_des_dict
        self.result_show = ls
        self.bar_hint_text = "搜索..."
        self.on_submit = self.submit
        self.on_change = self.change

    def change(self, e):
        if e.data == "":
            self.result_show.visible = False
            self.show_view.visible = True
            self.page.update()

    def build(self):
        super().build()
        self.page.on_keyboard_event = self.on_keyboard_event

    def on_keyboard_event(self, e):
        if e.key == "\\":
            self.focus()

    def submit(self, e):
        self.result_show.cards.clean()
        self.page.run_task(self.search_tv, commons.search_api_url + e.data, commons.api_key)

    async def search_tv(self, url, data):
        self.load.visible = True
        self.page.update()
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as response:
                js = await response.json()

                items = js['subjects']
                for item in items:
                    subtitles = ""
                    for cast in item['casts']:
                        subtitles = subtitles + cast['name'] + " "

                    self.result_show.add_card(
                        item['title'],
                        item['images']['small'],
                        item['id'],
                        subtitles
                    )
                self.load.visible = False
                self.result_show.visible = True
                self.show_view.visible = False
                self.page.update()
