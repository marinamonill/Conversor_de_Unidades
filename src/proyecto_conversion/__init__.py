"""
Módulo de interfaz principal del conversor de unidades.
Permite acceder desde un único lugar a las funciones de longitud, temperatura y masa.
"""

from .longitud import metros_a_kilometros, pulgadas_a_centimetros
from .temperatura import celsius_a_fahrenheit
from .masa import gramos_a_kilogramos

__all__ = [
    "metros_a_kilometros",
    "pulgadas_a_centimetros",
    "celsius_a_fahrenheit",
    "gramos_a_kilogramos"
]
