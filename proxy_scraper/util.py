import hashlib
from collections import namedtuple

ProxyData = namedtuple("ProxyData", ["ip", "port", "scheme"])

def hash_text(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def format_proxy(proxy):
    return f"{proxy.scheme}://{proxy.ip}:{proxy.port}"
