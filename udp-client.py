import socket
import yaml


class UDPClient:
    def __init__(self):
        print("init")
        with open("config.yaml", 'r') as yamlfile:
            cfg = yaml.safe_load(yamlfile)

        self.server_ip = cfg['server-ip']
        self.server_port = cfg['server-port']

    def send(self, byte_data):
        self.socket.send(byte_data)


if __name__ == "__main__":
    udp_client = UDPClient()
