# mc-spotify-covers

Convierte texturas de Minecraft (32×32) en portadas nítidas para playlists de Spotify.

Los sitios de resize online mezclan los colores vecinos y la imagen queda borrosa. Este script usa **vecino más cercano (nearest neighbor)**: cada píxel se agranda sin mezclar nada, y el resultado se ve como Minecraft de verdad.

## Requisitos

- Python 3.9 o superior
- Pillow

```bash
python -m pip install pillow
```

## Estructura

```
mc-spotify-covers/
├── escalar_bloques.py
├── MCTexturePack/             <- texturas a escalar
└── MCTexturePackEscaladas/    <- resultado (lo crea el script)
```

## Uso

1. Pon tus texturas en la carpeta `MCTexturePack`.
2. Ejecuta:

```bash
python escalar_bloques.py
```

3. Las imágenes escaladas (640×640, mismos nombres) quedan en `MCTexturePackEscaladas`.

**¿Quieres usar tu propio texture pack?** Reemplaza el contenido de `MCTexturePack` con tus texturas y vuelve a ejecutar el script.

## Notas

- Spotify pide mínimo 300×300 px y máximo 4 MB. Las imágenes de salida cumplen ambos requisitos.
- Si una textura es animada (una tira vertical), el script toma el primer fotograma.
- Las portadas y texturas de ejemplo usan el pack de [@MultiPixelHD](https://x.com/MultiPixelHD) y las texturas originales pertenecen a Mojang Studios.
