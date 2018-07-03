"""
"""

import time
import logging

from opcua import ua, Server

logging.basicConfig()
# pylint: disable=C0103
logger = logging.getLogger()
logger.setLevel(logging.INFO)


if __name__ == "__main__":
  FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  logging.basicConfig(format=FORMAT)
  logger.info("Starting OPC/UA server...")
  logging.getLogger("opcua.server").setLevel(logging.WARNING)

  # setup our server
  SERVER = Server()
  SERVER.set_endpoint("opc.tcp://0.0.0.0:4840")
  SERVER.set_security_policy([
    ua.SecurityPolicyType.NoSecurity,
    ua.SecurityPolicyType.Basic128Rsa15_SignAndEncrypt,
    ua.SecurityPolicyType.Basic128Rsa15_Sign,
    ua.SecurityPolicyType.Basic256_SignAndEncrypt,
    ua.SecurityPolicyType.Basic256_Sign])

  # setup our own namespace, not really necessary but should as spec
  URI = "http://examples.freeopcua.github.io"
  IDX = SERVER.register_namespace(URI)
  # get Objects node, this is where we should put our nodes
  OBJECTS = SERVER.get_objects_node()
  IDX = 5
  # populating our address space
  CHOCOOBJ = OBJECTS.add_object(IDX, "Chocolate")
  TEMPVAR = CHOCOOBJ.add_variable("ns=5;s=temperature", "Float", 0.0)
  TEMPVAR.set_writable()    # Set MyVariable to be writable by clients

  # starting!
  SERVER.start()

  try:
    COUNT = 0
    while True:
      time.sleep(1)
      COUNT += 0.1
      TEMPVAR.set_value(COUNT)
  finally:
    #close connection, remove subcsriptions, etc
      SERVER.stop()
