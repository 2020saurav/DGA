import shutil
import sys
import subprocess

class Server:
    def __init__(self, ID, IP, port, role, alive):
        self.ID = ID
        self.IP = IP
        self.port = port
        self.role = role
        self.alive = alive

servers = [
    Server('1', '127.0.0.1', 2020, "master", True),
    Server('2', '127.0.0.1', 2021, "slave", True),
    Server('3', '127.0.0.1', 2022, "slave", True)
]

# Recursively create directories
for server in servers:
    shutil.copytree('DGA', server.ID)

for server in servers:
    command = 'python ' + server.ID + '/setup.py ' + \
    server.ID + ' ' + server.IP + ' ' + str(server.port)
    subprocess.call(command, shell=True)
