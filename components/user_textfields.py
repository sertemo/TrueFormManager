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
import styles

class UserTextField(ft.UserControl):
    def __init__(self, campo:str) -> None:
        super().__init__()
        self.campo = campo

    def build(self):
        self.value = ft.Text("Hola")
        return ft.TextField(label=self.campo, height=26, text_size=15, 
                            content_padding=ft.padding.only(left=10),
                            cursor_color=styles.ACENTOS,
                            filled=False, color=ft.colors.WHITE, 
                            border_color=styles.ACENTOS, selection_color=styles.ACENTOS,
                            focused_border_color=styles.ACENTOS, 
                            label_style=ft.TextStyle(color=styles.ACENTOS, size=12),
                            value=self.value)

nombre = ft.TextField(label='nombre', **styles.TEXTFIELD_PARAMS)
email = ft.TextField(label='email', **styles.TEXTFIELD_PARAMS)
telefono = ft.TextField(label='telefono', **styles.TEXTFIELD_PARAMS)
clave = ft.TextField(label='clave', **styles.TEXTFIELD_PARAMS)
apikey = ft.TextField(label='apikey', **styles.TEXTFIELD_PARAMS)
model = ft.TextField(label='model', **styles.TEXTFIELD_PARAMS)
fecha_alta = ft.TextField(label='fecha_alta', **styles.TEXTFIELD_PARAMS)
activo = ft.TextField(label='activo', **styles.TEXTFIELD_PARAMS)
admin = ft.TextField(label='admin', **styles.TEXTFIELD_PARAMS)
ultimo_uso = ft.TextField(label='ultimo_uso', **styles.TEXTFIELD_PARAMS)
ultimo_coste = ft.TextField(label='ultimo_coste', **styles.TEXTFIELD_PARAMS)
ultimo_palabras = ft.TextField(label='ultimo_palabras', **styles.TEXTFIELD_PARAMS)
palabras_limite = ft.TextField(label='palabras_limite', **styles.TEXTFIELD_PARAMS)
palabras_acumulado = ft.TextField(label='palabras_acumulado', **styles.TEXTFIELD_PARAMS)
facturado_acumulado = ft.TextField(label='facturado_acumulado', **styles.TEXTFIELD_PARAMS)
coste_acumulado = ft.TextField(label='coste_acumulado', **styles.TEXTFIELD_PARAMS)
ultimo_text_traducido = ft.TextField(label='ultimo_text_traducido', **styles.TEXTFIELD_PARAMS)

user_textfield_list = [nombre, email, telefono, clave,
                        apikey, model, fecha_alta, activo,
                        admin, ultimo_uso, ultimo_coste, ultimo_palabras,
                        palabras_limite, palabras_acumulado, facturado_acumulado,
                        coste_acumulado, ultimo_text_traducido]
