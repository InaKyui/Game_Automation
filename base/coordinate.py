#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : coordinate.py
[Time]        : 2023/06/07 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.3
[Description] : Class coorndinate.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.3"

import time
import random
from base.common import print_message, get_class_attribute
from airtest.core.api import device, click

class Coordinate:
    """
        Attributes:
            x - X coordinate of the click position..(decimal)
            y - Y coordinate of the click position..(decimal)
            error_x - The x-coordinate offset value.(decimal)
            error_y - The y-coordinate offset value.(decimal)
            idle - Waiting time after click, unit is seconds.
    """

    def __init__(self, x:float, y:float, error_x:float, error_y:float, idle:float):
        self.x = x
        self.y = y
        self.error_x = error_x
        self.error_y = error_y
        self.idle = idle

    def __repr__(self):
        """
            Print class property.
        """

        attrib_info = get_class_attribute(self.__dict__)
        return attrib_info

    def get_coordinate_dict(self):
        """
            Convert the class attributes to a dictionary.
        """

        return self.__dict__

    def click(self):
        """
            Click based on class attributes.
        """
        resolution = device().get_current_resolution()

        x = int(self.x * resolution[0])
        y = int(self.y * resolution[1])
        error_x = int(self.error_x * resolution[0])
        error_y = int(self.error_y * resolution[1])
        # Calculate actual coordinate and idle time.
        actual_x = int(x + random.randint(-error_x, error_x))
        if actual_x < 0:
            actual_x = 0
        actual_y = int(y + random.randint(-error_y, error_y))
        if actual_y < 0:
            actual_y = 0
        actual_time = random.randint(self.idle * 10, self.idle * 10 + 5)

        # Click.
        click([actual_x, actual_y])
        # print_message("Success", "Click ({0}, {1})".format(str(actual_x), str(actual_y)))
        # Idle.
        # print_message("Success", "Wait {0} seconds".format(str(actual_time / 10)))
        time.sleep(actual_time / 10)