# 研究区域及原位观测站点图

本程序基于gebco高程数据以及原位观测数据的经纬度坐标npy数组，生成研究区域及原位观测站点图。程序可以在指定的经纬度范围内，使用Python的Cartopy和Matplotlib库绘制包含地形、水深、行政边界等元素的站点分布图。

## 运行环境

- Python 3.8+
- 依赖包：numpy, pandas, matplotlib, cartopy, xarray

## 使用方法

1. 1）gebco数据，下载网址：https://www.gebco.net/data-products/gridded-bathymetry-data：
   2）原位观测数据npy文件，内部存放原位观测点位经纬度信息
   eg: [[lon1,lat1],[lon2,lat 2].......]

2. 安装依赖包
```bash 
pip install numpy pandas matplotlib cartopy xarray
```

3. 运行程序
```bash
python app.py
```

4. 程序将读取nc和npy文件，并在经纬度范围为\[105°E-125°E, 5°N-25°N\]的南海区域内绘制站点分布图。生成的图片文件名为`marineRsearch.png`，存储在程序所在目录下。

## 程序结构

- `app.py`: 主程序文件，负责数据读取、图形绘制和文件输出。
- `param.py`: 参数文件，定义了程序使用的文件路径、Shapefile数据和深度数据信息。
- `utils.py`: 工具函数文件，包括自定义colormap、山体阴影计算、陆地掩膜生成等函数。

## 主要功能

1. 读取站点npy文件。
2. 使用Cartopy库绘制南海区域的地图，包括海岸线、行政边界、断层带和河流等地理信息。 
3. 加载GEBCO 2026全球地形数据，并使用自定义colormap绘制水深信息。
4. 计算山体阴影，并将其叠加在水深图层之上，以突出地形特征。
5. 使用Matplotlib的散点图绘制站点位置，并使用legend标注站点名称。
6. 在图片周围添加经纬度网格，便于定位站点。
7. 将生成的图片保存为高分辨率（1200 DPI）的PNG格式文件。

## 注意事项

1. npy模板文件的格式和列名需与程序预期一致，否则可能导致读取错误。
2. Shapefile和全球地形数据需提前准备好，并将路径正确设置在`param.py`文件中。
3. 程序生成的图片文件可能较大，请确保磁盘空间充足。
4. 如需调整图片的样式和布局，可以修改`main.py`中的相关参数，如字体大小、散点大小、配色方案等。

