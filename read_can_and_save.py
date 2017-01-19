from pyvit.file.db.jsondb import JsonDbParser
from pyvit.hw import socketcan

parser = JsonDbParser()
file_read = 'ford_fusion_2017_canard'
b = parser.parse(file_read + '.json')

dev = socketcan.SocketCanDev('vcan0')
dev.start()

count = 0
ff = open('parkassist.txt','w')
while True:
    frame = dev.recv()
    signals = b.parse_frame(frame)
    if signals:
        for s in signals:
            count += 1
            ff.write(str(s)+'\n')
            print(s)
            if count % 10 == 0:
                print(count)
ff.close()
