import pyaudio
import socket
import threading

# Configure the IP addresses and ports
# Replace with your own IP addresses and ports
# Machine 1 (sender)
MY_IP = '192.168.0.160'
MY_PORT = 12345
# Machine 2 (receiver)
OTHER_IP = '192.168.0.104'
OTHER_PORT = 12345

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)
sock.bind((MY_IP, MY_PORT))

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open the input and output streams
input_stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
output_stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)

# Function to send audio
def send_audio():
    while True:
        data = input_stream.read(1024)
        sock.sendto(data, (OTHER_IP, OTHER_PORT))

# Function to receive audio
def receive_audio():
    while True:
        data, addr = sock.recvfrom(4096)
        output_stream.write(data)

# Start the send and receive threads
send_audio_thread = threading.Thread(target=send_audio)
receive_audio_thread = threading.Thread(target=receive_audio)
send_audio_thread.start()
receive_audio_thread.start()