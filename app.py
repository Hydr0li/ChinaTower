import tkinter as tk
import pandas as pd
import numpy as np
import pyPDF2
from PIL import Image, ImageTK

root = tk.Tk()
canvas = tk.canvas(root, width=600, height=300)
canvas.grid(columnspan=3)
root.mainloop()
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway")
browse_text.set("Browse")
