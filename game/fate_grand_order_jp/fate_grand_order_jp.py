#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.10
"""
[File]        : fate_grand_order_jp.py
[Time]        : 2023/12/31 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 3.0
[Description] : Fate grand order project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.7"

from base.game import Game
from base.task import Task
from base.utils import *
from base.coordinate import Coordinate
from airtest.core.api import *

class FateGrandOrder(Game):
    def __init__(self, name="Fate_Grand_Order", country="Jp"):
        super().__init__(name, country)
        # Define game attribute.
        self.package_name = "com.aniplex.fategrandorder"
        self.resolution = (1334, 750)

    def start(self):
        pass

    @task_log
    def task_init(self):
        """
            Initialize task information.
        """
        # Resolution at the time of recording.
        rcr_rsl = (1920, 1080)
        # # Login.
        # task_name = "login"
        # task_mode = "start_task"
        # task = Task(task_name)
        # self.tasks[task_mode].append(task)
        # Friend gacha.
        task_name = "friend_gacha"
        task_mode = "random_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # # Quest.
        # Coordinate information based on (1920,1080)
        # Skill:          [1](485,540);[2](965,540);[3](1445,540)
        # Master:         [Main](1790,480)
        #                 [1](1360,470);[2](1495,470);[3](1630,870)
        # Servant_1:      [1](110,870);[2](245,870);[3](375,870)
        # Servant_2:      [1](590,870);[2](720,870);[3](850,870)
        # Servant_3:      [1](1065,870);[2](1195,870);[3](1330,870)
        # Noble phantasm: [1](620,250);[2](960,250);[3](1290,250)
        # Card:           [1](195,750);[2](580,750)
        # task_name = "event_quest"
        # task_mode = "random_task"
        # task_coordinates = [
        #     {
        #         "scroll_bar": Coordinate(round(1885/rcr_rsl[0], 4),
        #                        round(830/rcr_rsl[1], 4),
        #                        round(3/rcr_rsl[0], 4),
        #                        round(3/rcr_rsl[1], 4),
        #                        1).get_coordinate_dict(),
        #         "skill_1": Coordinate(round(485/rcr_rsl[0], 4),
        #                               round(540/rcr_rsl[1], 4),
        #                               round(5/rcr_rsl[0], 4),
        #                               round(5/rcr_rsl[1], 4),
        #                               1).get_coordinate_dict(),
        #         "skill_2": Coordinate(round(965/rcr_rsl[0], 4),
        #                               round(540/rcr_rsl[1], 4),
        #                               round(5/rcr_rsl[0], 4),
        #                               round(5/rcr_rsl[1], 4),
        #                               1).get_coordinate_dict(),
        #         "skill_3": Coordinate(round(1445/rcr_rsl[0], 4),
        #                               round(540/rcr_rsl[1], 4),
        #                               round(5/rcr_rsl[0], 4),
        #                               round(5/rcr_rsl[1], 4),
        #                               1).get_coordinate_dict(),
        #         "switch_3": Coordinate(round(810/rcr_rsl[0], 4),
        #                                round(520/rcr_rsl[1], 4),
        #                                round(5/rcr_rsl[0], 4),
        #                                round(5/rcr_rsl[1], 4),
        #                                0.5).get_coordinate_dict(),
        #         "switch_4": Coordinate(round(1110/rcr_rsl[0], 4),
        #                                round(520/rcr_rsl[1], 4),
        #                                round(5/rcr_rsl[0], 4),
        #                                round(5/rcr_rsl[1], 4),
        #                                0.5).get_coordinate_dict(),
        #         "switch_confirm": Coordinate(round(960/rcr_rsl[0], 4),
        #                                      round(940/rcr_rsl[1], 4),
        #                                      round(5/rcr_rsl[0], 4),
        #                                      round(5/rcr_rsl[1], 4),
        #                                      3).get_coordinate_dict(),
        #         "master_main": Coordinate(round(1790/rcr_rsl[0], 4),
        #                                   round(480/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "master_1": Coordinate(round(1360/rcr_rsl[0], 4),
        #                                round(470/rcr_rsl[1], 4),
        #                                round(5/rcr_rsl[0], 4),
        #                                round(5/rcr_rsl[1], 4),
        #                                0.5).get_coordinate_dict(),
        #         "master_2": Coordinate(round(1495/rcr_rsl[0], 4),
        #                                round(470/rcr_rsl[1], 4),
        #                                round(5/rcr_rsl[0], 4),
        #                                round(5/rcr_rsl[1], 4),
        #                                0.5).get_coordinate_dict(),
        #         "master_3": Coordinate(round(1630/rcr_rsl[0], 4),
        #                                round(470/rcr_rsl[1], 4),
        #                                round(5/rcr_rsl[0], 4),
        #                                round(5/rcr_rsl[1], 4),
        #                                0.5).get_coordinate_dict(),
        #         "servant_1_1": Coordinate(round(110/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_1_2": Coordinate(round(245/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_1_3": Coordinate(round(375/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_2_1": Coordinate(round(590/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_2_2": Coordinate(round(720/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_2_3": Coordinate(round(850/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_3_1": Coordinate(round(1065/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_3_2": Coordinate(round(1195/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "servant_3_3": Coordinate(round(1330/rcr_rsl[0], 4),
        #                                   round(870/rcr_rsl[1], 4),
        #                                   round(5/rcr_rsl[0], 4),
        #                                   round(5/rcr_rsl[1], 4),
        #                                   0.5).get_coordinate_dict(),
        #         "noble_phantasm_1": Coordinate(round(620/rcr_rsl[0], 4),
        #                                        round(250/rcr_rsl[1], 4),
        #                                        round(5/rcr_rsl[0], 4),
        #                                        round(5/rcr_rsl[1], 4),
        #                                        0.5).get_coordinate_dict(),
        #         "noble_phantasm_2": Coordinate(round(960/rcr_rsl[0], 4),
        #                                        round(250/rcr_rsl[1], 4),
        #                                        round(5/rcr_rsl[0], 4),
        #                                        round(5/rcr_rsl[1], 4),
        #                                        0.5).get_coordinate_dict(),
        #         "noble_phantasm_3": Coordinate(round(1290/rcr_rsl[0], 4),
        #                                        round(250/rcr_rsl[1], 4),
        #                                        round(5/rcr_rsl[0], 4),
        #                                        round(5/rcr_rsl[1], 4),
        #                                        0.5).get_coordinate_dict(),
        #         "card_1": Coordinate(round(195/rcr_rsl[0], 4),
        #                              round(750/rcr_rsl[1], 4),
        #                              round(5/rcr_rsl[0], 4),
        #                              round(5/rcr_rsl[1], 4),
        #                              0.3).get_coordinate_dict(),
        #         "card_2": Coordinate(round(580/rcr_rsl[0], 4),
        #                              round(750/rcr_rsl[1], 4),
        #                              round(5/rcr_rsl[0], 4),
        #                              round(5/rcr_rsl[1], 4),
        #                              0.3).get_coordinate_dict()
        #     }
        # ]
        # task = Task(task_name, task_coordinates)
        # self.tasks[task_mode].append(task)
        # # Event_gacha.
        # task_name = "event_gacha"
        # task_mode = "random_task"
        # task = Task(task_name)
        # self.tasks[task_mode].append(task)

    @task_log
    def __task_login(self):
        pass

    @task_log
    def __task_event_quest(self):
        task = self.get_task("event_quest")
        for cycle in range(200):
            for i in range(5):
                if self.exists_and_touch("servant_oberon_stage_1", 2.5):
                    break
                elif self.exists_and_touch("servant_oberon_stage_5", 2.5):
                    break
                else:
                    # Refreshing cooldown.
                    if i > 0:
                        time.sleep(11)
                    self.touch("quest_refresh")
                    self.touch("button_confirm", 1.5)
            if cycle == 0:
                self.touch("quest_start")
            self.wait("quest_attack", timeout=30, interval=3)
            # Round 1.
            task.coordinates["servant_3_1"].click(2)
            task.coordinates["servant_3_2"].click()
            task.coordinates["skill_1"].click(2)
            task.coordinates["servant_3_3"].click()
            task.coordinates["skill_1"].click(2)
            task.coordinates["servant_1_3"].click(2.5)
            task.coordinates["servant_2_3"].click(2.5)
            self.touch("quest_attack", 0.3)
            task.coordinates["noble_phantasm_3"].click()
            task.coordinates["noble_phantasm_2"].click()
            task.coordinates["card_1"].click()
            self.wait("quest_attack", timeout=60, interval=3)
            # Round 2.
            self.touch("quest_attack", 0.3)
            task.coordinates["noble_phantasm_1"].click()
            task.coordinates["card_1"].click()
            task.coordinates["card_2"].click()
            self.wait("quest_attack", timeout=75, interval=3)
            # Round 3.
            task.coordinates["servant_1_1"].click(2.5)
            task.coordinates["servant_1_2"].click(2.5)
            task.coordinates["servant_2_1"].click(2.5)
            task.coordinates["master_main"].click()
            task.coordinates["master_3"].click()
            task.coordinates["switch_3"].click()
            task.coordinates["switch_4"].click()
            task.coordinates["switch_confirm"].click()
            task.coordinates["servant_3_1"].click(2)
            task.coordinates["servant_3_2"].click()
            task.coordinates["skill_1"].click(2)
            task.coordinates["servant_3_3"].click()
            task.coordinates["skill_1"].click(2)
            task.coordinates["master_main"].click()
            task.coordinates["master_1"].click(2)
            self.touch("quest_attack", 0.3)
            task.coordinates["noble_phantasm_1"].click()
            task.coordinates["card_1"].click()
            task.coordinates["card_2"].click()
            # Finish.
            self.wait("quest_fetters", timeout=60, interval=5)
            time.sleep(2.5)
            for _ in range(5):
                if self.exists_and_touch("quest_fetters", 1.5):
                    break
                else:
                    task.coordinates["card_1"].click(2)
            for _ in range(5):
                if self.exists_and_touch("quest_experiences", 1.5):
                    break
                else:
                    task.coordinates["card_1"].click(2)
            for _ in range(3):
                if not self.exists_and_touch("quest_next", 1.5):
                    break
            self.exists_and_touch("quest_cancel_friend", 1.5)
            self.touch("quest_continue", 2.5)
            if self.exists_and_touch("quest_golden_apple"):
                self.touch("button_decide", 3.5)

    @task_log
    def __task_event_gacha(self):
        self.touch("event_gacha", 1.5)
        try:
            self.wait("event_gacha_continue", timeout=15, interval=3)
        except:
            touch((self.resolution[0] / 2, self.resolution[0] / 2))
        pos = self.exists_and_touch("event_gacha_continue")
        while True:
            touch(pos)
            if self.exists("button_close"):
                break

    def __task_friend_gacha(self):
        if self.exists_and_touch("friend_gacha_free_summon") or self.exists_and_touch("friend_gacha_summon"):
            while True:
                self.touch("button_decide")
                for _ in range(10):
                    touch((self.resolution[0] * 0.9, self.resolution[0] * 0.7))
                    if self.exists_and_touch("friend_gacha_continue"):
                        break

    def run_task(self, task:str=None, special_task:str=None):
        # Collection of tasks and special tasks.
        switch_tasks  = {
            "login": self.__task_login,
            "friend_gacha": self.__task_friend_gacha,
            "event_quest": self.__task_event_quest,
            "event_gacha": self.__task_event_gacha
        }
        # Running tasks based on task type.
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