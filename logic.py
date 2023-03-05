
# サーバは、以下の関数を RPC としてクライアントに提供します。

# floor(double x): 10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
# nroot(int n, int x): 方程式 rn = x における、r の値を計算する。
# reverse(string s): 文字列 s を入力として受け取り、入力文字列の逆である新しい文字列を返す。
# validAnagram(string str1, string str2): 2 つの文字列を入力として受け取り，2 つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す。
# sort(string[] strArr): 文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。

class Logic:
    floor: int = lambda self, x: int(x)
    n_root: float = lambda self, n, x: x ** (1/n)
    reverse: str = lambda self, str: str[::-1]
    validAnagram: bool = lambda self, str1, str2: sorted(str1) == sorted(str2)
    sort: list = lambda self, str_arr: sorted(str_arr)

    def __init__(self):
        self.hashmap = {
            "floor": self.floor,
            "nroot": self.n_root,
            "reverse": self.reverse,
            "validAnagram": self.validAnagram,
            "sort": self.sort
        }

    def _parse_request(self, req):
        print(req)
        func_name = self.hashmap[req["method"]]
        param_list = req["params"]
        param_types_list = req["param_types"]
        parsed_param_list = []

        type_map = {
            "int": int,
            "float": float,
            "str": str,
            "list[str]": lambda x: x
        }

        for i, val in enumerate(param_types_list):
            if val not in type_map:
                print(f'{val} is not supported type')
                exit()
            parsed_param_list.append(type_map[val][param_list[i]])

        if len(parsed_param_list) != len(func_name.__code__.co_valnames) - 1:
            print('Invalid number of arguments')
            exit()

        return func_name(*parsed_param_list)
