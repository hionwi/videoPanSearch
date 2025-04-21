# 视频网盘搜索 app

安装环境（推荐使用 [uv](https://docs.astral.sh/uv/)）

```
uv sync
```

运行 app

```
uv run flet run main.py
```

打包 app

```
uv run flet pack main.py --add-data "assets;assets"
```

参考 [Publishing Flet app to multiple platforms](https://flet.dev/docs/publish)

## 应用功能

鼠标停留显示视频简介

左键点击显示百度网盘链接

右键点击跳转到对应豆瓣页面

视频搜索功能

## 应用截图

![movie](docs/movie.png)

![summary](docs/summary.png)

![pan](docs/pan.png)
