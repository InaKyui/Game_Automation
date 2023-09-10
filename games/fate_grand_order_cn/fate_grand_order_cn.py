#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : fate_grand_order_cn.py
[Time]        : 2023/09/10 18:00:00
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
        # Coordinate information based on (1920,1080)
        # Skill:          [1](485,540);[2](965,540);[3](1445,540)
        # Master:         [Main](1790,480)
        #                 [1](1360,470);[2](1495,470);[3](1630,870)
        # Servant_1:      [1](110,870);[2](245,870);[3](375,870)
        # Servant_2:      [1](590,870);[2](720,870);[3](850,870)
        # Servant_3:      [1](1065,870);[2](1195,870);[3](1330,870)
        # Noble phantasm: [1](620,250);[2](960,250);[3](1290,250)
        # Card:           [1](195,750);[2](580,750)
        task_name = "daily_quest"
        task_mode = "random_task"
        task_coordinates = [
            {
                "scroll_bar": Coordinate(round(1885/rcr_rsl[0], 4),
                               round(830/rcr_rsl[1], 4),
                               round(3/rcr_rsl[0], 4),
                               round(3/rcr_rsl[1], 4),
                               1).get_coordinate_dict(),
                "skill_1": Coordinate(round(485/rcr_rsl[0], 4),
                                      round(540/rcr_rsl[1], 4),
                                      round(5/rcr_rsl[0], 4),
                                      round(5/rcr_rsl[1], 4),
                                      1).get_coordinate_dict(),
                "skill_2": Coordinate(round(965/rcr_rsl[0], 4),
                                      round(540/rcr_rsl[1], 4),
                                      round(5/rcr_rsl[0], 4),
                                      round(5/rcr_rsl[1], 4),
                                      1).get_coordinate_dict(),
                "skill_3": Coordinate(round(1445/rcr_rsl[0], 4),
                                      round(540/rcr_rsl[1], 4),
                                      round(5/rcr_rsl[0], 4),
                                      round(5/rcr_rsl[1], 4),
                                      1).get_coordinate_dict(),
                "master_main": Coordinate(round(1790/rcr_rsl[0], 4),
                                          round(480/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "master_1": Coordinate(round(1360/rcr_rsl[0], 4),
                                       round(470/rcr_rsl[1], 4),
                                       round(5/rcr_rsl[0], 4),
                                       round(5/rcr_rsl[1], 4),
                                       1).get_coordinate_dict(),
                "master_2": Coordinate(round(1495/rcr_rsl[0], 4),
                                       round(470/rcr_rsl[1], 4),
                                       round(5/rcr_rsl[0], 4),
                                       round(5/rcr_rsl[1], 4),
                                       1).get_coordinate_dict(),
                "master_3": Coordinate(round(1630/rcr_rsl[0], 4),
                                       round(470/rcr_rsl[1], 4),
                                       round(5/rcr_rsl[0], 4),
                                       round(5/rcr_rsl[1], 4),
                                       1).get_coordinate_dict(),
                "servant_1_1": Coordinate(round(110/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_1_2": Coordinate(round(245/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_1_3": Coordinate(round(375/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_2_1": Coordinate(round(590/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_2_2": Coordinate(round(720/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_2_3": Coordinate(round(850/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_3_1": Coordinate(round(1065/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_3_2": Coordinate(round(1195/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "servant_3_3": Coordinate(round(1330/rcr_rsl[0], 4),
                                          round(870/rcr_rsl[1], 4),
                                          round(5/rcr_rsl[0], 4),
                                          round(5/rcr_rsl[1], 4),
                                          1).get_coordinate_dict(),
                "noble_phantasm_1": Coordinate(round(620/rcr_rsl[0], 4),
                                               round(250/rcr_rsl[1], 4),
                                               round(5/rcr_rsl[0], 4),
                                               round(5/rcr_rsl[1], 4),
                                               1.5).get_coordinate_dict(),
                "noble_phantasm_2": Coordinate(round(960/rcr_rsl[0], 4),
                                               round(250/rcr_rsl[1], 4),
                                               round(5/rcr_rsl[0], 4),
                                               round(5/rcr_rsl[1], 4),
                                               1.5).get_coordinate_dict(),
                "noble_phantasm_3": Coordinate(round(1290/rcr_rsl[0], 4),
                                               round(250/rcr_rsl[1], 4),
                                               round(5/rcr_rsl[0], 4),
                                               round(5/rcr_rsl[1], 4),
                                               1.5).get_coordinate_dict(),
                "card_1": Coordinate(round(195/rcr_rsl[0], 4),
                                     round(750/rcr_rsl[1], 4),
                                     round(5/rcr_rsl[0], 4),
                                     round(5/rcr_rsl[1], 4),
                                     0.5).get_coordinate_dict(),
                "card_2": Coordinate(round(580/rcr_rsl[0], 4),
                                     round(750/rcr_rsl[1], 4),
                                     round(5/rcr_rsl[0], 4),
                                     round(5/rcr_rsl[1], 4),
                                     0.5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

    @task_log
    def __task_login(self):
        time.sleep(30)
        if exists(self.get_image("login_update.png")):
            touch(self.get_image("login_update.png"))
            time.sleep(1)
        wait(self.get_image("login_tip.png"), timeout=360, interval=15)
        time.sleep(1)
        touch(self.get_image("login_tip.png"))
        time.sleep(30)
        touch(self.get_image("login_logo.png"))
        time.sleep(45)
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

        for cycle in range(3):
            touch(self.get_image("quest_entrance.png"))
            time.sleep(1)
            touch(self.get_image("quest_daily_mission.png"))
            time.sleep(1)
            if not exists(self.get_image("quest_coin.png")):
                task.coordinates["scroll_bar"].click()
                time.sleep(1)
            touch(self.get_image("quest_coin.png"))
            time.sleep(1)
            touch(self.get_image("quest_craft_essences_monalisa.png"))
            time.sleep(1)
            if cycle == 0:
                touch(self.get_image("quest_start.png"))
                time.sleep(10)

            wait(self.get_image("quest_attack.png"))
            time.sleep(1)
            # Round 1.
            task.coordinates["servant_1_1"].click()
            time.sleep(5)
            task.coordinates["servant_2_1"].click()
            time.sleep(1)
            task.coordinates["skill_1"].click()
            time.sleep(5)
            task.coordinates["servant_2_2"].click()
            time.sleep(1)
            task.coordinates["skill_1"].click()
            time.sleep(5)
            task.coordinates["servant_3_1"].click()
            time.sleep(5)
            task.coordinates["servant_3_2"].click()
            time.sleep(1)
            task.coordinates["skill_1"].click()
            time.sleep(5)
            task.coordinates["servant_3_3"].click()
            time.sleep(1)
            task.coordinates["skill_1"].click()
            time.sleep(5)
            task.coordinates["master_main"].click()
            time.sleep(0.5)
            task.coordinates["master_2"].click()
            time.sleep(0.5)
            task.coordinates["skill_1"].click()
            time.sleep(5)
            touch(self.get_image("quest_attack.png"))
            time.sleep(1.5)
            task.coordinates["noble_phantasm_1"].click()
            time.sleep(0.5)
            task.coordinates["card_1"].click()
            time.sleep(0.5)
            task.coordinates["card_2"].click()
            time.sleep(15)
            wait(self.get_image("quest_attack.png"))
            time.sleep(1)
            # Round 2.
            touch(self.get_image("quest_attack.png"))
            time.sleep(1.5)
            task.coordinates["noble_phantasm_1"].click()
            time.sleep(0.5)
            task.coordinates["card_1"].click()
            time.sleep(0.5)
            task.coordinates["card_2"].click()
            time.sleep(15)
            wait(self.get_image("quest_attack.png"))
            time.sleep(1)
            # Round 3.
            task.coordinates["servant_1_3"].click()
            time.sleep(5)
            touch(self.get_image("quest_attack.png"))
            time.sleep(1.5)
            task.coordinates["noble_phantasm_1"].click()
            time.sleep(0.5)
            task.coordinates["card_1"].click()
            time.sleep(0.5)
            task.coordinates["card_2"].click()
            time.sleep(15)
            # Finish.
            wait(self.get_image("quest_fetters.png"), timeout=360, interval=15)
            time.sleep(1)
            touch(self.get_image("quest_fetters.png"), timeout=360, interval=15)
            time.sleep(1)
            touch(self.get_image("quest_experiences.png"), timeout=360, interval=15)
            time.sleep(1)
            for _ in range(3):
                if exists(self.get_image("quest_next.png")):
                    touch(self.get_image("quest_next.png"))
                    time.sleep(1.5)
                else:
                    break
            touch(self.get_image("quest_continue.png"))
            time.sleep(1.5)
            if exists(self.get_image("quest_silver_apple.png")):
                break
                # touch(self.get_image("quest_silver_apple.png"))
                # time.sleep(1.5)
                # touch(self.get_image("quest_decide.png"))
                # time.sleep(1.5)

    def run_task(self):
        switch_tasks  = {
            "login": self.__task_login,
            "daily_quest": self.__task_daily_quest
        }

        self.task_process(switch_tasks)