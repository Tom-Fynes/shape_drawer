import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from turtle import RawTurtle, TurtleScreen

from src.config import (
    THEME, 
    TITLE, 
    WINDOW_SIZE,
    WINDOW_COLOUR
)
from src.logic import ShapeDrawer

def main() -> None:
    root = ThemedTk(theme=THEME) 
    root.title(TITLE)
    root.geometry(WINDOW_SIZE)

    canvas_frame = ttk.Frame(root)
    canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(canvas_frame, width=500, height=500)
    canvas.pack(fill=tk.BOTH, expand=True)

    screen = TurtleScreen(canvas)
    t = RawTurtle(screen)
    screen.bgcolor(WINDOW_COLOUR)


    button_frame = ttk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X)

    shapes = ShapeDrawer(t)

    ttk.Button(button_frame, text="Heart", command=lambda: shapes.heart()).pack(side=tk.LEFT, padx=10, pady=5)
    ttk.Button(button_frame, text="Square", command=lambda: shapes.square()).pack(side=tk.LEFT, padx=10, pady=5)
    ttk.Button(button_frame, text="Star", command=lambda: shapes.star()).pack(side=tk.LEFT, padx=10, pady=5)
    ttk.Button(button_frame, text="Circle", command=lambda: shapes.circle()).pack(side=tk.LEFT, padx=10, pady=5)
    ttk.Button(button_frame, text="Clear", command=lambda: shapes.clear_screen()).pack(side=tk.LEFT, padx=10, pady=5)
    ttk.Button(button_frame, text="Exit", command=root.destroy).pack(side=tk.RIGHT, padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
