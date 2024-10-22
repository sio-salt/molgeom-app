import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import py3Dmol
# import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ウィンドウのタイトルを設定
        self.setWindowTitle('3D Visualization App')

        # QWebEngineViewを作成
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # HTMLコンテンツを生成してロード
        html = self.generate_html()
        self.browser.setHtml(html)

    def generate_html(self):
        # # .xyzファイルからデータを読み込む
        # xyz_coords = pd.read_csv('Ih_cart_C60.xyz', delim_whitespace=True, header=None, names=['element', 'x', 'y', 'z'])

        # .xyzファイルの内容を取得
        with open('Ih_cart_C60.xyz', 'r') as f:
            xyz_data = f.read()

        # 原子数とコメント行を追加
        xyz_data = '60\n' + 'comment line\n' + xyz_data

        # 3Dmol.jsビューアを作成
        viewer = py3Dmol.view(width=800, height=600)

        # データをプロット
        viewer.addModel(xyz_data, 'xyz')

        # # 原子を描画
        # for i, row in xyz_coords.iterrows():
        #     viewer.addSphere({
        #         'center': {'x': row['x'], 'y': row['y'], 'z': row['z']},
        #         'radius': 0.3,
        #         'color': 'gray'
        #     })
        #     viewer.addLabel(str(i+1), {
        #         'position': {'x': row['x'], 'y': row['y'], 'z': row['z']},
        #         'fontSize': 12,
        #         'backgroundColor': 'black',
        #         'backgroundOpacity': 0.2
        #     })

        # スタイルを設定
        viewer.setStyle({}, {'sphere': {'radius': 6.0, 'color': 'green'}})
        viewer.setStyle({}, {'stick': {'radius': 0.2}})

        # ビューアを初期化
        viewer.zoomTo()

        # HTMLコンテンツを生成
        html = viewer._repr_html_()

        return html

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
