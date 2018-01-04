import requests
from ..parser import Parser
from ..util import ProxyData
from bs4 import BeautifulSoup

class SocksProxyParser(Parser):
    def parse(self):
        soup = BeautifulSoup(requests.get("https://socks-proxy.net/").text, "html.parser")
        table_body_rows = soup.select("#proxylisttable > tbody > tr")

        for row in table_body_rows:
            data = row.select("td")
            scheme = data[4].lower()

            yield ProxyData(data[0].text, data[1].text, scheme)
