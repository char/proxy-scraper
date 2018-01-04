from .util import ProxyData, format_proxy, hash_text
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
import requests

# GOOGLE_DOT_COM_HASH = hash_text(requests.get("https://google.com").text)
# return hash_text(r.text) == GOOGLE_DOT_COM_HASH

TEST_URL = "https://g0.gstatic.com"

def test_proxy(proxy):
    proxies = {
        "http": format_proxy(proxy),
        "https": format_proxy(proxy)
    }

    try:
        r = requests.get(TEST_URL, proxies=proxies, timeout=5)
        return True, r.elapsed.total_seconds() * 1000, hash_text(r.text)
    except:
        pass

    return (False, 0, None)

def parse_and_test_proxies(parser):
    with ThreadPoolExecutor(max_workers=256) as executor:
        future_map = { executor.submit(test_proxy, proxy) : proxy for proxy in parser.parse() }
        for future in futures.as_completed(future_map):
            proxy = future_map[future]
            yield proxy, future.result()

def collect_proxies(working_proxies, gen):
    for proxy, result in gen:
        (working, ping, response_hash) = result
        if working:
            print(format_proxy(proxy))
            print("  Latency [ms]: {}".format(int(ping)))
            working_proxies.append({
                "ip": proxy.ip,
                "port": proxy.port,
                "scheme": proxy.scheme,

                "test_data": {
                    "url": TEST_URL,
                    "latency": int(ping),
                    "hash": response_hash
                }
            })


def main():
    working_proxies = []
    def collect_with_parser(name, parser):
        print("Parsing {} proxies...".format(name))
        collect_proxies(working_proxies, parse_and_test_proxies(parser))

    with ThreadPoolExecutor(max_workers=4) as executor:
        from .parsers.spys_one import SpysOneParser
        from .parsers.free_proxy_list import FreeProxyListParser
        from .parsers.socks_proxy import SocksProxyParser
        from .parsers.premproxy import PremProxyParser

        executor.submit(collect_with_parser, "spys.one", SpysOneParser())
        executor.submit(collect_with_parser, "free-proxy-list.net", FreeProxyListParser())
        executor.submit(collect_with_parser, "socks-proxy.net", SocksProxyParser())
        executor.submit(collect_with_parser, "premproxy.com", PremProxyParser())

    print("\nFound {} working proxies.".format(len(working_proxies)))

    import json
    with open("working_proxies.json", "w") as f:
        json.dump(sorted(working_proxies, key=lambda p: p["test_data"]["latency"]), f, indent=2)
