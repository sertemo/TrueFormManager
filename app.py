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

from dotenv import load_dotenv
import flet as ft

from db.handler import UserDBHandler
from components.user_info import UserInfo
from components.user_textfields import user_textfield_list
from components.user_option_button import ButtonUserOptions
from db.models import UserDB
from db.settings import COLLECTION_USUARIOS
import styles

TITLE = 'TrueForm Manager'
CAMPOS_BLOQUEADOS = ['fecha_alta', 'ultimo_uso', 'ultimo_coste',
                        'ultimo_palabras', 'palabras_acumulado', 'facturado_acumulado',
                        'coste_acumulado', 'ultimo_text_traducido']

# Cargamos variables de entorno
load_dotenv()

db_handler = UserDBHandler(COLLECTION_USUARIOS)

def main(page:ft.Page) -> None:
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    page.title = TITLE
    page.theme = ft.Theme(font_family="RobotoSlab")
    page.bgcolor = styles.COLOR_FONDO_GENERAL
    page.window_width = 1000
    page.window_height = 850
    page.window_resizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TRANSLATE, color=ft.colors.AMBER_50),
        #leading_width=180,
        title=ft.Row([
            ft.Text(TITLE.split()[0], weight=ft.FontWeight.BOLD, color=ft.colors.WHITE30),
            ft.Text(TITLE.split()[1], weight=ft.FontWeight.BOLD, color=styles.ACENTOS)
        ]),
        bgcolor=styles.COLOR_FONDO_GENERAL,
        toolbar_height=60,
        center_title=True,        
    )

    def poblar_listview_usuarios(listview:ft.ListView, handler:UserDBHandler) -> ft.ListView:
        """Puebla una listview con elementos de una base de datos
        y la devuelve

        Parameters
        ----------
        listview : ft.ListView
            _description_
        handler : UserDBHandler
            _description_

        Returns
        -------
        ft.ListView
            _description_
        """
        for user in handler:
            listview.controls.append(UserInfo(user, load_user_info))    
        return listview

    def load_user_info(e:ft.ControlEvent) -> None:
        """Carga la información de un usuario en los textfields"""    
        # Sacamos la clave (campo único de quien se haya hecho click)
        clave_user = e.control.key
        # Sacamos todos los campos de ese usuario
        user_dict = db_handler.find_one('clave', clave_user)
        # Lo pasamos por UserDb para que saque los campos en el mismo orden
        userdb = UserDB(**user_dict)
        user_dict_ordered = userdb.model_dump()
        # Iteramos para rellenar los campos
        for campo, user_info in zip(user_textfield_list, user_dict_ordered.values()):
            campo.value = user_info
            if campo.label in CAMPOS_BLOQUEADOS:
                campo.disabled = True
            campo.update()

    def limpiar_campos(e:ft.ControlEvent) -> None:
        for campo in user_textfield_list:
            campo.value = ""
            campo.disabled = False
            campo.update()

    #TODO
    def añadir_usuario():
        # TODO Comprobar si existe el email en db
        # TODO Comprobar si exsite la clave en db
        # TODO Comprobar campos vacíos
        # TODO Pasarle a Userdb solo los campos requeridos
        pass



    def eliminar_usuario():
        pass

    panel_control = ft.Container(
        ft.Column([
            ft.Container(
                ft.Row([
                    ft.Icon(ft.icons.MANAGE_ACCOUNTS, color=ft.colors.AMBER_50),
                    ft.Text('Panel de Control', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE60)
                ],
            alignment=ft.MainAxisAlignment.CENTER),
            ),
            ft.Row([
                ButtonUserOptions(ft.icons.DELETE, 'Resetear campos', limpiar_campos),
                ButtonUserOptions(ft.icons.PERSON_ADD_ALT, 'Añadir usuario', None),
                ButtonUserOptions(ft.icons.PERSON_REMOVE_ROUNDED, 'Eliminar usuario', None),
                ButtonUserOptions(ft.icons.UPDATE, 'Modificar campos', None),
            ]),
            *user_textfield_list

        ]),
        #bgcolor=ft.colors.AMBER_50,
        border_radius=8,
        border=ft.border.all(2, color=ft.colors.WHITE38),
        width=300,
        height=700,
        padding=5,
        alignment=ft.alignment.center_right,
    )
    listview_usuarios = ft.ListView(
        height=panel_control.height,
        width=panel_control.width,
        spacing=5
    )

    usuarios = ft.Container(
        ft.Column([
            ft.Container(
                ft.Row([
                    ft.Icon(ft.icons.PEOPLE, color=ft.colors.AMBER_50),
                    ft.Text('Usuarios', weight=ft.FontWeight.BOLD, color=ft.colors.WHITE60)
                ],
            alignment=ft.MainAxisAlignment.CENTER),
            ),
            ft.Container(
                poblar_listview_usuarios(listview_usuarios, db_handler),
            )
            
        ]),
        #bgcolor=ft.colors.AMBER_50,
        border_radius=panel_control.border_radius,
        border=panel_control.border,
        width=panel_control.width,
        height=panel_control.height // 2,
        padding=5,
        alignment=panel_control.alignment
    )

    container_principal = ft.Container(
        ft.Row([
            panel_control,
            usuarios
    ],
    ),
    )

    page.add(
        container_principal
    )

if __name__ == '__main__':
    ft.app(
        target=main,
        assets_dir="assets")