"""
Galaxy project module for tracking stars and their coordinates.
"""


class Galaxy:
    """
    A class to represent a galaxy containing stars with coordinates.
    Tracks the bounding box of all stars in the galaxy.
    """
    
    def __init__(self):
        """Initialize an empty galaxy with no bounds set."""
        self.stars = []
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        self.min_z = None
        self.max_z = None
    
    def add_star(self, x, y, z, name=None):
        """
        Add a new star to the galaxy and update bounds.
        
        Args:
            x (float): X coordinate of the star
            y (float): Y coordinate of the star
            z (float): Z coordinate of the star
            name (str, optional): Name of the star
        """
        star = {'x': x, 'y': y, 'z': z, 'name': name}
        self.stars.append(star)
        
        # Update bounds using max and min to compare current bounds with new star coordinates
        if self.min_x is None:
            # First star - initialize bounds
            self.min_x = x
            self.max_x = x
            self.min_y = y
            self.max_y = y
            self.min_z = z
            self.max_z = z
        else:
            # Update bounds if necessary
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)
            self.min_z = min(self.min_z, z)
            self.max_z = max(self.max_z, z)
    
    def get_bounds(self):
        """
        Get the current bounding box of the galaxy.
        
        Returns:
            dict: Dictionary containing min and max coordinates for each axis,
                  or None if no stars have been added
        """
        if self.min_x is None:
            return None
        
        return {
            'min_x': self.min_x,
            'max_x': self.max_x,
            'min_y': self.min_y,
            'max_y': self.max_y,
            'min_z': self.min_z,
            'max_z': self.max_z
        }
    
    def get_star_count(self):
        """
        Get the number of stars in the galaxy.
        
        Returns:
            int: Number of stars
        """
        return len(self.stars)
