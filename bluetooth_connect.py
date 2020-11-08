import bluetooth

serverMACAddress = '00:1f:e1:dd:08:3d'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
sock.close()

devices = discover_devices()
for device in devices:
    print([_ for _ in find_service(address=device) if 'RFCOMM' in _['protocol'] ])
# now manually select the desired device or hardcode its name/mac whatever in the script
bt_addr = ...
port = [_ for _ in find_service(address=bt_addr) if 'RFCOMM' in _['protocol']][0]['port']
s = BluetoothSocket(RFCOMM)
s.connect((bt_addr, port))
