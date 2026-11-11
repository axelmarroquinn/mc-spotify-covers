# escalar_bloques.py
# Requisito: python -m pip install pillow
# Uso: python escalar_bloques.py                      -> procesa .\MCTexturePack
#      python escalar_bloques.py "C:\ruta\carpeta"    -> procesa otra carpeta

import sys
from pathlib import Path
from PIL import Image

TAMANO = 640                      # Lado final en px (múltiplo entero de 32 -> x20, píxeles uniformes)
EXTENSIONES = {".png", ".jpg", ".jpeg", ".webp"}

# Entrada: argumento de consola o carpeta "MCTexturePack" junto al script
entrada = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "MCTexturePack"

# Salida: carpeta hermana con el mismo nombre + "Escaladas" (MCTexturePack -> MCTexturePackEscaladas)
salida = entrada.parent / f"{entrada.name}Escaladas"
salida.mkdir(exist_ok=True)

for archivo in sorted(entrada.iterdir()):
    if not archivo.is_file() or archivo.suffix.lower() not in EXTENSIONES:
        continue

    try:
        img = Image.open(archivo).convert("RGBA")

        # Si la textura es una tira animada (alto > ancho), se recorta el primer fotograma cuadrado
        if img.height > img.width:
            img = img.crop((0, 0, img.width, img.width))

        # Fondo negro opaco: Spotify rellena la transparencia con negro de todos modos
        fondo = Image.new("RGBA", img.size, (0, 0, 0, 255))
        fondo.alpha_composite(img)

        # NEAREST = vecino más cercano: cada píxel se agranda sin mezclar colores (sin borrosidad)
        resultado = fondo.convert("RGB").resize((TAMANO, TAMANO), Image.NEAREST)

        # Se guarda como PNG (sin pérdida) conservando el nombre original
        resultado.save(salida / f"{archivo.stem}.png")
        print(f"OK  {archivo.name} -> {TAMANO}x{TAMANO}")

    except Exception as e:
        # Un archivo con problemas no detiene el resto del lote
        print(f"ERROR {archivo.name}: {e}")

print(f"\nListo. Resultados en: {salida}")