from vidstream import AudioSender
from vidstream import AudioReceiver

import threading


receiver = AudioReceiver('128.10.3.180',9999)
receive_thread = threading.Thread(target=receiver.start_server)


sender = AudioSender('128.10.1.12', 5556)
sender_thread = threading.Thread(target=sender.start_stream)


receive_thread.start()
sender_thread.start()