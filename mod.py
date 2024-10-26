import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import py3Dmol

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
        # .xyzファイルの内容を取得
        with open('Ih_cart_C60.xyz', 'r') as f:
            xyz_data = f.read()

        # 原子数とコメント行を追加
        xyz_data = '60\n' + 'comment line\n' + xyz_data

        # HTMLとJavaScriptコードを生成
        html_content = f"""
        <html>
        <head>
            <script src="https://3dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
        </head>
        <body>
            <div id="viewer" style="width: 800px; height: 600px;"></div>
            <script>
                var viewer = $3Dmol.createViewer("viewer");
                viewer.addModel(`{xyz_data}`, "xyz");
                viewer.setStyle({{}}, {{sphere: {{radius: 6.0, color: "green"}}}});
                viewer.setStyle({{}}, {{stick: {{radius: 0.2}}}});
                viewer.zoomTo();
                viewer.render();
            </script>
        </body>
        </html>
        """
        
        return html_content

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

