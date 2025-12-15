# interstellarproj

A Python project for tracking stars in a galaxy with automatic bounding box calculation.

## Features

- **Galaxy Class**: Manages a collection of stars with 3D coordinates
- **Automatic Bounds Tracking**: Uses `min()` and `max()` functions to efficiently track the bounding box of all stars
- **Flexible Star Management**: Add stars with coordinates and optional names

## Installation

No external dependencies required. Just clone the repository and start using:

```bash
git clone https://github.com/laithghannai/interstellarproj.git
cd interstellarproj
```

## Usage

```python
from galaxyproj.interstellar1 import Galaxy

# Create a new galaxy
galaxy = Galaxy()

# Add stars with coordinates
galaxy.add_star(0.0, 0.0, 0.0, "Sol")
galaxy.add_star(100.0, 50.0, 75.0, "Alpha Centauri")
galaxy.add_star(-80.0, -120.0, -40.0, "Proxima")

# Get the bounding box
bounds = galaxy.get_bounds()
print(f"X range: [{bounds['min_x']}, {bounds['max_x']}]")
print(f"Y range: [{bounds['min_y']}, {bounds['max_y']}]")
print(f"Z range: [{bounds['min_z']}, {bounds['max_z']}]")

# Get star count
print(f"Total stars: {galaxy.get_star_count()}")
```

## Examples

Run the example script to see the Galaxy class in action:

```bash
python example_usage.py
```

## Testing

Run the test suite to verify the implementation:

```bash
python test_interstellar1.py
```

## Project Structure

```
interstellarproj/
├── galaxyproj/
│   ├── __init__.py
│   └── interstellar1.py      # Main Galaxy class implementation
├── test_interstellar1.py     # Test suite
├── example_usage.py          # Example usage demonstration
└── README.md                 # This file
```

## Implementation Details

The Galaxy class maintains a bounding box by tracking minimum and maximum coordinates for each axis (x, y, z). When a new star is added:

1. If it's the first star, all bounds are initialized to its coordinates
2. For subsequent stars, the bounds are updated using Python's `min()` and `max()` functions
3. This ensures O(1) bounds updates and O(1) bounds retrieval

This approach efficiently handles both expanding bounds (when new stars extend the galaxy) and maintaining bounds (when new stars fall within existing bounds).