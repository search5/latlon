# Usage Guide

## Creating Coordinates

### From decimal degrees

The simplest way is to pass two scalars directly to `LatLon`:

```python
from latlon import LatLon

palmyra = LatLon(5.8833, -162.0833)
```

### From Latitude / Longitude objects

```python
from latlon import LatLon, Latitude, Longitude

palmyra = LatLon(Latitude(5.8833), Longitude(-162.0833))
```

### From degrees, minutes, seconds

Any combination of integer degrees, decimal minutes, and decimal seconds is accepted.
The `_update()` method reconciles any overflow (e.g. minutes > 60) automatically.

```python
palmyra = LatLon(
    Latitude(degree=5, minute=52, second=59.88),
    Longitude(degree=-162, minute=-4.998)
)
```

### From a formatted string

Use `string2latlon` (or `string2geocoord` for a single coordinate) with a format string.
Format codes:

| Code | Meaning |
|------|---------|
| `H`  | Hemisphere identifier (`N`, `S`, `E`, `W`) |
| `D`  | Decimal degrees (e.g. `5.833`) |
| `d`  | Integer degrees (e.g. `5`) |
| `M`  | Decimal minutes (e.g. `52.998`) |
| `m`  | Integer minutes (e.g. `52`) |
| `S`  | Decimal seconds (e.g. `59.88`) |

Codes are separated by `%`. Any other character between `%` delimiters is treated as a literal separator.

```python
from latlon import string2latlon

palmyra = string2latlon('5 52 59.88 N', '162 4 59.88 W', 'd% %m% %S% %H')
palmyra = string2latlon('N 5, 52.998', 'W 162, 4.998', 'H% %d%, %M')
palmyra = string2latlon('5.8833', '-162.0833', 'D')
```

!!! note
    A hemisphere identifier (`H`) and the degree/decimal-degree value must be separated by at least one character. `'5 52 59.88N'` is invalid; `'5 52 59.88 N'` is valid.

---

## Formatting Output

Both `LatLon` and individual `Latitude`/`Longitude` objects have a `to_string()` method.
The format string uses the same codes as above, plus optional zero-padding and decimal precision:

```
[0N]<code>[.P]
```

- `0N` — zero-pad the integer part to *N* digits
- `.P` — round to *P* decimal places

### Examples

```python
palmyra = LatLon(5.8833, -162.0833)

palmyra.to_string('D')           # ('5.8833', '-162.0833')
palmyra.to_string('H% %D')       # ('N 5.8833', 'W 162.0833')
palmyra.to_string('d%_%M')       # ('5_52.998', '-162_4.998')
palmyra.to_string('d%_%M.3')     # ('5_52.998', '-162_4.998')
palmyra.to_string('02d%M.3%H')   # ('0552.998N', '1624.998W')
palmyra.to_string('d% %m% %S% %H')  # ('5 52 59.88 N', '162 4 59.88 W')
```

### SeeYou CUP format example

```python
from latlon import LatLon

ll = LatLon(51.61140, -0.80798)
lat_str, lon_str = ll.to_string('02d%M.3%H')
# lat_str = '5136.684N'
# lon_str = '0048.479W'
```

---

## Distance and Heading

```python
from latlon import LatLon

palmyra = LatLon(5.8833, -162.0833)
honolulu = LatLon(21.3, -157.8167)

# Great-circle distance (WGS84 ellipsoid, km)
distance = palmyra.distance(honolulu)
print(distance)  # 1766.691...

# FAI sphere approximation
print(palmyra.distance(honolulu, ellipse='sphere'))  # 1774.771...

# Initial and reverse headings (degrees)
print(palmyra.heading_initial(honolulu))   # 14.690...
print(palmyra.heading_reverse(honolulu))   # 165.648...
```

---

## Offset

Compute a new coordinate by travelling a given distance and heading from an existing one:

```python
initial_heading = palmyra.heading_initial(honolulu)
hnl = palmyra.offset(initial_heading, distance)
print(hnl.to_string('D'))  # ('21.3', '-157.8167')
```

---

## GeoVector Arithmetic

Subtracting two `LatLon` objects returns a `GeoVector` with `heading` and `magnitude` (distance in km):

```python
vector = honolulu - palmyra        # GeoVector
print(vector)                      # heading, magnitude

scaled = vector * 2                # double the distance
reconstructed = palmyra + (scaled / 2.0)
print(reconstructed)               # back to honolulu coordinates
```

---

## Equality and Approximate Equality

```python
palmyra_1 = LatLon(Latitude(5.8833), Longitude(-162.0833))
palmyra_2 = LatLon(5.8833, -162.0833)

palmyra_1 == palmyra_2  # True — compares decimal_degree values

# For floating-point-safe comparison (within 1 mm by default):
palmyra_1.almost_equal(palmyra_2)  # True
```

---

## Projection

```python
import pyproj
from latlon import LatLon

palmyra = LatLon(5.8833, -162.0833)
projection = pyproj.Proj(proj='merc', ellps='WGS84')
x, y = palmyra.project(projection)
```
