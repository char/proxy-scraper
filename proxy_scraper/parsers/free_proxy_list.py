import requests
from ..parser import Parser
from ..util import ProxyData
from bs4 import BeautifulSoup

class FreeProxyListParser(Parser):
    def parse(self):
        soup = BeautifulSoup(requests.get("https://free-proxy-list.net/").text, "html.parser")
        table_body_rows = soup.select("#proxylisttable > tbody > tr")

        for row in table_body_rows:
            data = row.select("td")
            scheme = "https" if data[6].text == "yes" else "http"

            yield ProxyData(data[0].text, data[1].text, scheme)
