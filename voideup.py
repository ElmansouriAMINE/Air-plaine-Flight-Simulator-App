import pyaudio
import socket

# Paramètres d'enregistrement audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Paramètres de connexion
HOST = '192.168.0.160' # Remplacer par l'adresse IP du serveur
PORT = 5000

# Initialiser l'objet Pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

# Initialiser la connexion Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Boucle pour recevoir et jouer la voix
while True:
    data = s.recv(CHUNK)
    stream.write(data)

# Fermer la connexion et l'objet Pyaudio
s.close()
stream.stop_stream()
stream.close()
p.terminate()