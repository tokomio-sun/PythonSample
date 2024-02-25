import socketserver
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s\t%(name)s\t%(message)s")


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger("EchoRequestHandler")
        self.logger.debug("__init__")
        super().__init__(request, client_address, server)
        return

    def setup(self):
        self.logger.debug("setup")
        return super().setup()

    def handle(self):
        self.logger.debug("handle")

        # self.request is the TCP socket connected to the client

        # 改行コードを受信するまで待機する
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

    def finish(self):
        self.logger.debug("finish")
        return super().finish()


class EchoServer(socketserver.TCPServer):

    def __init__(self, server_address, handler_class):
        self.logger = logging.getLogger("EchoServer")
        self.logger.debug("__init__")
        super().__init__(server_address, handler_class)
        return

    def server_activate(self):
        self.logger.debug("server_activate")
        super().server_activate()
        return

    def serve_forever(self):
        self.logger.debug("waiting for request")
        self.logger.info("Handling requests, press <Ctrl-C> to quit")
        while True:
            self.handle_request()
        return

    def handle_request(self):
        self.logger.debug("handle_request")
        return super().handle_request()

    def verify_request(self, request, client_address):
        self.logger.debug("verify_request(%s, %s)", request, client_address)
        return super().verify_request(request, client_address)

    def process_request(self, request, client_address):
        self.logger.debug("process_request(%s, %s)", request, client_address)
        return super().process_request(request, client_address)

    def server_close(self):
        self.logger.debug("server_close")
        return super().server_close()

    def finish_request(self, request, client_address):
        self.logger.debug("finish_request(%s, %s)", request, client_address)
        return super().finish_request(request, client_address)

    def close_request(self, request_address):
        self.logger.debug("close_request(%s)", request_address)
        return super().close_request(request_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    address = ("127.0.0.1", 9999)

    # Create the server, binding to localhost on port 9999
    with EchoServer(server_address=address, handler_class=MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
