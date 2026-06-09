# -*- encoding: utf-8 -*-
'''
@File        :  main.py
@Time        :  2024/8/27 23:16:00
@Author      :  chen siyu
@Mail        :  chensy57@mail2.sysu.edu.cn
@Version     :  1.0
@Description :  section plot of marine scientific research
@envName     :  nc_cartopy(laptop); geoDraw(pc)
'''

import warnings
from glob import glob

import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.geoaxes import GeoAxes
from matplotlib.colors import LinearSegmentedColormap
from .param import *
from .utils import *


warnings.filterwarnings(
    'ignore', 
    message='facecolor will have no effect as it has been defined as "never".'
)
warnings.filterwarnings(
    'ignore', 
    message='The .ylabels_right attribute is deprecated. Please'
)
warnings.filterwarnings(
    'ignore', 
    message='The .xlabels_top attribute is deprecated. Please'
)


plt.rcParams['font.family'] = ['times new roman']   # 定义英文字体为新罗马
plt.rcParams["font.sans-serif"]=["SimHei"]          # 定义中文字体为宋体

def load_depth_ds(ncdir:str) -> np.array:
    """
        Description : load depth netCDF format dataset and mask land
        Input       : gebcco depth dataset directory
        output      : np arrat
    """
    ds         = xr.open_dataset(ncdir)
    depth      = ds['elevation'].values
    depth      = depth.astype(np.float32)
    ll_bbox    = [
        ds['lon'].values[0], 
        ds['lon'].values[-1], 
        ds['lat'].values[0], 
        ds['lat'].values[-1]]

    mask         = generate_land_mask(ll_bbox, depth.shape)      # 生成陆地掩膜
    depth[mask]  = np.nan

    return depth

def main():
    # 设置常量
    DPI = 1200                  # 分辨率
    SCATTER_SIZE = 15           # 散点大小
    SCATTER_LINEWIDTH = 0.5     # 散点线宽
    LL_BBOX = [100, 160, 0, 45] # 经纬度边界
    PROJ = ccrs.PlateCarree()   # 投影方式

    fig = plt.figure(dpi=DPI)
    
    ax:GeoAxes = fig.add_subplot(1,1,1,projection=PROJ)
    ax.set_extent(LL_BBOX,crs=ccrs.PlateCarree())       # 设置显示范围
    
    # 添加相关shp资料
    ax.coastlines(resolution='50m',linewidth=0.5, edgecolor='black',zorder=20)
    ax.add_feature(cfeat.BORDERS, linewidth=0.8, linestyle='-',zorder=20)
    ax.add_feature(cfeat.LAND, facecolor='gray', zorder=10)
    
    for _, value in shp_dir.items():
        shp_var = cfeat.ShapelyFeature(
            Reader(value['dir']).geometries(),
            PROJ,
        )
        ax.add_feature(
            shp_var, 
            facecolor = value["facecolor"],
            edgecolor = value["edgecolor"],
            linewidth = value["linewidth"],
            linestyle = value["linestyle"],
            zorder    = value["zorder"],
        )
        del _, value
    
    # # 添加深度数据并获取经纬度范围
    depth = load_depth_ds(gebcco_dir["SCS"])
    hill_shade = hillshade(-depth,315,45)

    # # 添加自定义color map
    # cmap = custom_cmap()
    cmap = LinearSegmentedColormap.from_list(
    "custom_bathy",
    [
        "#1D54A5",
        "#6DA4D4",
        "#B6DFF8",
        "#9DC3EA52",
        "#EFF3FF"
    ]
)

    # # 绘制深度图及深度梯度计算所得山体阴影
    cf = ax.imshow(
        depth,
        origin = 'lower',
        cmap = cmap,
        extent = LL_BBOX,
        transform = PROJ,
        vmin = -6000, vmax = 0,
        interpolation = 'nearest'
        )
    
    cd = ax.imshow(
        hill_shade,
        origin = 'lower',
        cmap = 'Greys_r',
        extent = LL_BBOX,
        transform = PROJ,
        alpha = 0.5,
        interpolation = 'nearest'
        )
    
    rect_scs = generate_rectangle([105,125,5,25], edgecolor="#D15A5A", zorder=30)
    rect_hc = generate_rectangle([140,152,32,40], edgecolor="#F49117", zorder=30)
    
    ax.add_patch(rect_scs)
    ax.add_patch(rect_hc)

    # 设定colorbar
    cbar = fig.colorbar(cf, 
        ax=ax, extend='both', 
        shrink=0.8, # colorbar长度，越小越短
        pad=0.05, 
        fraction=0.05,   # colorbar 宽度，越大越宽
        orientation='vertical', 
        boundaries=np.linspace(-6000, 0, 13))
    cbar.ax.set_xlabel('Depth (m)',fontsize=8, labelpad=12)
    cbar.ax.tick_params(labelsize=8)
    cbar.ax.yaxis.set_tick_params(labelsize=8)

    gl = ax.gridlines(crs=ccrs.PlateCarree(),
        draw_labels=True,
        linestyle='--',
        color='gray',
        linewidth=0.5,
        alpha=0.5,
        xlocs=np.arange(100,160,5),
        ylocs=np.arange(0,45,5)
        )
    ax._autoscaleXon = False
    ax._autoscaleYon = False
    gl.xlabels_top = False  
    gl.ylabels_right = False  
    gl.top_labels = False
    gl.right_labels = False
    gl.left_labels = True
    gl.bottom_labels = True
    gl.xlabel_style = {'size': 8, 'color': 'black'}
    gl.ylabel_style = {'size': 8, 'color': 'black'}

    plt.savefig("marineRsearch.png", dpi=DPI, bbox_inches='tight')

if __name__ == "__main__":
    main()