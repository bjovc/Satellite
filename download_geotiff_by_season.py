import openeo

# Connection and authentication
con = openeo.connect("openeo.dataspace.copernicus.eu")
con.authenticate_oidc()

# Definition of the region 
spatial_extent = {"west": -6.25, "south": 42.27, "east": -6.16, "north": 42.36 ,"crs": "EPSG:4326",}
year = '2023'

# SPRING
temporal_extent = [year+"-03-01", year+"-05-31"]
datacube = con.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=temporal_extent,
    max_cloud_cover=10,
    bands=["B04", "B03", "B02"],
)

download_path = 'seasons/spring/sentinel2_' +year+ '_3-5.'
datacube.download(download_path+'nc')


# SUMMER
temporal_extent = [year+"-06-01", year+"-08-31"]
datacube = con.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=temporal_extent,
    max_cloud_cover=10,
    bands=["B04", "B03", "B02", "SCL"],
)
download_path = 'seasons/summer/sentinel2_' +year+ '_6-8.'
datacube.download(download_path+'nc')

# AUTUMN
temporal_extent = [year+"-09-01", year+"-11-30"]
datacube = con.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=temporal_extent,
    max_cloud_cover=10,
    bands=["B04", "B03", "B02", "SCL"],
)
download_path = 'seasons/autumn/sentinel2_' +year+ '_9-11.'
datacube.download(download_path+'nc')

# WINTER
#january - february
temporal_extent = [year+"-01-01", year+"-02-28"]
datacube = con.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=temporal_extent,
    max_cloud_cover=10,
    bands=["B04", "B03", "B02", "SCL"],
)
download_path = 'seasons/winter/sentinel2_' +year+ '_1-2.'
datacube.download(download_path+'nc')

# december
temporal_extent = [year+"-12-01", year+"-12-31"]
datacube = con.load_collection(
    "SENTINEL2_L2A",
    spatial_extent=spatial_extent,
    temporal_extent=temporal_extent,
    max_cloud_cover=10,
    bands=["B04", "B03", "B02", "SCL"],
)
download_path = 'seasons/winter/sentinel2_' +year+ '_12.'
datacube.download(download_path+'nc')
