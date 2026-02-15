# Cifrado César (alfabeto español)

Este proyecto implementa un cifrado César en Python usando alfabeto español con `ñ`.

## Características

- Cifra y descifra texto con desplazamiento (`ROT#`).
- Conserva mayúsculas y minúsculas.
- Mantiene espacios, números y símbolos sin cambios.
- Normaliza la clave para que funcione con cualquier entero (positivo o negativo).

## Requisitos

- Python 3.8 o superior

## Ejecución

```bash
python3 cesar.py
```

Al iniciar, se muestra un menú interactivo:

1. Cifrar texto
2. Descifrar texto
3. Salir

## Uso rápido

Ejemplo de cifrado:

- Texto: `Hola, mundo`
- Clave: `3`
- Resultado: `Krñd, oxpgr`

## Estructura

- `cesar.py`: lógica de cifrado/descifrado y menú de consola.
