# proxy-scraper

Parses a number of 'proxy list' sites, tests the listed proxies, and outputs
them as JSON.

`proxy_parser.py` is a standalone script that takes this JSON file, and outputs
into individual `proxies_<scheme>.txt` files.

## Setting up a development environment

Using [Pipenv](https://github.com/pypa/pipenv), this is relatively simple:

```bash
$ pipenv install
$ pipenv shell
[pipenv: proxy-scraper] $ python3 run.py
```

## TODO

- More parallelization of tasks
- Write parsers for more sites

## Possible Ideas

- Use already-scraped proxies to access proxy listing sites?
- Write a 'general scraper' - Scraping all web pages for possible proxies,
and try to deduce scheme?
