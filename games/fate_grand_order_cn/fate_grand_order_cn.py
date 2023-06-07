#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : fate_grand_order_cn.py
[Time]        : 2023/06/07 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.3
[Description] : Fate grand order project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.3"

import os
import time
from base.game import Game
from base.task import Task
from base.common import *
from base.coordinate import Coordinate
from airtest.core.api import *

class FateGrandOrder(Game):
    def __init__(self, name="Fate_Grand_Order", country="Cn"):
        super().__init__(name, country)
        # Define game attribute.
        self.package_name = "com.bilibili.fatego"
        self.resolution = (1920, 1080)

    @task_log
    def task_init(self):
        """
            Initialize task information.
        """

        # Resolution at the time of recording.
        rcr_rsl = (1920, 1080)
        # Login.
        task_name = "login"
        task_mode = "start_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Daily quest.
        # Coordinate information.(1920,1080)
        # First: [1](110,870);[2](245,870);[3](375,870)
        # Second:[1](890,870);[2](720,870);[3](850,870)
        # Third: [1](1065,870);[2](1195,870);[3](1330,870)
        # Hero:  [Main](1790,480)
        #        [1](1360,470);[2](1495,470);[3](1630,870)
        # Skill: [1](475,690);[2](960,690);[3](1420,690)
        task_name = "daily_quest"
        task_mode = "random_task"
        task_coordinates = [
            {
                "first_skill": Coordinate(round(210/rcr_rsl[0], 4),
                                          round(200/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1.5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

    @task_log
    def __task_login(self):
        wait(self.get_image("login_tip.png"), timeout=360, interval=15)
        time.sleep(1)
        touch(self.get_image("login_tip.png"))
        time.sleep(30)
        touch(self.get_image("login_logo.png"))
        time.sleep(30)
        touch(self.get_image("login_close.png"))
        time.sleep(5)
        for i in range(5):
            if exists(self.get_image("button_close.png")):
                touch(self.get_image("button_close.png"))
                time.sleep(3)
            else:
                break

    @task_log
    def __task_daily_quest(self):
        task = self.get_task("daily_quest")
        pass

    def run_task(self):
        switch_tasks  = {
            "login": self.__task_login,
            "daily_quest": self.__task_daily_quest
        }

        self.task_process(switch_tasks)