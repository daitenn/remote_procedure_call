import { ClientStart } from "./client_nw_logic";

class Client {
  public static main() {
    ClientStart.startUnixSocketServer();
  }
}

Client.main();
