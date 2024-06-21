import folium

NAME = "map"
LOCATION = [35.6560680409,139.54404911776]
ZOOM = 15

map = folium.Map(LOCATION, zoom_start=ZOOM)
map.save(f'{NAME}.html')