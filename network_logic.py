import socket
import os
import json
from logic import Logic


class NetworkLogic:
    @staticmethod
    def start_unix_socket_server() -> None:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            SERVER_ADDRESS = os.path.expanduser("~/tcp_socket_file")
            print("server_address is here", SERVER_ADDRESS)
            NetworkLogic._bind_socket(sock, SERVER_ADDRESS)

            while True:
                connection, address = sock.accept()

                try:
                    print("connection from {}" .format(address))
                    logic = Logic()
                    while True:
                        request = NetworkLogic._received_data(connection)
                        if request:
                            response = NetworkLogic._process_request(
                                request, logic, SERVER_ADDRESS)
                            connection.sendall(response.encode("utf-8"))
                        else:
                            print("no data", address)
                            break
                finally:
                    print("close connection")
                    connection.close()

    @staticmethod
    def _bind_socket(sock: socket.socket, address: str) -> None:
        try:
            os.unlink(address)
        except:
            pass

        print("starting up on server", address)
        sock.bind(address)
        sock.listen(2)
        print(f'Listening to {address}')

    def _received_data(sock: socket.socket) -> str:
        data = sock.recv(256)
        if data:
            return data.decode("utf-8")
        else:
            return ""

    def _process_request(req: str, logic: Logic, address: str) -> str:
        request_dict = json.loads(req)
        result = logic._parse_request(request_dict)
        result_type = str(type(result))
        result_dict = {
            "result": result,
            "result_type": result_type,
            "id": address
        }
        response = json.dumps(result_dict)
        return response
