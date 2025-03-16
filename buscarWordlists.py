import requests

def scan_url(target_url, word):
    """Escanea un sitio web buscando una palabra específica en las rutas."""
    full_url = f"{target_url.rstrip('/')}/{word}"
    
    try:
        response = requests.get(full_url, timeout=5)
        
        if response.status_code == 200:
            print(f"[+] Encontrado: {full_url} (Código {response.status_code})")
        elif response.status_code == 403:
            print(f"[-] Acceso denegado: {full_url} (Código {response.status_code})")
        elif response.status_code == 404:
            print(f"[!] No encontrado: {full_url} (Código {response.status_code})")
        else:
            print(f"[*] Estado desconocido: {full_url} (Código {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[X] Error al conectar con {full_url}: {e}")

def cargar_wordlist(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {archivo}")
        return []

# --- Parámetros del escaneo ---
TARGET_URL = "http://127.0.0.1:8000"  # cambiar por el sitio a escanear
WORDLIST_FILE = "top-usernames-shortlist.txt"  # archivo con la lista de palabras

# --- Ejecutar escaneo ---
wordlist = cargar_wordlist(WORDLIST_FILE)
if wordlist:
    print(f"Escaneando {TARGET_URL} con {len(wordlist)} palabras de {WORDLIST_FILE}...\n")
    for word in wordlist:
        scan_url(TARGET_URL, word)

