import os
import geopandas as gpd
import matplotlib.pyplot as plt
from tqdm import tqdm


year = '2023'
#ruta_shapefile = f'shapefiles/tabuyo/tabuyo_{year}/tabuyo_{year}_fixed.shp'
ruta_shapefile = f'shapefiles/tabuyo/tabuyo_{year}/mini_tabuyo.shp'
carpeta_salida = f'datacubes/tabuyo/{year}/mask_testing'

if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

gdf = gpd.read_file(ruta_shapefile)

color_dict = { # Colores en el notion
    "MT": [0.690, 0.784, 0.153], # Matorral - VERDE
    "PA": [0.776, 0.251, 0.804], # Pasto con arbolado - ROSA
    "PR": [0.459, 0.365, 0.839], # Pasto arbustivo - MORADO
    "PS": [0.388, 0.859, 0.835], # Pastizal - AZUL
}

fig, ax = plt.subplots()
ax.axis('off')

total_iterations = len(gdf)
progress_bar = tqdm(total=total_iterations, desc="Procesando")

# Dibujar los poligonos en colores basados en el atributo 'uso_sigpac'
for index, row in gdf.iterrows():
    usage = row['uso_sigpac'] # USO_SIGPAC

    if usage in color_dict:
        color = color_dict[usage]
        gdf[gdf.index == index].plot(ax=ax, color=[color])

    progress_bar.update(1)
    
progress_bar.close()
nombre_imagen = f'mini_mascara_{year}.png'  
ruta_imagen = os.path.join(carpeta_salida, nombre_imagen)
plt.savefig(ruta_imagen, dpi=300, bbox_inches='tight', pad_inches=0) 

print(f'Imagen con la máscara guardada en {ruta_imagen}')
    