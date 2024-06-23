import sys
import folium
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage

# 現在地の座標（初期値）
latitude = 35.681236  # 東京駅の緯度
longitude = 139.767125  # 東京駅の経度

# foliumの地図を作成する関数
def create_map(lat, lon):
    fmap = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], tooltip='Current Location').add_to(fmap)
    return fmap

# foliumの地図をHTMLファイルに保存する関数
def save_map(fmap, file_name):
    fmap.save(file_name)

# PyQtのメインウィンドウ
class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folium Map with PyQt")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

        self.map_file = "map.html"
        self.update_map(latitude, longitude)

        # タイマーを設定して位置情報を定期的に更新
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(5000)  # 5秒ごとに更新

    def update_map(self, lat, lon):
        fmap = create_map(lat, lon)
        save_map(fmap, self.map_file)
        self.web_view.setUrl(QUrl.fromLocalFile(self.map_file))

    def update_position(self):
        global latitude, longitude
        # ダミーの位置更新ロジック（実際のアプリケーションではGPSやAPIから取得）
        latitude += 0.0001
        longitude += 0.0001
        self.update_map(latitude, longitude)

# アプリケーションのエントリーポイント
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())