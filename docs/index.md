---
hide:
  - navigation
  - toc
---

# pagemeta docs

## InspectedURL

`InspectedURL` is a dataclass whose function is to extract relevant metadata via `SiteHeaders` and `PageMeta`.

::: pagemeta.main.InspectedURL

## SiteHeaders

`SiteHeaders` is a dataclass whose function is to use [httpx.Response](https://httpx.org) and extract relevant metadata (_last-modified_, _content-type_, etc.).

::: pagemeta.headers.SiteHeaders

## PageMeta

`PageMeta` is a dataclass whose function is to [httpx.get](https://httpx.org) a given URL's metadata (_title_, _description_, _[open graph](https://ogp.me/) image_) with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/).

::: pagemeta.main.PageMeta
