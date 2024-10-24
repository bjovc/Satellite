import os
from osgeo import gdal

def change_crs(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Find all GeoTIFF files in input folder and its subfolders
    tif_files = []
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.tif'):
                tif_files.append(os.path.join(root, file))

    # Loop through each GeoTIFF file
    for tif_file in tif_files:
        # Define output file path
        output_file = os.path.join(output_folder, os.path.relpath(tif_file, input_folder))

        # Ensure output directory exists
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Perform CRS transformation using gdalwarp
        gdal.Warp(output_file, tif_file, dstSRS='EPSG:4326')

        print(f"Transformed {tif_file} to EPSG:4326 and saved to {output_file}")

# Example usage
input_folder = 'datacubes/tabuyo/2023/mini_tiffs'
output_folder = 'datacubes/tabuyo/2023/a'

change_crs(input_folder, output_folder)
