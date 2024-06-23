from datetime import datetime
import folium


class Map:


    def __init__(self, name, location, zoom):
        self.name = name
        self.location = location
        self.zoom = zoom
        self.map = folium.Map(self.location, zoom_start=self.zoom)
        self.map.save(f'{self.name}.html')
        
    def save_map(self,index):
        dt = datetime.now()
        self.map.save(f'{dt.year}_{dt.month}_{dt.day}_{dt.hour}_{index}.html')