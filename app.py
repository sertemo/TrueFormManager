# Copyright 2024 Sergio Tejedor Moreno

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Script para desarrollar el código principal de la app con Flet



import flet as ft

from models import UsuarioDB

TITLE = 'TrueForm Manager'
COLOR_FONDO_GENERAL = '#5b6060'
VERDE_FOSFO = '#a5de37'

def main(page:ft.Page) -> None:
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    page.title = TITLE
    page.theme = ft.Theme(font_family="RobotoSlab")
    page.bgcolor = COLOR_FONDO_GENERAL
    page.window_width = 1000
    page.window_height = 800
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TRANSLATE, color=ft.colors.AMBER_50),
        #leading_width=180,
        title=ft.Row([
            ft.Text(TITLE.split()[0], weight=ft.FontWeight.BOLD, color=ft.colors.WHITE30),
            ft.Text(TITLE.split()[1], weight=ft.FontWeight.BOLD, color=VERDE_FOSFO)
        ]),
        bgcolor=COLOR_FONDO_GENERAL,
        toolbar_height=60,
        center_title=True,        
    )

    panel_control = ft.Container(
        ft.Column([
            ft.Container(
                ft.Row([
                    ft.Icon(ft.icons.MANAGE_ACCOUNTS, color=ft.colors.AMBER_50),
                    ft.Text('Panel de Control', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE60)
                ],
            alignment=ft.MainAxisAlignment.CENTER),
            ),
            *[ft.TextField(label=campo, height=26, text_size=15, content_padding=ft.padding.only(left=10),
                            cursor_color=VERDE_FOSFO,
                            filled=False, color=ft.colors.WHITE60, border_color=VERDE_FOSFO, selection_color=VERDE_FOSFO,
                            focused_border_color=VERDE_FOSFO, label_style=ft.TextStyle(color=VERDE_FOSFO, size=12)) for campo in UsuarioDB.model_fields]
        ]),
        #bgcolor=ft.colors.AMBER_50,
        border_radius=8,
        border=ft.border.all(2, color=ft.colors.WHITE38),
        width=300,
        height=650,
        padding=5,
        alignment=ft.alignment.center,
    )

    usuarios = ft.Container(
        ft.Column([
            ft.Container(
                ft.Row([
                    ft.Icon(ft.icons.PEOPLE, color=ft.colors.AMBER_50),
                    ft.Text('Usuarios', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE60)
                ],
            alignment=ft.MainAxisAlignment.CENTER),
            )            
            
        ]),
        #bgcolor=ft.colors.AMBER_50,
        border_radius=panel_control.border_radius,
        border=panel_control.border,
        width=panel_control.width,
        height=panel_control.height,
        padding=5,
        alignment=panel_control.alignment

    )

    container_principal = ft.Container(
        ft.Row([
            panel_control,
            usuarios
    ])
    )

    page.add(
        container_principal
    )

if __name__ == '__main__':
    ft.app(
        target=main,
        assets_dir="assets")