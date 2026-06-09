# -*- encoding: utf-8 -*-
'''
@File        :  param.py
@Time        :  2026/9/6 23:16:00
@Author      :  chen siyu & Su changwei
@Mail        :  chensy57@mail2.sysu.edu.cn 
@Mail        :  suchw5@mail2.sysu.edu.cn
@Version     :  2.0
@Description :  parameter
@envName     :  nc_cartopy(laptop); geoDraw(pc)
'''

table_dir:str = r"assets/*.xlsx"

shp_dir:dict = {
    # "city"      : {
    #     "dir"       : r"C:/Users/sysu/Desktop/section_autoPlot-main/assets/shp/City/CN_city.shp",
    #     "facecolor" : 'none',
    #     "edgecolor" : 'black',
    #     "linewidth" : 0.1,
    #     "linestyle" : '--',
    #     "zorder"    : 20
    # },
    # "river3"    : {
    #     "dir"       : r"C:/Users/sysu/Desktop/section_autoPlot-main/assets/shp/R3/hyd2_4p.shp",
    #     "facecolor" : 'none',
    #     "edgecolor" : 'black',
    #     "linewidth" : 0.1,
    #     "linestyle" : '--',
    #     "zorder"    : 20
    #     },
    # "river5"    : {
    #     "dir"       : r"C:/Users/sysu/Desktop/section_autoPlot-main/assets/shp/R5/River5_polyline.shp",
    #     "facecolor" : None,
    #     "edgecolor" : None,
    #     "linewidth" : 1,
    #     "linestyle" : '-',
    #     "zorder"    : 20
    #     },
    "nineline"  : {
        "dir"       : r"C:/Users/sysu/Desktop/section_autoPlot-main/assets/shp/SouthSea/nineline.shp",
        "facecolor" : None,
        "edgecolor" : 'orange',
        "linewidth" : 1.8,
        "linestyle" : '-',
        "zorder"    : 20
        },
    # "islands"   : {
    #     "dir"       : r"C:/Users/sysu/Desktop/section_autoPlot-main/assets/shp/SouthSea/islands.shp",
    #     "facecolor" : None,
    #     "edgecolor" : 'black',
    #     "linewidth" : 0.01,
    #     "linestyle" : '-',
    #     "zorder"    : 20
    #     },
    # "bou2_4l"   : {
    #     "dir"       : r"assets/shp/SouthSea/bou2_4l.shp",
    #     "facecolor" : None,
    #     "edgecolor" : 'black',
    #     "linewidth" : 1,
    #     "linestyle" : '-',
    #     "zorder"    : 20
    #     },
    # "zhujiang"  : {
    #     "dir"       : r"C:/Users/sysu/Desktop/section_autoPlot-main/assets/shp/SouthSea/zhujiang.shp",
    #     "facecolor" : 'blue',
    #     "edgecolor" : 'darkblue',
    #     "linewidth" : 1,
    #     "linestyle" : '-',
    #     "zorder"    : 20
    #     }
}

gebcco_dir:dict = {
    "SCS":r"D:/soft/matlab/matlab_work/SCS_research_region_plot/gebco_2026_n45.0_s0.0_w100.0_e160.0.nc"
}

coords_dir:dict = {
    "HC_drift":r"C:/Users/sysu/Desktop/section_autoPlot-main/lat_lon_coords/drift_32_40_140_152.npy",
    "HC_ship":r"C:/Users/sysu/Desktop/section_autoPlot-main/lat_lon_coords/ship_base_32_40_140_152.npy",
    "SCS_ship":r"C:/Users/sysu/Desktop/section_autoPlot-main/lat_lon_coords/ship_base_5_25_105_125.npy"

}

