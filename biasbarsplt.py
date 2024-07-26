"""
File: biasbars.py
---------------------
Add your comments here
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

FIGURE = None

import tkinter
import biasbarsdataplt
import biasbarsgui as gui

KEYS = biasbarsdataplt.KEYS


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

FILENAME = "data/movies-multi.csv"

VERTICAL_MARGIN = 30
LEFT_MARGIN = 60
RIGHT_MARGIN = 30
LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]
LABEL_OFFSET = 10
BAR_WIDTH = 75
LINE_WIDTH = 2
TEXT_DX = 2
NUM_VERTICAL_DIVISIONS = 7
TICK_WIDTH = 15

def get_centered_x_coordinate(width, idx):
    pass
    if idx == 0:
        return (((width - RIGHT_MARGIN) - LEFT_MARGIN) / 6) + LEFT_MARGIN
    elif idx == 1:
        return ((LEFT_MARGIN + (width - RIGHT_MARGIN)) / 2)
    elif idx == 2:
        return (((width - RIGHT_MARGIN) - LEFT_MARGIN) / 6) * 5 + LEFT_MARGIN
    else:
        pass
    


def draw_fixed_content(canvas):
    canvas.delete('all')

def plot_word(canvas, word_data, word):
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    global FIGURE

    x_vals = np.arange(len(LABELS))
    bar_size= 0.2

    mydpi = 100
    fig = Figure(figsize=(width/mydpi,height/mydpi),dpi=mydpi)
    plot = fig.add_subplot()

    for i in range(len(KEYS)):
        plot.bar(x_vals+(bar_size*i),word_data[word][KEYS[i]],bar_size,label=KEYS[i])
    
    plot.set_title(word + ' Frequency by Key')
    plot.legend(loc='best')

    if FIGURE:
        FIGURE.get_tk_widget().destroy()

    FIGURE = FigureCanvasTkAgg(fig, master=canvas)
    FIGURE.get_tk_widget().pack()
    FIGURE.draw()


def convert_counts_to_frequencies(word_data):
    pass
    # K = 1000000
    # total_words_men = sum([sum(counts[biasbarsdataplt.KEY_MEN]) for word, counts in word_data.items()])
    # total_words_women = sum([sum(counts[biasbarsdataplt.KEY_WOMEN]) for word, counts in word_data.items()])
    # for word in word_data:
    #     gender_data = word_data[word]
    #     for i in range(3):
    #         gender_data[biasbarsdataplt.KEY_MEN][i] *= K / total_words_men
    #         gender_data[biasbarsdataplt.KEY_WOMEN][i] *= K / total_words_women


def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    word_data = biasbarsdataplt.read_file(FILENAME)
    convert_counts_to_frequencies(word_data)

    top = tkinter.Tk()
    top.wm_title('Bias Bars')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, word_data, plot_word, biasbarsdataplt.search_words)

    draw_fixed_content(canvas)

    top.mainloop()


if __name__ == '__main__':
    main()