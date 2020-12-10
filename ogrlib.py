from osgeo import ogr
import os

shapefile = r"C:\Users\4SM-001\Desktop\Natural_Earth_quick_start\10m_cultural\ne_10m_populated_places.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()
layer.SetSpatialFilterRect(-102, 26, -94, 36)
for feature in layer:
    if feature.GetField("ADM0NAME") != "United States of America":
        continue
    else:
        print(feature.GetField("NAME"))