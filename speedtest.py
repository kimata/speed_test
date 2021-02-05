#!/usr/bin/env python3

import subprocess
import json
import pprint

# sudo apt-get install gnupg1 apt-transport-https dirmngr
# export INSTALL_KEY=379CE192D401AB61
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY
# echo "deb https://ookla.bintray.com/debian generic main" | sudo tee  /etc/apt/sources.list.d/speedtest.list
# sudo apt-get update
# sudo apt-get install speedtest

def run_test():
    proc = subprocess.run('speedtest --accept-license --server-id=28910 --format=json',
                          shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True)

    return json.loads(proc.stdout)


def format_result(result):
    return {
        'latency': result['ping']['latency'],
        'jitter': result['ping']['jitter'],
        'upload': int(result['upload']['bandwidth'] * 8 / (1000*1000)),
        'download': int(result['download']['bandwidth'] * 8 / (1000*1000)),
    }

print(json.dumps(format_result(run_test())))
