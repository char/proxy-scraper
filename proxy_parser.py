import json

working_proxies = None

with open("working_proxies.json") as working_proxies_file:
    working_proxies = json.load(working_proxies_file)

proxies_by_scheme = {}
for proxy in working_proxies:
    if proxy["scheme"] not in proxies_by_scheme:
        proxies_by_scheme[proxy["scheme"]] = []

    proxies_by_scheme[proxy["scheme"]].append(proxy["ip"] + ":" + proxy["port"])

for scheme in proxies_by_scheme:
    with open("proxies_{}.txt".format(scheme), "w") as scheme_file:
        scheme_file.write("\n".join(proxies_by_scheme[scheme]))
