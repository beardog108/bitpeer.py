import socket
from protocoin.clients import *

class MyBitcoinClient(BitcoinClient):
    def handle_tx(self, message_header, message):
        print message
        for tx_out in message.tx_out:
            print ("BTC: %.8f" % tx_out.get_btc_value())

    def handle_inv(self, message_header, message):
        getdata = GetData()
        getdata_serial = GetDataSerializer()
        getdata.inventory = message.inventory
        self.send_message(getdata, getdata_serial)

def run_main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("bitcoin.sipa.be", 8333))
    print ("Connected !")
    client = MyBitcoinClient(sock)
    client.handshake()
    client.loop()

if __name__ == "__main__":
    run_main()
