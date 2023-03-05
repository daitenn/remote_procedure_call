import { ClientStart } from "./client_nw_logic.js";
class Client {
  static main() {
    ClientStart.startUnixSocketServer();
  }
}
Client.main();
//# sourceMappingURL=client.js.map
