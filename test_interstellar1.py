"""
Tests for the Galaxy class in interstellar1 module.
"""
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from galaxyproj.interstellar1 import Galaxy


def test_empty_galaxy():
    """Test that a new galaxy has no bounds."""
    galaxy = Galaxy()
    assert galaxy.get_bounds() is None
    assert galaxy.get_star_count() == 0
    print("✓ Empty galaxy test passed")


def test_single_star():
    """Test adding a single star."""
    galaxy = Galaxy()
    galaxy.add_star(10.0, 20.0, 30.0, "Star1")
    
    bounds = galaxy.get_bounds()
    assert bounds is not None
    assert bounds['min_x'] == 10.0
    assert bounds['max_x'] == 10.0
    assert bounds['min_y'] == 20.0
    assert bounds['max_y'] == 20.0
    assert bounds['min_z'] == 30.0
    assert bounds['max_z'] == 30.0
    assert galaxy.get_star_count() == 1
    print("✓ Single star test passed")


def test_multiple_stars_expanding_bounds():
    """Test that bounds expand correctly when adding multiple stars."""
    galaxy = Galaxy()
    
    # Add first star
    galaxy.add_star(0.0, 0.0, 0.0, "Origin")
    bounds = galaxy.get_bounds()
    assert bounds['min_x'] == 0.0
    assert bounds['max_x'] == 0.0
    
    # Add star with larger coordinates - should expand max bounds
    galaxy.add_star(100.0, 200.0, 300.0, "Far Star")
    bounds = galaxy.get_bounds()
    assert bounds['min_x'] == 0.0
    assert bounds['max_x'] == 100.0
    assert bounds['min_y'] == 0.0
    assert bounds['max_y'] == 200.0
    assert bounds['min_z'] == 0.0
    assert bounds['max_z'] == 300.0
    
    # Add star with negative coordinates - should expand min bounds
    galaxy.add_star(-50.0, -100.0, -150.0, "Negative Star")
    bounds = galaxy.get_bounds()
    assert bounds['min_x'] == -50.0
    assert bounds['max_x'] == 100.0
    assert bounds['min_y'] == -100.0
    assert bounds['max_y'] == 200.0
    assert bounds['min_z'] == -150.0
    assert bounds['max_z'] == 300.0
    
    assert galaxy.get_star_count() == 3
    print("✓ Multiple stars expanding bounds test passed")


def test_star_within_bounds():
    """Test that adding a star within existing bounds doesn't change them."""
    galaxy = Galaxy()
    
    # Establish initial bounds
    galaxy.add_star(-100.0, -100.0, -100.0)
    galaxy.add_star(100.0, 100.0, 100.0)
    
    initial_bounds = galaxy.get_bounds()
    
    # Add star within existing bounds
    galaxy.add_star(50.0, 50.0, 50.0, "Middle Star")
    
    new_bounds = galaxy.get_bounds()
    
    # Bounds should remain unchanged
    assert new_bounds['min_x'] == initial_bounds['min_x']
    assert new_bounds['max_x'] == initial_bounds['max_x']
    assert new_bounds['min_y'] == initial_bounds['min_y']
    assert new_bounds['max_y'] == initial_bounds['max_y']
    assert new_bounds['min_z'] == initial_bounds['min_z']
    assert new_bounds['max_z'] == initial_bounds['max_z']
    
    assert galaxy.get_star_count() == 3
    print("✓ Star within bounds test passed")


def test_bounds_with_identical_coordinates():
    """Test adding multiple stars with some identical coordinates."""
    galaxy = Galaxy()
    
    galaxy.add_star(5.0, 5.0, 5.0)
    galaxy.add_star(5.0, 10.0, 5.0)
    galaxy.add_star(10.0, 5.0, 5.0)
    
    bounds = galaxy.get_bounds()
    assert bounds['min_x'] == 5.0
    assert bounds['max_x'] == 10.0
    assert bounds['min_y'] == 5.0
    assert bounds['max_y'] == 10.0
    assert bounds['min_z'] == 5.0
    assert bounds['max_z'] == 5.0
    
    print("✓ Identical coordinates test passed")


if __name__ == "__main__":
    print("Running Galaxy bounds tests...")
    print()
    
    test_empty_galaxy()
    test_single_star()
    test_multiple_stars_expanding_bounds()
    test_star_within_bounds()
    test_bounds_with_identical_coordinates()
    
    print()
    print("All tests passed! ✓")
