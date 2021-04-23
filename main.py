import platform
import subprocess
import time
from wakeonlan import send_magic_packet


mac_address = "00:00:00:00:00:00"  # Mac address of target machine
response = False

while not response:
    def ping(host):
        parm = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', parm, '4', host]

        return subprocess.call(command) == 0

    response = ping('192.168.0.1')  # IP address of target machine

    if not response:
        print("Need to WOL!")
        send_magic_packet(mac_address)
        print("First packet sent")
        time.sleep(5.5)
        send_magic_packet(mac_address)
        print("Second packet sent")
        time.sleep(5.5)
        send_magic_packet(mac_address)
        print("Third packet sent")
        time.sleep(5.5)