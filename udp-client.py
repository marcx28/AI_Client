import getopt
import socket
import sys

import yaml


class UDPClient:

    def __init__(self, argv):
        # Loading of config using flag -f (argument)
        config_file = ''
        try:
            opts, args = getopt.getopt(argv, "hf:", "ifile=")
        except getopt.GetoptError:
            print('python3 udp-client.py -f <configFileName>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('python3 udp-client.py -f <configFileName>')
                sys.exit()
            elif opt in ("-f", "--ifile"):
                config_file = arg

        with open(config_file, 'r') as yamlfile:
            cfg = yaml.safe_load(yamlfile)
        # End of Loading config file

        print("init")

        self.server_ip = cfg['server-ip']
        self.server_port = cfg['server-port']

        self.socket = None

        print(self.server_ip)
        print(self.server_port)

        self.connect()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("socket created")

    def send(self, byte_data):
        self.socket.send(byte_data)


if __name__ == "__main__":
    udp_client = UDPClient(sys.argv[1:])
