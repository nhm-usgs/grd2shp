import gridmet_cfsv2 as gm
import grd2shp
import geopandas as gpd


gm_vars = ['air_temperature',
           'air_temperature',
           'precipitation_amount',
           'wind_speed',
           'surface_downwelling_shortwave_flux_in_air',
           'specific_humidity']
m = gm.Gridmet(type=0)
ds1 = m.tmax
ds2 = m.tmin
ds3 = m.prcp
ds4 = m.wind_speed
ds5 = m.srad
ds6 = m.specific_humidity
# print(ds.head(), ds['air_temperature'].long_name)
# ds1 = xr.open_dataset('C:/Users/rmcd/.gridmet/cfsv2_metdata_forecast_tmmx_daily_median.nc')
# ds2 = xr.open_dataset(r'C:/Users/rmcd/.gridmet/cfsv2_metdata_forecast_tmmn_daily_median.nc')
gdf = gpd.read_file(r'C:/Users/rmcd/OneDrive - DOI/GitRepos/onhm-fetcher-parser/Data_v1_1/GFv1.1_simple.shp')
g2 = grd2shp.Grd2Shp()
# print(g2.initialize.__annotations__)
# ds2 = 0
pin = g2.initialize(
    grd=[ds1, ds2, ds3, ds4, ds5, ds6],
    calctype=0,
    shp=gdf,
    wght_file=r'C:/Users/rmcd/OneDrive - DOI/GitRepos/onhm-fetcher-parser/Data_v1_1/' +
              'tmp_Gridmet_weights_hru_v1_1e_test.csv',
    time_var='day',
    lat_var='lat',
    lon_var='lon',
    var=gm_vars,
    var_output=['tmax', 'tmin', 'prcp', 'ws', 'srad', 'shum'],
    opath=r'D:/gitNHM/grd2shp/notebook',
    fileprefix='test_'
)

numts = g2.num_timesteps
print(numts)
for i in range(1):
    g2.run_weights()

g2.write_file(elev_file=r'D:\gitNHM\grd2shp\notebook\package.gpkg', punits=1)
