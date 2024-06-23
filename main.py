import numpy as np
from stl import mesh

import folium
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui.ui_Monitor import Ui_MainWindow


class Monitor(QMainWindow, Ui_MainWindow):

    MAP_HTML = "./map/UEC.html"
    ICON_SVG = "./map/airplane.svg"
    STL_FILE = "./stl/Rocket.stl"

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_map(self.MAP_HTML)
        self.set_stl(self.STL_FILE)
        self.set_axis()
        
    def set_map(self, map_html):
        self.map_view.setHtml(open(map_html).read())
    
    def set_icon(self, icon_file):
        self.map_view.iconUrl(QUrl(icon_file))
    
    def set_stl(self, stl_file):
        model = self.load_stl(stl_file)
        self.obj_view.addItem(model)
        self.obj_view.setBackgroundColor('black')
        self.obj_view.setCameraPosition(distance=300, elevation=45)
    
    def set_axis(self):
        axis = gl.GLAxisItem(
            size=QVector3D(400, 400, 400),
            antialias=True
        )
        self.obj_view.addItem(axis)
      
    def load_stl(self, stl_file):
        stl_mesh = mesh.Mesh.from_file(stl_file)
        vertices = np.array(stl_mesh.vectors, dtype=np.float32)
        faces = np.arange(vertices.shape[0] * 3, dtype=np.uint32).reshape(vertices.shape[0], 3)
        model = gl.GLMeshItem(vertexes=vertices.reshape(-1, 3), faces=faces, smooth=False, color=(1, 1, 1, 1), shader="shaded")
        return model
      
if __name__ == '__main__':
    from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)
    app = QApplication([])
    window = Monitor()
    window.show()
    app.exec()
