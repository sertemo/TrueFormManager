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
from typing import Callable

import flet as ft
from db.models import UserDB
import styles

class UserInfo(ft.UserControl):
    def __init__(self, user:UserDB, click_func:Callable) -> None:
        super().__init__()
        self.user = user
        self.click_func = click_func
        self.key = user.clave

    @staticmethod
    def on_hover(e:ft.ControlEvent) -> None:        
        if e.data == "true":
            e.control.bgcolor = styles.ACENTOS
            e.control.content.controls[0].color = styles.COLOR_LETRAS_OSCURO
        else:
            e.control.bgcolor = ft.colors.WHITE12
            e.control.content.controls[0].color = ft.colors.WHITE60
        e.control.update()

    def build(self) -> ft.Container:
        return ft.Container(
            ft.Row([
                ft.Text(self.user.nombre, size=15, color=ft.colors.WHITE60),
                ft.Row([
                    ft.Text(f'{self.user.palabras_acumulado:,}', size=10, color=ft.colors.GREY_500),
                    ft.Text('/', size=10, color=ft.colors.GREY_500),
                    ft.Text(f'{self.user.palabras_limite:,}', size=10, color=ft.colors.GREY_500)
                ],
                spacing=1)                
            ]),
            key=self.key,
            bgcolor=ft.colors.WHITE12,
            border_radius=styles.BORDER_RADIUS,
            padding=5,
            on_hover=self.on_hover,
            on_click=self.click_func
        )

