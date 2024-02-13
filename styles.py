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
import flet as ft

COLOR_FONDO_GENERAL = '#5b6060'
ACENTOS = '#a5de37'
COLOR_LETRAS_OSCURO = '#5b6060'
BORDER_RADIUS = 3
TEXTFIELD_PARAMS = {
    'height': 26, 'text_size': 15, 
    'content_padding': ft.padding.only(left=10),
    'cursor_color': ACENTOS,
    'filled': False, 'color': ft.colors.WHITE, 
    'border_color': ACENTOS, 'selection_color': ACENTOS,
    'focused_border_color': ACENTOS, 
    'label_style': ft.TextStyle(color=ACENTOS, size=12)
}