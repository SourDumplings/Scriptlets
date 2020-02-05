import json
import os


def callback(host, port, password, userPath):
    # 在此处修改您的callback，自定义逻辑

    print(host, port, password)
    ss_local_config = json.dumps({
        "server": host,
        "server_port": port,
        "password": password,
        "method": "chacha20",
        "protocol": "origin",
        "obfs": "http_simple",
    }, indent=4)
    print(ss_local_config)

    os.chdir(userPath + "/vultr/ssr")
    with open("local.json", "w") as f:
        f.write(ss_local_config)
    print("local.json updated.")
