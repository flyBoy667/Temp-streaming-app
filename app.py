from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from streamz.dataframe import DataFrame
from streamz import Stream
import pandas as pd
from threading import Thread
import time

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Initialisation Flask
server = Flask(__name__)
api = Api(server)

# Initialisation Dash
app_dash = Dash(__name__, server=server, url_base_pathname="/dashboard/")

# Initialisation Streamz
example = pd.DataFrame({"temperature": [0.0], "timestamp": [pd.Timestamp.now()]})
stream = Stream()
df = DataFrame(stream, example=example)

# Buffer pour stocker les données
buffer = pd.DataFrame(columns=["timestamp", "temperature"])

# Parser pour les requêtes API
temp_parser = reqparse.RequestParser()
temp_parser.add_argument(
    "temperature", type=float, required=True, help="Température en degrés Celsius"
)


class TemperatureAPI(Resource):
    def post(self):
        args = temp_parser.parse_args()
        new_data = pd.DataFrame(
            {"temperature": [args["temperature"]], "timestamp": [pd.Timestamp.now()]}
        )

        # Émission des données dans le stream
        stream.emit(new_data)

        return {
            "message": "Température enregistrée",
            "temperature": args["temperature"],
        }


api.add_resource(TemperatureAPI, "/api/temperature")


def update_buffer(x):
    global buffer

    if not x.empty:
        buffer = pd.concat([buffer, x]).tail(20)


df.stream.sink(update_buffer)

# Layout Dash
app_dash.layout = html.Div([
    html.H1("Monitoring Température en Temps Réel"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='interval-update', interval=1000, n_intervals=0)
])


@app_dash.callback(
    Output('live-graph', 'figure'),
    Input('interval-update', 'n_intervals')
)
def update_graph(n):
    global buffer
    if buffer.empty:
        return go.Figure()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=buffer["timestamp"],
        y=buffer["temperature"],
        mode='lines+markers',
        name='Température',
        line=dict(color='red')
    ))

    fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Seuil 30°C")

    fig.update_layout(
        xaxis_title="Temps",
        yaxis_title="Température (°C)",
        margin=dict(l=40, r=40, t=40, b=40),
        template="plotly_white"
    )
    return fig


def run_flask():
    server.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)


if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Arrêt du programme")
