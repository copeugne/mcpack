# IDAS worksite and transport comparison attempt

Generated with tools/view_item8_betterend_ruins.py at 53e1c5d1 from retained
idas-1.13.7+1.21.1-neoforge.jar, SHA-256
7f5031dd90ae0b32d7fe5c6c47c877cac1eb95a178bc78d196cb24c17ce82522.

Eleven templates cover six records: two dig-site assemblies (six pieces), Nether
pump camp, washing camp, the log, train ruins and winter wagon. All four SVG gzip
sheets independently reproduce exactly and were visually inspected. The small
worksites show different equipment arrangements; the log is a furnished authored
structure rather than a natural fallen-log feature. Full contents and definitions
must accompany canonical decisions.

The dig-site and transport sheets materially clip geometry below the sheet and,
for the train, at the left edge. This attempt is preserved as incomplete visual
coverage, not accepted full layout proof for those records. A bounded layout fix
in the existing renderer is needed before relying on their complete silhouettes.
The source NBT remains complete. Lower log/stable geometry also crosses the sheet
boundary. Independently scaled full-cube projections hide interiors and do not
prove assembly, effective placement, operating machinery, entity creation or
visibility in play. Water is not omitted. Green is only a plant-name hint.

```sh
uv run -m tools.view_item8_betterend_ruins --idas-worksites --output evidence/item-8/sources/idas-worksite-views
uv run -m tools.view_item8_betterend_ruins --idas-worksites --output evidence/raw/item8/idas-worksite-views-r1
uv run ruff check tools/view_item8_betterend_ruins.py
uv run basedpyright tools/view_item8_betterend_ruins.py
```

Use fresh output directories and compare the four SVG gzip files before adding
this README. PNGs are scratch inspection views. No family closure follows from
this source increment alone.

| File | SHA-256 |
| --- | --- |
| desert_dig.svg.gz | e882569002c83437920495caf30e3624a340b3b24301388cfb065591fcfab7df |
| dig_site.svg.gz | be016c36c711c39ca9b8f663d5c0922d5f38604cfccdeaba800ecde962e1aa04 |
| transport.svg.gz | 17171a99867149132c4e5d13e44d5c4e0a7a076fa8ce2df5ca127c68abab4c4f |
| worksites.svg.gz | 897528771be3a138d56467539da5c7472dc47debfa474c7bd1aea693f3ce0f0c |
