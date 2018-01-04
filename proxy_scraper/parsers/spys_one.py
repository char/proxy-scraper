import requests
from ..parser import Parser
from ..util import ProxyData

class SpysOneParser(Parser):
    def parse(self):
        r = requests.get("http://spys.one/pl.txt")
        for index, line in enumerate(r.text.splitlines()[3:-1]):
            split = line.split(" ")
            if split:
                if split[0]:
                    ip_port = split[0].split(":")
                    scheme = "https" if "-S " in line else "http"

                    yield ProxyData(ip_port[0], ip_port[1], scheme)
