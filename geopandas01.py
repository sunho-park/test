import geopandas as gpd
#df = gpd.read_file(r'C:\Users\4SM-001\Desktop\Natural_Earth_quick_start\10m_cultural\ne_10m_admin_0_boundary_lines_land.shp')
df = gpd.read_file(r"C:\Users\4SM-001\Desktop\Natural_Earth_quick_start\10m_cultural\ne_10m_admin_0_boundary_lines_disputed_areas.shp")
print(df.head())