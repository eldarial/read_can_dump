import sys
import json

for line in iter(sys.stdin.readline, ""):
    linejson = json.loads(line)
    linejson['data'] = linejson['data'][2:]
    linejson['id'] = hex(int(linejson['id']))[2:].zfill(3)
    linejson['len'] = len(linejson['data']) / 2
    print("({timestamp}) can{bus} {id}#{data}".format(**linejson))
