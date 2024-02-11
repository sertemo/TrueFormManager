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

from pydantic import BaseModel, Field

from utils import get_datetime_formatted

class UsuarioDB(BaseModel):
    nombre:str
    email:str
    telefono:str
    clave:str
    apikey:str
    model:str = 'gpt-3.5-turbo'
    fecha_alta:str = Field(default_factory=get_datetime_formatted)
    activo:bool = True
    admin:bool = False       
    ultimo_uso:str = '' # fecha de última traducciójn
    ultimo_coste:float = 0 # coste de la última traducción
    ultimo_palabras:int = 0 # palabras del ultimo documento traducido
    palabras_limite:int # num max de palabras contratadas
    palabras_acumulado:int = 0 # palabras traducidas hasta la fecha
    facturado_accumulado:float # importe facturado hasta la fecha a este usuario
    coste_acumulado:float = 0 # coste acumulado hasta la fecha por este usuario
    ultimo_text_traducido:str = '' # checkpoint que se van guardando del texto traducido por seguridad