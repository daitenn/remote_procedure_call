import * as net from 'net';
import * as path from 'path';
import * as os from 'os';
import * as readline from 'readline';
export class ClientStart {
    static async startUnixSocketServer() {
        const socket = new net.Socket();
        const SERVER_ADDRESS = path.join(os.homedir(), "tcp_socket_file");
        console.log("server_address is  here: ", SERVER_ADDRESS);
        socket.on("connect", async () => {
            const methodName = await ClientStart.promptUser("Enter method name in the following options: \nfloor(float x), nroot(int n, int x), reverse(str s), validAnagram(str s1, str s2), sort(list[str] strArr)\n");
            const params = await ClientStart.promptUser("Parameter??");
            const paramTypes = await ClientStart.promptUser("paramType??");
            const requestDict = {
                "method": methodName,
                "params": params.trim().split(" "),
                "param_types": paramTypes.trim().split(" "),
                "id": SERVER_ADDRESS
            };
            const request = JSON.stringify(requestDict);
            console.log("Sending request to Server", request);
            socket.write(request, "utf-8");
            console.log("Sent to Server");
        });
        ClientStart.connectionToServer(socket, SERVER_ADDRESS);
    }
    static async promptUser(question) {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        return new Promise((resolve) => {
            rl.question(question, answer => {
                resolve(answer);
                rl.close();
            });
        });
    }
    static connectionToServer(socket, address) {
        try {
            socket.connect(address);
            console.log("Successfully connecting");
        }
        catch (e) {
            console.error(e);
            process.exit();
        }
    }
}
//# sourceMappingURL=client_nw_logic.js.map