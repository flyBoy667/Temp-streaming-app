from streamz.dataframe import DataFrame
from streamz import Stream
import pandas as pd
import numpy as np
import time
import threading
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# 1. Initialisation du Stream
example = pd.DataFrame({'temperature': [0.0], 'timestamp': [pd.Timestamp.now()]})
stream = Stream()
df = DataFrame(stream, example=example)

# 2. Configuration du plot
plt.figure(figsize=(10, 5))
plt.title('Monitoring Température en Temps Réel')
plt.xlabel('Temps')
plt.ylabel('Température (°C)')
plt.grid(True)

# 3. Buffer pour stocker les données
buffer = pd.DataFrame(columns=['timestamp', 'temperature'])

# 4. Callback de mise à jour
def update_plot(x):
    global buffer
    
    if not x.empty:
        # Ajout des nouvelles données
        buffer = pd.concat([buffer, x]).tail(20)  # Garde les 20 derniers points
        
        # Mise à jour du graphique
        clear_output(wait=True)
        plt.clf()
        
        plt.plot(buffer['timestamp'], buffer['temperature'], 'r-', marker='o', label='Température')
        plt.axhline(y=30, color='g', linestyle='--', label='Seuil Alerte (30°C)')
        
        # Annotation des dépassements
        alerts = buffer[buffer['temperature'] > 30]
        if not alerts.empty:
            for _, row in alerts.iterrows():
                plt.annotate(f"ALERTE {row['temperature']:.1f}°C", 
                            (row['timestamp'], row['temperature']),
                            textcoords="offset points", 
                            xytext=(0,10), 
                            ha='center',
                            color='red')
        
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        display(plt.gcf())

# 5. Connexion du Sink
df.stream.sink(update_plot)

# 6. Simulation de données (identique à votre code)
def emit_data():
    while True:
        data = pd.DataFrame({
            'temperature': [np.random.uniform(20, 40)],
            'timestamp': [pd.Timestamp.now()]
        })
        stream.emit(data)
        time.sleep(1)

threading.Thread(target=emit_data, daemon=True).start()
