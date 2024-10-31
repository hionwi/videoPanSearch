import asyncio
import time

import flet as ft

from enc import generate_keys, sign, very
from commons import process_bar, snack_bar


def enc_page(page: ft.Page):
    def gk(e):
        try:
            assert 0 < len(id_input.value)
            pk, sk = generate_keys(id_input.value.encode())
            pk_input.value = bytes(pk).hex().upper()
            sk_input.value = bytes(sk).hex().upper()
            id_input_2.value = id_input.value

            id_input_3.value = id_input.value
            pk_input_2.value = bytes(pk).hex().upper()
        except:
            snack_bar.content.value = "生成密钥失败"
            snack_bar.open = True
        page.update()

    id_input = ft.TextField(label="ID", on_submit=gk)

    id_yes_button = ft.ElevatedButton("生成密钥", on_click=gk)

    id_input_2 = ft.TextField(label="ID", )
    message_input = ft.TextField(label="签名消息")
    pk_input = ft.TextField(label="公钥", )
    sk_input = ft.TextField(label="私钥", )

    def sign_message(e):
        try:
            assert 0 < len(pk_input.value)
            assert 0 < len(sk_input.value)
            assert 0 < len(id_input_2.value)
            sig = sign(id_input_2.value.encode(), bytes.fromhex(pk_input.value), bytes.fromhex(sk_input.value),
                       message_input.value.encode())

            message_input_2.value = message_input.value
            sig_input.value = bytes(sig).hex().upper()
        except:
            snack_bar.content.value = "签名失败"
            snack_bar.open = True
        page.update()

    sign_button = ft.ElevatedButton("签名", icon=ft.icons.EDIT, on_click=sign_message)

    id_input_3 = ft.TextField(label="ID", )
    message_input_2 = ft.TextField(label="签名消息", )
    pk_input_2 = ft.TextField(label="公钥", )
    sig_input = ft.TextField(label="签名", )

    def very_message(e):
        try:
            assert 0 < len(pk_input_2.value)
            assert 0 < len(sig_input.value)
            assert 0 < len(id_input_3.value)

            if very(id_input_3.value.encode(), bytes.fromhex(pk_input_2.value), message_input_2.value.encode(),
                    bytes.fromhex(sig_input.value)):
                snack_bar.content.value = "验证成功"
            else:
                snack_bar.content.value = "验证失败"
        except:
            snack_bar.content.value = "验证失败"
        snack_bar.open = True
        page.update()

    very_button = ft.ElevatedButton("验证", icon=ft.icons.VERIFIED, on_click=very_message)

    def clean_data(e):
        id_input.value = ""
        id_input_2.value = ""
        message_input.value = ""
        pk_input.value = ""
        sk_input.value = ""
        id_input_3.value = ""
        message_input_2.value = ""
        pk_input_2.value = ""
        sig_input.value = ""
        page.update()

    col = ft.Column(
        [
            ft.Text("",height=0),
            ft.Row([id_input, id_yes_button]),
            ft.Divider(),
            id_input_2, message_input, pk_input, sk_input, sign_button,
            ft.Divider(),
            id_input_3, message_input_2, pk_input_2, sig_input, very_button,
            ft.ElevatedButton(icon=ft.icons.DELETE, text="清空数据", on_click=clean_data, color=ft.colors.RED),
        ],
        scroll=ft.ScrollMode.HIDDEN,
    )

    return ft.Tab(
        tab_content=ft.Row([
            ft.Image(src="enc.png", width=25, height=25),
            ft.Text("加密与签名")
        ]),
        content=ft.Container(
            col,
            padding=8,
        ),

    )
