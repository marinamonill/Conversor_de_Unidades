# conversor_unidades

Librería de Python para la conversión de unidades básicas: longitud, temperatura y masa. Desarrollada como parte del módulo Arquitectura de software y Control de versiones del máster de Evolve.

---

## ✅ Funcionalidad

Este módulo permite convertir unidades en tres categorías:

- **Longitud**: metros ↔ kilómetros, pulgadas ↔ centímetros
- **Temperatura**: grados Celsius ↔ Fahrenheit
- **Masa**: gramos ↔ kilogramos

---

## 📦 Instalación

1. Clonar el repositorio o descarga el proyecto.
2. Activar el entorno virtual.
3. Desde la raíz del proyecto, ejecutar:

```bash
pip install -e .
```

---

## 🚀 Uso

Se pueden importar las funciones directamente desde el módulo principal:

```python
from conversor_unidades import (
    metros_a_kilometros,
    pulgadas_a_centimetros,
    celsius_a_fahrenheit,
    gramos_a_kilogramos
)

print(metros_a_kilometros(1500))        # 1.5
print(pulgadas_a_centimetros(10))       # 25.4
print(celsius_a_fahrenheit(0))          # 32.0
print(gramos_a_kilogramos(1000))        # 1.0
```

También es posible ejecutar una demo desde el archivo `scripts/main.py`:

```bash
python scripts/main.py
```

---

## 📁 Estructura del Proyecto

```
conversor_unidades/
├── src/
│   └── proyecto_conversion/
│       ├── __init__.py
│       ├── longitud.py
│       ├── masa.py
│       └── temperatura.py
├── scripts/
│   └── main.py
├── data/                 
├── setup.py
├── requirements.txt
└── README.md
```

---

## 📚 Requisitos

- Python 3.7 o superior

---
