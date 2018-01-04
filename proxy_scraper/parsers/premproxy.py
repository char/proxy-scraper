import requests
from ..parser import Parser
from ..util import ProxyData
from bs4 import BeautifulSoup

class PremProxyParser(Parser):
    def parse(self):
        for i in range(12, 0, -1):
            url = "https://premproxy.com/socks-list/{}.htm".format(str(i).zfill(2))

            soup = BeautifulSoup(requests.get(url).text, "html.parser")

            table_rows = soup.select("#proxylist > * > table > tbody > tr")
            for row in table_rows:
                data = row.select("td")

                ip_port = data[0].text.split(":")
                ip = ip_port[0]
                port = ip_port[1]

                scheme = "socks5" if "5" in data[1].text else "socks4"

                yield ProxyData(ip, port, scheme)
