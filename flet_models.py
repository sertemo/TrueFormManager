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
from models import UserDB

class UserInfo(ft.UserControl):
    def __init__(self, user:UserDB) -> None:
        super().__init__()
        self.username = user.nombre

    @staticmethod
    def on_hover(e:ft.ControlEvent) -> None:
        e.control.bgcolor = '#a5de37' if e.data == "true" else ft.colors.WHITE12
        e.control.content.controls[0].color = '#5b6060' if e.data == "true" else ft.colors.WHITE60
        e.control.update()

    def build(self) -> ft.Container:
        return ft.Container(
            ft.Row([
                ft.Text(self.username, size=15, color=ft.colors.WHITE60)
            ]),
            bgcolor=ft.colors.WHITE12,
            border_radius=3,
            padding=5,
            on_hover=self.on_hover,
            #on_click=""
        )

    
