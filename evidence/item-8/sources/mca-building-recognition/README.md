# MCA building recognition source

Extractor 2ac49ba. Independent r1 reproduction matches all three sources and
the manifest byte for byte. Manifest SHA-256:
06481eae75ce8b701dd96d45455a5d0ea74f24c56a180018bc101dc7334433cf

```sh
uv run -m tools.inspect_item8_pool_elements --archive mca-neoforge-7.7.11+1.21.1.jar --class-name net/conczin/mca/resources/BuildingTypes.class --class-name net/conczin/mca/resources/data/BuildingType.class --class-name net/conczin/mca/server/world/data/Building.class --output evidence/raw/item8/mca-building-recognition-r1
```

BuildingTypes loads JSON classification rules. BuildingType maps blocks and tags
to required counts, with display and grouping properties. Building reads existing
world blocks and records coordinates for validation, room detection and type
selection; addBlock updates its recorded map rather than placing a world block.
The 26 packaged building_types documents therefore describe recognition criteria,
not 26 generated families or structure templates.
