import flet as ft

import commons
from base.tvshow import ShowView

a = {'count': 20, 'start': 0, 'total': 8, 'subjects': [
    {'rating': {'max': 10, 'average': 7.3, 'stars': '40', 'min': 0}, 'genres': ['剧情', '古装'],
     'title': '庆余年 第二季', 'casts': [{'alt': 'https://movie.douban.com/celebrity/1313867/', 'avatars': {
        'small': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg',
        'large': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg',
        'medium': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg'},
                                          'name': '张若昀', 'id': '1313867'},
                                         {'alt': 'https://movie.douban.com/celebrity/1274844/', 'avatars': {
                                             'small': 'https://img2.doubanio.com/view/celebrity/m/public/p1575489908.61.jpg',
                                             'large': 'https://img2.doubanio.com/view/celebrity/m/public/p1575489908.61.jpg',
                                             'medium': 'https://img2.doubanio.com/view/celebrity/m/public/p1575489908.61.jpg'},
                                          'name': '李沁', 'id': '1274844'},
                                         {'alt': 'https://movie.douban.com/celebrity/1045565/', 'avatars': {
                                             'small': 'https://img9.doubanio.com/view/personage/m/public/0879b6654b94c0aeb862c8433af54f06.jpg',
                                             'large': 'https://img9.doubanio.com/view/personage/m/public/0879b6654b94c0aeb862c8433af54f06.jpg',
                                             'medium': 'https://img9.doubanio.com/view/personage/m/public/0879b6654b94c0aeb862c8433af54f06.jpg'},
                                          'name': '陈道明', 'id': '1045565'}], 'collect_count': 317914,
     'original_title': '庆余年 第二季', 'subtype': 'tv', 'directors': [
        {'alt': 'https://movie.douban.com/celebrity/1315935/',
         'avatars': {'small': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg',
                     'large': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg',
                     'medium': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg'}, 'name': '孙皓',
         'id': '1315935'}], 'year': '2024',
     'images': {'small': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2907968100.jpg',
                'large': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2907968100.jpg',
                'medium': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2907968100.jpg'},
     'alt': 'https://movie.douban.com/subject/34937650/', 'id': '34937650'},
    {'rating': {'max': 10, 'average': 7.9, 'stars': '40', 'min': 0}, 'genres': ['剧情', '古装'],
     'title': '庆余年 第一季', 'casts': [{'alt': 'https://movie.douban.com/celebrity/1313867/', 'avatars': {
        'small': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg',
        'large': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg',
        'medium': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg'},
                                          'name': '张若昀', 'id': '1313867'},
                                         {'alt': 'https://movie.douban.com/celebrity/1274844/', 'avatars': {
                                             'small': 'https://img2.doubanio.com/view/celebrity/m/public/p1575489908.61.jpg',
                                             'large': 'https://img2.doubanio.com/view/celebrity/m/public/p1575489908.61.jpg',
                                             'medium': 'https://img2.doubanio.com/view/celebrity/m/public/p1575489908.61.jpg'},
                                          'name': '李沁', 'id': '1274844'},
                                         {'alt': 'https://movie.douban.com/celebrity/1045565/', 'avatars': {
                                             'small': 'https://img9.doubanio.com/view/personage/m/public/0879b6654b94c0aeb862c8433af54f06.jpg',
                                             'large': 'https://img9.doubanio.com/view/personage/m/public/0879b6654b94c0aeb862c8433af54f06.jpg',
                                             'medium': 'https://img9.doubanio.com/view/personage/m/public/0879b6654b94c0aeb862c8433af54f06.jpg'},
                                          'name': '陈道明', 'id': '1045565'}], 'collect_count': 1184412,
     'original_title': '庆余年 第一季', 'subtype': 'tv', 'directors': [
        {'alt': 'https://movie.douban.com/celebrity/1315935/',
         'avatars': {'small': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg',
                     'large': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg',
                     'medium': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg'}, 'name': '孙皓',
         'id': '1315935'}], 'year': '2019',
     'images': {'small': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2575362797.jpg',
                'large': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2575362797.jpg',
                'medium': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2575362797.jpg'},
     'alt': 'https://movie.douban.com/subject/25853071/', 'id': '25853071'},
    {'rating': {'max': 10, 'average': 0, 'stars': '00', 'min': 0}, 'genres': ['剧情', '古装'], 'title': '庆余年 第三季',
     'casts': [{'alt': 'https://movie.douban.com/celebrity/1313867/', 'avatars': {
         'small': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg',
         'large': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg',
         'medium': 'https://img1.doubanio.com/view/personage/m/public/8a5049855bbb9c6d14814625009c543c.jpg'},
                'name': '张若昀', 'id': '1313867'}, {'alt': 'https://movie.douban.com/celebrity/1274840/', 'avatars': {
         'small': 'https://img2.doubanio.com/view/personage/m/public/619f6f333570406107a9fd7e68ad3b2e.jpg',
         'large': 'https://img2.doubanio.com/view/personage/m/public/619f6f333570406107a9fd7e68ad3b2e.jpg',
         'medium': 'https://img2.doubanio.com/view/personage/m/public/619f6f333570406107a9fd7e68ad3b2e.jpg'},
                                                     'name': '吴刚', 'id': '1274840'}], 'collect_count': 6,
     'original_title': '庆余年 第三季', 'subtype': 'tv', 'directors': [
        {'alt': 'https://movie.douban.com/celebrity/1315935/',
         'avatars': {'small': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg',
                     'large': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg',
                     'medium': 'https://img9.doubanio.com/view/celebrity/m/public/p34416.jpg'}, 'name': '孙皓',
         'id': '1315935'}], 'year': '2027',
     'images': {'small': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2908491650.jpg',
                'large': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2908491650.jpg',
                'medium': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2908491650.jpg'},
     'alt': 'https://movie.douban.com/subject/35654271/', 'id': '35654271'},
    {'rating': {'max': 10, 'average': 0, 'stars': '00', 'min': 0}, 'genres': ['剧情', '古装'],
     'title': '庆余年之帝王业', 'casts': [{'alt': 'https://movie.douban.com/celebrity/1326498/', 'avatars': {
        'small': 'https://img3.doubanio.com/view/celebrity/m/public/p1622555055.03.jpg',
        'large': 'https://img3.doubanio.com/view/celebrity/m/public/p1622555055.03.jpg',
        'medium': 'https://img3.doubanio.com/view/celebrity/m/public/p1622555055.03.jpg'}, 'name': '李子峰',
                                           'id': '1326498'}, {'alt': 'https://movie.douban.com/celebrity/1434926/',
                                                              'avatars': {
                                                                  'small': 'https://img3.doubanio.com/view/personage/m/public/7f503946fd2442a42fa3b5d1bca9b997.jpg',
                                                                  'large': 'https://img3.doubanio.com/view/personage/m/public/7f503946fd2442a42fa3b5d1bca9b997.jpg',
                                                                  'medium': 'https://img3.doubanio.com/view/personage/m/public/7f503946fd2442a42fa3b5d1bca9b997.jpg'},
                                                              'name': '舒童', 'id': '1434926'}], 'collect_count': 104,
     'original_title': '庆余年之帝王业', 'subtype': 'tv', 'directors': [], 'year': '2024',
     'images': {'small': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2913445089.jpg',
                'large': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2913445089.jpg',
                'medium': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2913445089.jpg'},
     'alt': 'https://movie.douban.com/subject/37054789/', 'id': '37054789'},
    {'rating': {'max': 10, 'average': 0, 'stars': '00', 'min': 0}, 'genres': ['剧情', '古装'],
     'title': '庆余年之少年风流', 'casts': [], 'collect_count': 0, 'original_title': '庆余年之少年风流',
     'subtype': 'tv', 'directors': [], 'year': '2025',
     'images': {'small': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2907259378.jpg',
                'large': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2907259378.jpg',
                'medium': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2907259378.jpg'},
     'alt': 'https://movie.douban.com/subject/36860836/', 'id': '36860836'},
    {'rating': {'max': 10, 'average': 0, 'stars': '00', 'min': 0}, 'genres': ['动画'], 'title': '庆余年', 'casts': [],
     'collect_count': 27, 'original_title': '庆余年', 'subtype': 'tv', 'directors': [], 'year': '2030',
     'images': {'small': 'https://img1.doubanio.com/cuphead/movie-static/pics/tv_default_small.png',
                'large': 'https://img2.doubanio.com/cuphead/movie-static/pics/tv_default_large.png',
                'medium': 'https://img1.doubanio.com/cuphead/movie-static/pics/tv_default_medium.png'},
     'alt': 'https://movie.douban.com/subject/35025996/', 'id': '35025996'},
    {'rating': {'max': 10, 'average': 0, 'stars': '00', 'min': 0}, 'genres': ['短片'], 'title': '庆星年', 'casts': [
        {'alt': 'https://movie.douban.com/celebrity/1373314/',
         'avatars': {'small': 'https://img1.doubanio.com/view/celebrity/m/public/p1567425805.79.jpg',
                     'large': 'https://img1.doubanio.com/view/celebrity/m/public/p1567425805.79.jpg',
                     'medium': 'https://img1.doubanio.com/view/celebrity/m/public/p1567425805.79.jpg'},
         'name': '全建军', 'id': '1373314'}, {'alt': None, 'avatars': None, 'name': '夏浩铭', 'id': None},
        {'alt': None, 'avatars': None, 'name': '张鸣峰', 'id': None}], 'collect_count': 25, 'original_title': '庆星年',
     'subtype': 'movie', 'directors': [{'alt': None, 'avatars': None, 'name': '潘飞宏', 'id': None}], 'year': '2020',
     'images': {'small': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2581410670.jpg',
                'large': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2581410670.jpg',
                'medium': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2581410670.jpg'},
     'alt': 'https://movie.douban.com/subject/34953891/', 'id': '34953891'},
    {'rating': {'max': 10, 'average': 0, 'stars': '00', 'min': 0}, 'genres': ['纪录片', '短片'], 'title': '余年',
     'casts': [{'alt': None, 'avatars': None, 'name': '肖金秀', 'id': None}], 'collect_count': 22,
     'original_title': '余年', 'subtype': 'movie', 'directors': [{'alt': 'https://movie.douban.com/celebrity/1464420/',
                                                                  'avatars': {
                                                                      'small': 'https://img1.doubanio.com/view/personage/m/public/8e7cc32c0f92057878d73df4d8551ea8.jpg',
                                                                      'large': 'https://img1.doubanio.com/view/personage/m/public/8e7cc32c0f92057878d73df4d8551ea8.jpg',
                                                                      'medium': 'https://img1.doubanio.com/view/personage/m/public/8e7cc32c0f92057878d73df4d8551ea8.jpg'},
                                                                  'name': '陈名', 'id': '1464420'}], 'year': '2021',
     'images': {'small': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2762776902.jpg',
                'large': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2762776902.jpg',
                'medium': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2762776902.jpg'},
     'alt': 'https://movie.douban.com/subject/35371259/', 'id': '35371259'}], 'title': '搜索 "庆余年" 的结果'}


def test_page():
    tv_des_dict = {}
    cola = ShowView(commons.base_tv_url, commons.base_api_url, commons.api_key, tv_des_dict, commons.tv_list_url,
                    commons.search_api_url)

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
