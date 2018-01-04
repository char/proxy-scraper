from ..parser import Parser

class DummyParser(Parser):
    def __init__(self, proxies):
        self.proxies = proxies

    def parse(self):
        for proxy in self.proxies:
            yield proxy
