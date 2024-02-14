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

import styles

class ButtonUserOptions(ft.UserControl):
    def __init__(self, icono:str, tooltip:'str', click_func:Callable) -> None:
        super().__init__()
        self.icono = icono
        self.tooltip = tooltip
        self.click_func = click_func
        self.height = 35
        self.width = 35
        self.color_fondo = ft.colors.WHITE12
        self.color_icono = ft.colors.WHITE
    
    def on_hover(self, e:ft.ControlEvent) -> None:
        """ Cambia el fondo a verde cuando se hace hover
        sobre un contenedro"""     
        if e.data == "true":
            e.control.bgcolor = styles.ACENTOS
            e.control.content.color = styles.COLOR_LETRAS_OSCURO
        else:
            e.control.bgcolor = ft.colors.WHITE12
            e.control.content.color = ft.colors.WHITE60
        e.control.update()

    def build(self) -> ft.Container:
        return ft.Container(ft.Icon(self.icono, 
                                color=self.color_icono), 
                                bgcolor=self.color_fondo, 
                                height=self.height,
                                width=self.width,
                                border_radius=8,
                                tooltip=self.tooltip, 
                                on_click=self.click_func,
                                on_hover=self.on_hover)