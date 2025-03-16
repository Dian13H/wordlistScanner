# Wordlist Scanner
Un wordlist scanner es una herramienta de escaneo diseñada para identificar recursos web ocultos utilizando listas de palabras (wordlists). Está pensada para facilitar tareas de enumeración y descubrimiento de directorios y archivos en aplicaciones web.

En este repositorio se encuentran scripts de python para hacer escaneo de wordlists.

## Archivos
- `buscarPalabra.py`: busca una palabra dentro de la página web
- `buscarWordlists.py`: busca las palabras dentro de un archivo (wordlist) dentro de una página web
- `UserPassCombo-Jay.txt`: archivo con wordlists de usuarios y contraseñas
- `top-usernames-shortlist.txt`: archivo con wordlist de nombres de usuarios
- `victima.html`: HTML de ejemplo para probar el escáner

### Wordlists
Puedes encontrar más wordlists en el siguiente repositorio:
https://github.com/gmelodie/awesome-wordlists

## Requisitos
- Python 3.x
- Requests

## Instalación y uso
1. Clona el repositorio:

```bash
git clone https://github.com/Dian13H/wordlistScanner.git
cd wordlistScanner
```

2. En una terminal levanta un servidor web:

```bash
python3 -m http.server
```
3. En otra terminal ejecuta el script que desees:

```bash
python3 buscarWordlists.py
```

## Contribuciones
Las contribuciones son bienvenidas. Si tienes mejoras o correcciones, por favor crea un pull request o abre un issue.
