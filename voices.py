import pyaudio
import socket
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)
sock.bind(('128.10.1.185', 2222))

p = pyaudio.PyAudio()


input_stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
output_stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)

def send_audio():
    while True:
        data = input_stream.read(1024)
        sock.sendto(data, ('128.10.1.12', 1234))

def receive_audio():
    while True:

        data, addr = sock.recvfrom(4096)
        output_stream.write(data)


send_audio_thread = threading.Thread(target=send_audio)
receive_audio_thread = threading.Thread(target=receive_audio)
send_audio_thread.start()
receive_audio_thread.start()