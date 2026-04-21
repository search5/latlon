# latlon

Python library for representing and manipulating geographic coordinates (latitude and longitude).

## Features

- Convert lat/lon strings from almost any format into a `LatLon` object
- Automatically store decimal degrees, decimal minutes, and degree/minute/second information
- Output coordinates as formatted strings with configurable precision and zero-padding
- Project lat/lon coordinates into other projections via pyproj
- Calculate distance and heading between coordinates using FAI or WGS84 approximation
- Create a new `LatLon` by offsetting from another with a distance and heading
- Subtract two `LatLon` objects to get a `GeoVector` (distance + heading)
- Add/subtract `LatLon` and `GeoVector` objects

## Quick Start

```python
from latlon import LatLon, Latitude, Longitude

# Create from decimal degrees
palmyra = LatLon(5.8833, -162.0833)

# Create from degrees, minutes, seconds
palmyra = LatLon(
    Latitude(degree=5, minute=52, second=59.88),
    Longitude(degree=-162, minute=-4.998)
)

# Format output
print(palmyra.to_string('d% %m% %S% %H'))
# ('5 52 59.88 N', '162 4 59.88 W')

# Calculate distance between two points
honolulu = LatLon(21.3, -157.8167)
print(palmyra.distance(honolulu))  # km, WGS84
```

## Installation

```bash
pip install latlon3
```

Requires [pyproj](https://pyproj4.github.io/pyproj/).
