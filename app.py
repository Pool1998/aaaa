#!/usr/bin/env python
# coding: utf-8

# In[1]:


# サンプルアプリ: app.ipynb

import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Sin Wave')
    plt.title('Simple Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# app.py

from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # グラフの生成
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Sin Wave')
    plt.title('Simple Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)

    # グラフをBase64エンコードしてHTMLに埋め込む
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    image_base64 = base64.b64encode(image_stream.read()).decode()

    return render_template('index.html', image_base64=image_base64)

if __name__ == '__main__':
    app.run(debug=True)

