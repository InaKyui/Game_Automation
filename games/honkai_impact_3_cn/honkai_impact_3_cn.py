#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : honkai_impact_3_cn.py
[Time]        : 2023/09/17 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.5
[Description] : Honkai Impact 3 project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.5"

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

        # Receive energy.
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
        task_coordinates = [
            {
                "attack_button": Coordinate(round(105/rcr_rsl[0], 4),
                                            round(315/rcr_rsl[1], 4),
                                            round(5/rcr_rsl[0], 4),
                                            round(5/rcr_rsl[1], 4),
                                            1.5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
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
                                             1.5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

    @task_log
    def __task_login(self):
        if self.exists("button_confirm"):
            self.touch("button_confirm")
            self.wait("button_confirm", timeout=600, interval=10)
            self.touch("button_confirm")
        self.wait("login_tip", timeout=300, interval=10)
        self.touch("login_tip", 30)
        for _ in range(5):
            if self.exists("login_receive"):
                self.touch("login_receive", 3)
                # TODO Check actual situation.
                if self.exists("button_confirm"):
                    self.touch("button_confirm", 3)
            else:
                break
        if self.exists("login_abyss"):
            self.touch("login_abyss", 3)
        for _ in range(3):
            if self.exists("button_close"):
                self.touch("button_close", 1.5)
            else:
                break

    @task_log
    def __task_energy(self):
        task = self.get_task("energy")
        self.touch("menu_task", 3)
        task.coordinates["task_page"].click()
        self.touch("button_receive", 1.5)
        self.touch("button_confirm", 1)
        self.touch("button_back", 3)

    @task_log
    def __task_home(self):
        task = self.get_task("home")
        self.touch("menu_home", 5)
        self.touch("home_coin", 3)
        self.touch("home_quest", 1.5)
        self.touch("home_expand")
        for _ in range(10):
            if self.exists("home_quest_complete"):
                self.touch("home_quest_complete")
                self.touch("button_confirm", 1.5)
            else:
                break
        for _ in range(10):
            task.coordinates["new_quest"].click()
            if self.exists("home_dispatch"):
                self.touch("home_dispatch")
                self.touch("home_quest_start")
                if self.exists("home_dispatch"):
                    self.touch("button_back", 1.3)
                    break
            else:
                break
        self.touch("button_back", 3)
        self.touch("home_story_sweep", 1.5)
        if self.exists("home_story_sweep_complete"):
            self.touch("home_story_sweep_complete", 1.5)
            self.touch("button_confirm", 1.5)
        for _ in range(3):
            if self.exists("home_story_sweep_start"):
                self.touch("home_story_sweep_start", 1.5)
                self.touch("home_dispatch", 1.5)
                self.touch("home_story_sweep_confirm", 1.5)
                if self.exists("home_dispatch"):
                    self.touch("button_back", 1.5)
                    break
        self.touch("home_resource")
        if self.exists("home_story_sweep_complete"):
            self.touch("home_story_sweep_complete", 1.5)
            self.touch("button_confirm", 1.5)
        for _ in range(3):
            if self.exists("home_story_sweep_start"):
                self.touch("home_story_sweep_start", 1.5)
                self.touch("home_dispatch", 1.5)
                self.touch("home_story_sweep_confirm", 1.5)
                if self.exists("home_dispatch"):
                    self.touch("button_back", 1.5)
                    break
        self.touch("button_main", 1.5)

    @task_log
    def __task_fleet(self):
        self.touch("menu_fleet", 3)
        self.touch("fleet_task")
        self.touch("fleet_apply")
        self.touch("fleet_accept")
        for _ in range(8):
            if self.exists("fleet_submit"):
                self.touch("fleet_submit")
                self.touch("fleet_double_submit")
                self.touch("fleet_put")
            else:
                break
        self.touch("fleet_bonus")
        self.touch("fleet_receive")
        self.touch("button_confirm")
        self.touch("button_main", 1.5)

    @task_log
    def __task_quest(self):
        task = self.get_task("quest")
        self.touch("menu_quest", 1.5)
        if not self.exists("quest_resource"):
            task.coordinates["attack_button"].click()
        self.touch("quest_resource")
        self.touch("quest_event")
        self.touch("quest_confirm", 1.5)
        self.touch("button_confirm")
        self.touch("button_main", 1.5)

    @task_log
    def __task_complete(self):
        task = self.get_task("complete")
        self.touch("menu_task", 1.5)
        task.coordinates["task_page"].click()
        self.touch("button_receive")
        self.touch("button_confirm")
        task.coordinates["daily_resource"].click()
        self.touch("button_confirm")

    def run_task(self, task:str=None, special_task:str=None):
        # Collection of tasks and special tasks.
        switch_tasks  = {
            "login": self.__task_login,
            "energy": self.__task_energy,
            "home": self.__task_home,
            "fleet": self.__task_fleet,
            "quest": self.__task_quest,
            "complete": self.__task_complete
        }

        if task:
            self.task_init()
            for t in task:
                switch_tasks.get(t)()
        elif special_task:
            self.task_init()
            for st in special_task:
                switch_tasks.get("[special]" + st)()
        else:
            self.task_process(switch_tasks)