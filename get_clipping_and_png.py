import os
import subprocess
import numpy as np
import rasterio
from rasterio.enums import Resampling
from rasterio.plot import reshape_as_image
import matplotlib.pyplot as plt

year = '2023'

#shapefile_path = f'shapefiles/tabuyo/tabuyo_{year}/tabuyo_{year}_fixed.shp'
shapefile_path = f'shapefiles/tabuyo/tabuyo_{year}/mini_tabuyo.shp'

tiff_dir = f'datacubes/tabuyo/{year}/mini'
tiff_list = [file for file in os.listdir(tiff_dir) if file.endswith('.tif')]

# Recorrer la lista
for i, tiff_file in enumerate(tiff_list):
    tiff_path = os.path.join(tiff_dir, tiff_file)
    print('tif: ', tiff_path)
    clipping_path = f"datacubes/tabuyo/{year}/masks/mini_v3/{tiff_file}"

    # Recorte del geoTiff con el shp
    comando = f'gdalwarp -cutline {shapefile_path} -crop_to_cutline -dstnodata None {tiff_path} {clipping_path}'

    try:
        subprocess.run(comando, check=True, shell=True)
        print(f'Recorte para {tiff_file} guardado en {clipping_path}')
        
        # Generacion del PNG
        png_name = tiff_file.replace('tif', 'png')
        png_path = f"datacubes/tabuyo/{year}/pngs/mini_v3/{png_name}"

        with rasterio.open(clipping_path) as src:
            data = src.read(
                out_shape=(src.count, int(src.height), int(src.width)),
                resampling=Resampling.bilinear
            )
            transform = src.transform
            normalized_data = np.interp(data, (data.min(), data.max()), (0, 255)).astype(np.uint8)

        with rasterio.open(png_path, 'w', driver='PNG', height=data.shape[1], width=data.shape[2], count=src.count, dtype=np.uint8) as dst:
            dst.write(normalized_data)


    except subprocess.CalledProcessError as e:
        print(f'Error al generar el recorte para {tiff_file}: {e}')

