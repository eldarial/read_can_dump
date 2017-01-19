from pyvit.file.db.jsondb import JsonDbParser
from pyvit.hw import socketcan

parser = JsonDbParser()
b = parser.parse('ford_fusion_2017_canard.json')

dev = socketcan.SocketCanDev('vcan0')
dev.start()

count = 0
while True:
    frame = dev.recv()
    signals = b.parse_frame(frame)
    if signals:
        for s in signals:
            count += 1
            print(s)
            if count % 10 == 0:
                print(count)
