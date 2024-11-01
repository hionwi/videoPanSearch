import flet as ft
from DrissionPage import SessionPage

snack_bar = ft.SnackBar(content=ft.Text("格式错误,请重新输入"), duration=1000)
process_bar = ft.ProgressBar(visible=False)
tv_show_dialog = ft.AlertDialog(modal=False, title=ft.Text("cc"))
p1 = SessionPage()

tv_start = 0
tv_count = 20

base_tv_url = "https://movie.douban.com/subject/"
base_api_url = "https://api.douban.com/v2/movie/subject/"
search_api_url = "https://api.douban.com/v2/movie/search?q="
api_key = {'apikey': '0ab215a8b1977939201640fa14c66bab'}

tv_list_url = "https://m.douban.com/rexxar/api/v2/tv/recommend?refresh=0&start={}&count={}&selected_categories=%7B%22%E7%B1%BB%E5%9E%8B%22:%22%E5%8F%A4%E8%A3%85%22,%22%E5%BD%A2%E5%BC%8F%22:%22%E7%94%B5%E8%A7%86%E5%89%A7%22%7D&uncollect=false&tags=%E5%8F%A4%E8%A3%85&sort=R&ck=ryE4"
animal_list_url = "https://m.douban.com/rexxar/api/v2/tv/recommend?refresh=0&start={}&count={}&selected_categories=%7B%22%E7%B1%BB%E5%9E%8B%22:%22%E5%8A%A8%E7%94%BB%22,%22%E5%BD%A2%E5%BC%8F%22:%22%E7%94%B5%E8%A7%86%E5%89%A7%22%7D&uncollect=false&tags=%E5%8A%A8%E7%94%BB&sort=R&ck=ryE4"
cookies = {
    "ck": "ryE4"
}


p2 = SessionPage()