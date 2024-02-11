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

from datetime import datetime
import pytz

def get_datetime_formatted()-> str:
    """Devuelve la fecha actual formateada en str como:
    %d-%m-%Y %H:%M:%S

    Returns
    -------
    str
        _description_
    """
    return datetime.strftime(datetime.now(tz=pytz.timezone('Europe/Madrid')), format="%d-%m-%Y %H:%M:%S")