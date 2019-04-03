import pandas as pd
import numpy as np
from convert import to_latlon


data_1900 = pd.read_excel("../../Data/race1900_TableToExcel.xls")
data_1907 = pd.read_excel("../../Data/race1907_TableToExcel.xls")
data_1908 = pd.read_excel("../../Data/race1908_TableToExcel.xls")
data_1915 = pd.read_excel("../../Data/race1915_TableToExcel.xls")
data_1917 = pd.read_excel("../../Data/race1917_TableToExcel.xls")

data_list = [data_1900, data_1907, data_1908, data_1915, data_1917]
yr_list = ['1900', '1907', '1908', '1915', '1917']

lat_lons = {'Name': [], 'Latitude': [], 'Longitude': [], 'Street Address': []}
for year in range(0, len(yr_list)):
    for i in range(0, len(data_list[year].index)):
        x_spcs = (data_list[year].X.tolist())
        y_spcs = (data_list[year].Y.tolist())
        st_addr = (data_list[year].StAddr.tolist())
        name = (data_list[year][('GISvalueonly$.name'+yr_list[year])].tolist())

    for i in range(0, len(x_spcs)):
        x_spcs[i], y_spcs[i] = to_latlon(x_spcs[i], y_spcs[i])

    for i in range(0, len(x_spcs)):
        lat_lons['Name'].append(name[i])
        lat_lons['Latitude'].append(x_spcs[i])
        lat_lons['Longitude'].append(y_spcs[i])
        lat_lons['Street Address'].append(st_addr[i])

    df_name = yr_list[year]+'_df'
    df_name = pd.DataFrame(data=lat_lons)
    df_name.to_csv((yr_list[year]+'.csv'), index=False)
