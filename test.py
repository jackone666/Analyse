import numpy as np
import plotly.graph_objects as go
t = np.linspace(0, 10, 50)
y = np.sin(t)
fig = go.Figure(data=go.Scatter(x=t, y=y, mode="markers"))
fig.show()