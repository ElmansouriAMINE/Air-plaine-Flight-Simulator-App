import pyaudio
import socket

# Paramètres d'enregistrement audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Paramètres de connexion
HOST = '128.10.1.12' # Adresse IP du serveur
PORT = 5000

# Initialiser l'objet Pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# Initialiser la connexion Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

# Boucle pour enregistrer et envoyer la voix
while True:
    data = stream.read(CHUNK)
    s.sendto(data, ('128.10.1.12', PORT))

# Fermer la connexion et l'objet Pyaudio
# s.close()
# stream.stop_stream()
# stream.close()
# p.terminate()