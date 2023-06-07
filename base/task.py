#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : task.py
[Time]        : 2023/06/07 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.3
[Description] : Class task.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.3"

from base.common import get_class_attribute
from base.coordinate import Coordinate

class Task:
    """
        Attributes:
            [Common]
                name - Task name.
                coordinates - Required coordinate information.
            [Statistics]
                pass_count - Total successful count.
                fail_count - Total failed count.
                pass_rate - Success rate = pass_count / (pass_count + fail_count).
                avg_time - Average time.
    """

    def __init__(self, name:str, coordinates:list=[]):
        self.name = name
        self.coordinates = {}
        for cdi in coordinates:
            for ck in cdi.keys():
                self.coordinates[ck] = Coordinate(cdi[ck]["x"],
                                                  cdi[ck]["y"],
                                                  cdi[ck]["error_x"],
                                                  cdi[ck]["error_y"],
                                                  cdi[ck]["idle"])
        # self.result = None
        # self.error_message = ""
        self.pass_count = 0
        self.fail_count = 0
        self.pass_rate = 0
        self.avg_time = 0

    def __repr__(self):
        """
            Print class property.
        """

        attrib_info = get_class_attribute(self.__dict__)
        return attrib_info

    def __del__(self):
        return

    def get_coordinates_dict(self):
        """
            Coordinate information converted to dictionary.
        """

        crd_list = []
        for sck in self.coordinates.keys():
            crd = { sck: self.coordinates[sck].get_coordinate_dict() }
            crd_list.append(crd)
        return crd_list

    def get_config_dict(self):
        """
            Configuration information converted to dictionary.
        """

        config_dict = {
            "name": self.name,
            "coordinates": self.get_coordinates_dict()
        }
        return config_dict

    def get_log_dict(self):
        """
            Log information converted to dictionary.
        """

        log_dict = {
            "pass_count": self.pass_count,
            "fail_count": self.fail_count,
            "pass_rate": self.pass_rate,
            "avg_time": self.avg_time,
        }
        return log_dict