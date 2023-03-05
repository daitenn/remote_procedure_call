from network_logic import NetworkLogic


class Server:
    @staticmethod
    def main():
        NetworkLogic.start_unix_socket_server()


if __name__ == '__main__':
    Server.main()
