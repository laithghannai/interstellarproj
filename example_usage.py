#!/usr/bin/env python3
"""
Example usage of the Galaxy class to demonstrate bounds tracking.
"""
from galaxyproj.interstellar1 import Galaxy


def main():
    print("=== Galaxy Bounds Tracking Example ===\n")
    
    # Create a new galaxy
    galaxy = Galaxy()
    print("Created a new empty galaxy")
    print(f"Initial bounds: {galaxy.get_bounds()}")
    print(f"Star count: {galaxy.get_star_count()}\n")
    
    # Add first star at origin
    print("Adding star 'Sol' at coordinates (0, 0, 0)")
    galaxy.add_star(0.0, 0.0, 0.0, "Sol")
    bounds = galaxy.get_bounds()
    print(f"Bounds after first star: {bounds}")
    print(f"Star count: {galaxy.get_star_count()}\n")
    
    # Add star with positive coordinates
    print("Adding star 'Alpha Centauri' at coordinates (100, 50, 75)")
    galaxy.add_star(100.0, 50.0, 75.0, "Alpha Centauri")
    bounds = galaxy.get_bounds()
    print(f"Bounds after second star:")
    print(f"  X: [{bounds['min_x']}, {bounds['max_x']}]")
    print(f"  Y: [{bounds['min_y']}, {bounds['max_y']}]")
    print(f"  Z: [{bounds['min_z']}, {bounds['max_z']}]")
    print(f"Star count: {galaxy.get_star_count()}\n")
    
    # Add star with negative coordinates
    print("Adding star 'Proxima' at coordinates (-80, -120, -40)")
    galaxy.add_star(-80.0, -120.0, -40.0, "Proxima")
    bounds = galaxy.get_bounds()
    print(f"Bounds after third star:")
    print(f"  X: [{bounds['min_x']}, {bounds['max_x']}]")
    print(f"  Y: [{bounds['min_y']}, {bounds['max_y']}]")
    print(f"  Z: [{bounds['min_z']}, {bounds['max_z']}]")
    print(f"Star count: {galaxy.get_star_count()}\n")
    
    # Add star within existing bounds
    print("Adding star 'Sirius' at coordinates (20, 30, 40) - within existing bounds")
    galaxy.add_star(20.0, 30.0, 40.0, "Sirius")
    new_bounds = galaxy.get_bounds()
    print(f"Bounds after fourth star (should remain unchanged):")
    print(f"  X: [{new_bounds['min_x']}, {new_bounds['max_x']}]")
    print(f"  Y: [{new_bounds['min_y']}, {new_bounds['max_y']}]")
    print(f"  Z: [{new_bounds['min_z']}, {new_bounds['max_z']}]")
    print(f"Star count: {galaxy.get_star_count()}\n")
    
    print("=== Summary ===")
    print(f"Total stars in galaxy: {galaxy.get_star_count()}")
    print(f"Final bounding box:")
    print(f"  X range: {new_bounds['max_x'] - new_bounds['min_x']:.1f} units")
    print(f"  Y range: {new_bounds['max_y'] - new_bounds['min_y']:.1f} units")
    print(f"  Z range: {new_bounds['max_z'] - new_bounds['min_z']:.1f} units")


if __name__ == "__main__":
    main()
