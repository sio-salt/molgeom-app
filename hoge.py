import tkinter as tk
import py3Dmol


root = tk.Tk()
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

with open('Ih_cart_C60.xyz', 'r') as f:
    xyz_data = f.read()

viewer = py3Dmol.view(width=600, height=600)
viewer.add_to(frame)
viewer.removeAllModels()
viewer.addModel(xyz_data, 'xyz')
viewer.setStyle({'style_name': {'color': 'spectrum'}})
# viewer.setStyle({}, {'sphere': {'radius': 6.0, 'color': 'green'}})
# 結合を描画
viewer.setStyle({}, {'stick': {'radius': 0.2}})
viewer.zoomTo()

root.mainloop()
