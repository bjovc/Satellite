- **download_netCDF_and_geoTiff**: código para la descarga de los netCDF agrupados por meses (ya que tienen dimensión temporal) y los geoTiff de cada día del año que cumple los requisitos (baja nubosidad).

- **get_clipping_and_png**: código para recortar los geoTiffs utilizando los recintos shapefile y obetener el geoTiff recortado así como una imagen PNG.

- **visualize_geotiffs**: archivo de prueba para visualizar geoTiffs y PNGs y ver si están bien. También se puede hacer en QGIS.

- **satelitedes**: archivo para borrar las nubes de las imágenes. NO SE UTILIZA ya que lo que hace es sacar el valor mínimo de los píxeles dentro de un netCDF (o mes), y se queda con una sola imagen para todo ese mes.

- **download_geoTiff_by_season**: código para descargar los netCDF según la estación del año. NO SE UTILIZA ya que mejor descargamos por mes en download_netCDF_and_geoTiff.

- **donwload_and_visualize_by_season**: código para descargar los netCDF según la estación del año y visualizarlos. NO SE UTILIZA ya que mejor descargamos por mes en download_netCDF_and_geoTiff.

All data used is stored [here](https://drive.google.com/drive/folders/1vavVD1FwBqZE2JTFReFWYtK4xu4lnI7Q?usp=sharing).
