#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : honkai_impact_3_cn.py
[Time]        : 2023/05/01 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.0
[Description] : Honkai Impact 3 project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.0"

import os
import time
from base.game import Game
from base.task import Task
from base.common import *
from base.coordinate import Coordinate
from airtest.core.api import *

class HonkaiImpact3(Game):
    def __init__(self, name="Honkai_Impact_3", country="Cn"):
        super().__init__(name, country)
        # Define game attribute.
        self.package_name = "com.miHoYo.enterprise.NGHSoD"
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

        # Receive_energy.
        task_name = "energy"
        task_mode = "start_task"
        task_coordinates = [
            {
                "task_page": Coordinate(round(210/rcr_rsl[0], 4),
                                        round(200/rcr_rsl[1], 4),
                                        round(5/rcr_rsl[0], 4),
                                        round(5/rcr_rsl[1], 4),
                                        1.5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Home.
        task_name = "home"
        task_mode = "random_task"
        task_coordinates = [
            {
                "new_quest": Coordinate(round(1425/rcr_rsl[0], 4),
                                        round(135/rcr_rsl[1], 4),
                                        round(5/rcr_rsl[0], 4),
                                        round(5/rcr_rsl[1], 4),
                                        1.5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Fleet.
        task_name = "fleet"
        task_mode = "random_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Quest.
        task_name = "quest"
        task_mode = "random_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Complete.
        task_name = "complete"
        task_mode = "finish_task"
        task_coordinates = [
            {
                "task_page": Coordinate(round(210/rcr_rsl[0], 4),
                                        round(200/rcr_rsl[1], 4),
                                        round(5/rcr_rsl[0], 4),
                                        round(5/rcr_rsl[1], 4),
                                        1.5).get_coordinate_dict()
            },
            {
                "daily_resource": Coordinate(round(1820/rcr_rsl[0], 4),
                                             round(1000/rcr_rsl[1], 4),
                                             round(3/rcr_rsl[0], 4),
                                             round(3/rcr_rsl[1], 4),
                                             3).get_coordinate_dict()
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
        for i in range(5):
            if exists(self.get_image("login_receive.png")):
                touch(self.get_image("login_receive.png"))
                time.sleep(3)
                touch(self.get_image("button_confirm.png"))
                time.sleep(3)
            else:
                break
        if exists(self.get_image("login_abyss.png")):
            touch(self.get_image("login_abyss.png"))
            time.sleep(5)
        for i in range(3):
            if exists(self.get_image("button_close.png")):
                touch(self.get_image("button_close.png"))
                time.sleep(3)
            else:
                break

    @task_log
    def __task_energy(self):
        task = self.get_task("energy")
        touch(self.get_image("menu_task.png"))
        time.sleep(5)
        task.coordinates["task_page"].click()
        touch(self.get_image("button_receive.png"))
        time.sleep(3)
        touch(self.get_image("button_confirm.png"))
        time.sleep(1.5)
        touch(self.get_image("button_back.png"))
        time.sleep(5)

    @task_log
    def __task_home(self):
        task = self.get_task("home")
        touch(self.get_image("menu_home.png"))
        time.sleep(7)
        touch(self.get_image("home_coin.png"))
        time.sleep(5)
        touch(self.get_image("home_quest.png"))
        time.sleep(3)
        touch(self.get_image("home_expand.png"))
        time.sleep(3)
        for i in range(10):
            if exists(self.get_image("home_quest_complete.png")):
                touch(self.get_image("home_quest_complete.png"))
                time.sleep(1.5)
                touch(self.get_image("button_confirm.png"))
                time.sleep(3)
            else:
                break
        for i in range(10):
            task.coordinates["new_quest"].click()
            if exists(self.get_image("home_dispatch.png")):
                touch(self.get_image("home_dispatch.png"))
                time.sleep(1.5)
                touch(self.get_image("home_quest_start.png"))
                time.sleep(3)
                if exists(self.get_image("home_dispatch.png")):
                    touch(self.get_image("button_back.png"))
                    time.sleep(3)
                    break
            else:
                break
        touch(self.get_image("button_back.png"))
        time.sleep(5)
        touch(self.get_image("home_story_sweep.png"))
        time.sleep(3)
        if exists(self.get_image("home_story_sweep_complete.png")):
            touch(self.get_image("home_story_sweep_complete.png"))
            time.sleep(1.5)
            touch(self.get_image("button_confirm.png"))
            time.sleep(3)
        for i in range(3):
            if exists(self.get_image("home_story_sweep_start.png")):
                touch(self.get_image("home_story_sweep_start.png"))
                time.sleep(1.5)
                touch(self.get_image("home_dispatch.png"))
                time.sleep(1.5)
                touch(self.get_image("home_story_sweep_confirm.png"))
                time.sleep(3)
                if exists(self.get_image("home_dispatch.png")):
                    touch(self.get_image("button_back.png"))
                    time.sleep(3)
                    break
        touch(self.get_image("home_resource.png"))
        time.sleep(3)
        if exists(self.get_image("home_story_sweep_complete.png")):
            touch(self.get_image("home_story_sweep_complete.png"))
            time.sleep(1.5)
            touch(self.get_image("button_confirm.png"))
            time.sleep(3)
        for i in range(3):
            if exists(self.get_image("home_story_sweep_start.png")):
                touch(self.get_image("home_story_sweep_start.png"))
                time.sleep(1.5)
                touch(self.get_image("home_dispatch.png"))
                time.sleep(1.5)
                touch(self.get_image("home_story_sweep_confirm.png"))
                time.sleep(3)
                if exists(self.get_image("home_dispatch.png")):
                    touch(self.get_image("button_back.png"))
                    time.sleep(5)
                    break
        touch(self.get_image("button_main.png"))
        time.sleep(5)

    @task_log
    def __task_fleet(self):
        touch(self.get_image("menu_fleet.png"))
        time.sleep(5)
        touch(self.get_image("fleet_task.png"))
        time.sleep(3)
        touch(self.get_image("fleet_apply.png"))
        time.sleep(3)
        touch(self.get_image("fleet_accept.png"))
        time.sleep(3)
        for i in range(8):
            if exists(self.get_image("fleet_submit.png")):
                touch(self.get_image("fleet_submit.png"))
                time.sleep(3)
                touch(self.get_image("fleet_double_submit.png"))
                time.sleep(3)
                touch(self.get_image("fleet_put.png"))
                time.sleep(5)
            else:
                break
        touch(self.get_image("fleet_bonus.png"))
        time.sleep(3)
        touch(self.get_image("fleet_receive.png"))
        time.sleep(3)
        touch(self.get_image("button_confirm.png"))
        time.sleep(5)
        touch(self.get_image("button_main.png"))
        time.sleep(5)

    @task_log
    def __task_quest(self):
        touch(self.get_image("menu_quest.png"))
        time.sleep(5)
        touch(self.get_image("quest_resource.png"))
        time.sleep(3)
        touch(self.get_image("quest_event.png"))
        time.sleep(3)
        touch(self.get_image("quest_confirm.png"))
        time.sleep(3)
        touch(self.get_image("button_confirm.png"))
        time.sleep(1.5)
        touch(self.get_image("button_main.png"))
        time.sleep(5)

    @task_log
    def __task_complete(self):
        task = self.get_task("complete")
        touch(self.get_image("menu_task.png"))
        time.sleep(5)
        task.coordinates["task_page"].click()
        touch(self.get_image("button_receive.png"))
        time.sleep(3)
        touch(self.get_image("button_confirm.png"))
        time.sleep(1.5)
        task.coordinates["daily_resource"].click()
        touch(self.get_image("button_confirm.png"))
        time.sleep(1.5)


    def run_task(self):
        switch_tasks  = {
            "login": self.__task_login,
            "energy": self.__task_energy,
            "home": self.__task_home,
            "fleet": self.__task_fleet,
            "quest": self.__task_quest,
            "complete": self.__task_complete
        }

        self.task_process(switch_tasks)