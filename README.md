VeraSetas v3.6 — Indicador de confianza en la cobertura de datos.

En Predicción, a zoom 11+, cada cuadrícula muestra «Datos: Baja/Media». La ficha detalla meteorología, altitud y cartografía forestal. Se reserva Media para cuadrículas con datos meteorológicos completos, altitud y especies identificadas en polígonos MFE25 importados. Baja si falta alguna fuente o solo hay OSM. No se muestra Alta porque el índice no está validado con hallazgos reales.

No son probabilidades de presencia ni una medida estadística de precisión. Los datos MFE25 oficiales siguen sin estar incluidos en el paquete.


## v3.7 — Tamaño visual de cuadrícula
Selector Original / Mitad / Cuarto en Predicción. La subdivisión es solo visual y mantiene los datos meteorológicos de las 64 celdas regionales originales. No implica mayor resolución ni precisión.


## v3.8 — Preparación para terreno de mayor resolución

Se puede cargar un GeoJSON de puntos con `elevation` (metros) y opcionalmente `forest` (taxón/hábitat verificado) en cada centro de subcasilla. El mapa corrige la penalización de altitud y añade un ajuste experimental de bosque en casillas con datos. No sustituye los valores regionales de lluvia y temperatura.

El script `preparar_terreno.py` transforma un GeoTIFF MDT real (por ejemplo MDT05 del IGN) en `data/terreno_vegetacion.geojson`. Requiere `rasterio`, y no incluye los archivos oficiales descargados. No inventa la clasificación forestal.

**Limitación:** solo los centros de la subdivisión Cuarto coinciden con las 1024 muestras que genera el script; en Mitad no se aplica la corrección local. Seleccionar Cuarto tras cargar datos. Los datos MFE25 vectoriales oficiales siguen pendientes.


## v3.9: colores por especie vegetal
En Flora, cada especie identificada recibe un color propio en los polígonos OSM y en los polígonos GeoJSON importados, con leyenda y controles individuales. No se inventan especies para zonas sin datos. Los datos MFE25 oficiales siguen sin incluirse.
