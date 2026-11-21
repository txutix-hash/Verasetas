#!/usr/bin/env python3
"""Muestrea un MDT GeoTIFF/COG oficial y produce puntos para subcasillas VeraSetas.
Dependencias: pip install rasterio pyproj. Entrada debe tener CRS válido.
Uso: python preparar_terreno.py MDT05.tif data/terreno_vegetacion.geojson
El campo forest se deja sin asignar hasta incorporar cartografía vectorial validada.
"""
import sys,json,math
from pathlib import Path
try:
 import rasterio
 from rasterio.warp import transform
except ImportError:
 sys.exit('Instala rasterio: pip install rasterio')
if len(sys.argv)!=3:sys.exit('Uso: python preparar_terreno.py MDT05.tif salida.geojson')
features=[]
with rasterio.open(sys.argv[1]) as ds:
 if ds.crs is None:sys.exit('El raster carece de CRS; no se puede georreferenciar')
 for i in range(8):
  for j in range(8):
   south=39.42+i*(40.20-39.42)/8;west=-6.43+j*(-5.34+6.43)/8
   for y in range(4):
    for x in range(4):
     lat=south+(y+.5)*(40.20-39.42)/32;lon=west+(x+.5)*(-5.34+6.43)/32
     xs,ys=transform('EPSG:4326',ds.crs,[lon],[lat]);v=next(ds.sample([(xs[0],ys[0])]))[0]
     if not math.isfinite(float(v)) or (ds.nodata is not None and float(v)==ds.nodata):continue
     features.append({'type':'Feature','geometry':{'type':'Point','coordinates':[round(lon,7),round(lat,7)]},'properties':{'elevation':round(float(v),1),'source':'MDT importado (verificar procedencia)'}})
Path(sys.argv[2]).parent.mkdir(parents=True,exist_ok=True)
Path(sys.argv[2]).write_text(json.dumps({'type':'FeatureCollection','features':features},ensure_ascii=False))
print('Puntos MDT válidos:',len(features))
