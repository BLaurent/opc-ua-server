from opcua import Client
import logging

#%load_ext autoreload
#%autoreload 2


logging.basicConfig(level=logging.INFO)

client = Client("opc.tcp://172.23.0.254:4840/freeopcua/server/")
client.connect()


def test():
  root = client.get_root_node()
  print("Objects node is: ", root)

  print("Children of root are: ", root.get_children())

  variable = root.get_child(["0:Objects", "2:Chocolate", "2:temperature"])
  print(variable.get_value())

  var=client.get_node("ns=2;i=2")
  print(var.get_value())


