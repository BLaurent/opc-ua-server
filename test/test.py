from opcua import Client
import logging

#%load_ext autoreload
#%autoreload 2


logging.basicConfig(level=logging.INFO)

# client = Client("opc.tcp://172.23.0.254:4840")
client = Client("opc.tcp://localhost:9999")
client.connect()


def test():
  root = client.get_root_node()
  print("Objects node is: ", root)

  print("Children of root are: ", root.get_children())

  var=client.get_node("ns=5;s=temperature")
  print(var.get_value())


