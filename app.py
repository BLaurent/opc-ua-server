"""
"""

import time

from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    SERVER = Server()
    SERVER.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    URI = "http://examples.freeopcua.github.io"
    IDX = SERVER.register_namespace(URI)

    # get Objects node, this is where we should put our nodes
    OBJECTS = SERVER.get_objects_node()

    # populating our address space
    CHOCOOBJ = OBJECTS.add_object(IDX, "Chocolate")
    TEMPVAR = CHOCOOBJ.add_variable(IDX, "temperature", 6.7)
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
