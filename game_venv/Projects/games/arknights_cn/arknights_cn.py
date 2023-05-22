#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : arknights.py
[Time]        : 2023/05/01 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.0
[Description] : Arknights project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.0"

import os
import time
# import pytesseract
from base.game import Game
from base.task import Task
from base.common import *
from base.coordinate import Coordinate
from airtest.core.api import *

class Arknights(Game):
    def __init__(self, name="Arknights", country="Cn"):
        super().__init__(name, country)
        # Define game attribute.
        self.package_name = "com.hypergryph.arknights"
        self.resolution = (1920, 1080)

        self.__event_quest = False

    @task_log
    def task_init(self):
        """
            Initialize task information.
        """

        # Resolution at the time of recording.
        rcr_rsl = (1280, 720)
        # Login.
        task_name = "login"
        task_mode = "start_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Source center.
        task_name = "source_center"
        task_mode = "random_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Infrastructure.
        task_name = "infrastructure"
        task_mode = "random_task"
        task_coordinates = [
            {
                "center": Coordinate(round(865/rcr_rsl[0], 4),
                                     round(165/rcr_rsl[1], 4),
                                     round(3/rcr_rsl[0], 4),
                                     round(3/rcr_rsl[1], 4),
                                     5).get_coordinate_dict()
            },
            {
                "trade_a": Coordinate(round(65/rcr_rsl[0], 4),
                                      round(310/rcr_rsl[1], 4),
                                      round(3/rcr_rsl[0], 4),
                                      round(3/rcr_rsl[1], 4),
                                      5).get_coordinate_dict()
            },
            {
                "trade_b": Coordinate(round(280/rcr_rsl[0], 4),
                                      round(310/rcr_rsl[1], 4),
                                      round(3/rcr_rsl[0], 4),
                                      round(3/rcr_rsl[1], 4),
                                      5).get_coordinate_dict()
            },
            {
                "manufacture_a": Coordinate(round(495/rcr_rsl[0], 4),
                                            round(310/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            5).get_coordinate_dict()
            },
            {
                "manufacture_b": Coordinate(round(65/rcr_rsl[0], 4),
                                            round(520/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            5).get_coordinate_dict()
            },
            {
                "manufacture_c": Coordinate(round(280/rcr_rsl[0], 4),
                                            round(520/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            5).get_coordinate_dict()
            },
            {
                "manufacture_d": Coordinate(round(495/rcr_rsl[0], 4),
                                            round(520/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            5).get_coordinate_dict()
            },
            {
                "dormitory_a": Coordinate(round(800/rcr_rsl[0], 4),
                                          round(310/rcr_rsl[1], 4),
                                          round(3/rcr_rsl[0], 4),
                                          round(3/rcr_rsl[1], 4),
                                          5).get_coordinate_dict()
            },
            {
                "dormitory_b": Coordinate(round(915/rcr_rsl[0], 4),
                                         round(415/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         5).get_coordinate_dict()
            },
            {
                "dormitory_c": Coordinate(round(800/rcr_rsl[0], 4),
                                         round(520/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         5).get_coordinate_dict()
            },
            {
                "dormitory_d": Coordinate(round(915/rcr_rsl[0], 4),
                                         round(625/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         5).get_coordinate_dict()
            },
            {
                "office": Coordinate(round(1265/rcr_rsl[0], 4),
                                     round(415/rcr_rsl[1], 4),
                                     round(3/rcr_rsl[0], 4),
                                     round(3/rcr_rsl[1], 4),
                                     5).get_coordinate_dict()
            },
            {
                "first_operator": Coordinate(round(485/rcr_rsl[0], 4),
                                             round(205/rcr_rsl[1], 4),
                                             round(3/rcr_rsl[0], 4),
                                             round(3/rcr_rsl[1], 4),
                                             1.5).get_coordinate_dict()
            },
            {
                "second_operator": Coordinate(round(485/rcr_rsl[0], 4),
                                              round(480/rcr_rsl[1], 4),
                                              round(3/rcr_rsl[0], 4),
                                              round(3/rcr_rsl[1], 4),
                                              1.5).get_coordinate_dict()
            },
            {
                "third_operator": Coordinate(round(625/rcr_rsl[0], 4),
                                             round(205/rcr_rsl[1], 4),
                                             round(3/rcr_rsl[0], 4),
                                             round(3/rcr_rsl[1], 4),
                                             1.5).get_coordinate_dict()
            },
            {
                "fourth_operator": Coordinate(round(625/rcr_rsl[0], 4),
                                              round(480/rcr_rsl[1], 4),
                                              round(3/rcr_rsl[0], 4),
                                              round(3/rcr_rsl[1], 4),
                                              1.5).get_coordinate_dict()
            },
            {
                "fifth_operator": Coordinate(round(765/rcr_rsl[0], 4),
                                             round(205/rcr_rsl[1], 4),
                                             round(3/rcr_rsl[0], 4),
                                             round(3/rcr_rsl[1], 4),
                                             1.5).get_coordinate_dict()
            },
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Event quest.
        task_name = "event_quest"
        task_mode = "random_task"
        task_coordinates = [
            {
                "last_quest": Coordinate(round(1100/rcr_rsl[0], 4),
                                         round(580/rcr_rsl[1], 4),
                                         round(5/rcr_rsl[0], 4),
                                         round(5/rcr_rsl[1], 4),
                                         5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Daily quest.
        task_name = "daily_quest"
        task_mode = "random_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Recruit center.
        task_name = "recruit_center"
        task_mode = "random_task"
        task_coordinates = [
            {
                "blank_area": Coordinate(round(100/rcr_rsl[0], 4),
                                         round(300/rcr_rsl[1], 4),
                                         round(5/rcr_rsl[0], 4),
                                         round(5/rcr_rsl[1], 4),
                                         5).get_coordinate_dict()
            },
            {
                "first_archive": Coordinate(round(325/rcr_rsl[0], 4),
                                            round(290/rcr_rsl[1], 4),
                                            round(5/rcr_rsl[0], 4),
                                            round(5/rcr_rsl[1], 4),
                                            5).get_coordinate_dict()
            },
            {
                "second_archive": Coordinate(round(955/rcr_rsl[0], 4),
                                             round(290/rcr_rsl[1], 4),
                                             round(5/rcr_rsl[0], 4),
                                             round(5/rcr_rsl[1], 4),
                                             5).get_coordinate_dict()
            },
            {
                "third_archive": Coordinate(round(325/rcr_rsl[0], 4),
                                            round(570/rcr_rsl[1], 4),
                                            round(5/rcr_rsl[0], 4),
                                            round(5/rcr_rsl[1], 4),
                                            5).get_coordinate_dict()
            },
            {
                "fourth_archive": Coordinate(round(955/rcr_rsl[0], 4),
                                             round(570/rcr_rsl[1], 4),
                                             round(5/rcr_rsl[0], 4),
                                             round(5/rcr_rsl[1], 4),
                                             5).get_coordinate_dict()
            },
            {
                "max_time": Coordinate(round(450/rcr_rsl[0], 4),
                                       round(295/rcr_rsl[1], 4),
                                       round(3/rcr_rsl[0], 4),
                                       round(3/rcr_rsl[1], 4),
                                       5).get_coordinate_dict()
            },
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Complete.
        task_name = "complete"
        task_mode = "finish_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

    @task_log
    def __task_login(self):
        # Game updates will cause the program error.
        wait(self.get_image("login_start.png"), timeout=360, interval=15)
        time.sleep(1)
        touch(self.get_image("login_start.png"))
        time.sleep(7)
        touch(self.get_image("login_enter.png"))
        time.sleep(30)
        if exists(self.get_image("login_rewards.png")):
            # Receive login rewards
            touch(self.get_image("login_rewards.png"))
            time.sleep(3)
        # Close event announcement.
        for i in range(5):
            if exists(self.get_image("login_close.png")):
                touch(self.get_image("login_close.png"))
                time.sleep(3)
            else:
                break

    @task_log
    def __task_source_center(self):
        touch(self.get_image("menu_source_center.png"))
        time.sleep(3)
        touch(self.get_image("source_exchange.png"))
        time.sleep(1.5)
        touch(self.get_image("source_harvest.png"))
        time.sleep(1.5)
        touch(self.get_image("source_receive.png"))
        time.sleep(3)
        # Exchange item.

        # Back to the home page.
        for i in range(5):
            if exists(self.get_image("button_back.png")):
                touch(self.get_image("button_back.png"))
                time.sleep(3)
            else:
                break

    def __change_operator(self, room:str):
        task = self.get_task("infrastructure")
        task.coordinates[room].click()
        time.sleep(5)
        # Release the operator.
        if not exists(self.get_image("operator_release.png")):
            touch(self.get_image("operator_info.png"))
            time.sleep(3)
        touch(self.get_image("operator_release.png"))
        time.sleep(1.5)
        if exists(self.get_image("button_ensure.png")):
            touch(self.get_image("button_ensure.png"))
            time.sleep(3)
        # Deploy the operator.
        touch(self.get_image("operator_deploy.png"))
        time.sleep(3)
        operator_count = {
            "center": 5,
            "trade_a": 3,
            "trade_b": 3,
            "manufacture_a": 2,
            "manufacture_b": 2,
            "manufacture_c": 2,
            "manufacture_d": 2,
            "dormitory_a": 5,
            "dormitory_b": 5,
            "dormitory_c": 5,
            "dormitory_d": 5,
            "meeting": 2,
            "office": 1
        }

        if operator_count[room] >= 1:
            task.coordinates["first_operator"].click()
            time.sleep(1)
        if operator_count[room] >= 2:
            task.coordinates["second_operator"].click()
            time.sleep(1)
        if operator_count[room] >= 3:
            task.coordinates["third_operator"].click()
            time.sleep(1)
        if operator_count[room] >= 4:
            task.coordinates["fourth_operator"].click()
            time.sleep(1)
        if operator_count[room] >= 5:
            task.coordinates["fifth_operator"].click()
            time.sleep(1)
        time.sleep(3)
        touch(self.get_image("operator_confirm.png"))
        time.sleep(5)
        if exists(self.get_image("operator_double_confirm.png")):
            touch(self.get_image("operator_double_confirm.png"))
            time.sleep(5)
        # Back to home page.
        if exists(self.get_image("button_back.png")):
            touch(self.get_image("button_back.png"))
            time.sleep(3)

    @task_log
    def __task_infrastructure(self):
        touch(self.get_image("menu_infrastructure.png"))
        time.sleep(5)
        if exists(self.get_image("infrastructure_notification.png")):
            touch(self.get_image("infrastructure_notification.png"))
            time.sleep(3)
            if exists(self.get_image("infrastructure_resource.png")):
                touch(self.get_image("infrastructure_resource.png"))
                time.sleep(1.5)
            if exists(self.get_image("infrastructure_coin.png")):
                touch(self.get_image("infrastructure_coin.png"))
                time.sleep(1.5)
            if exists(self.get_image("infrastructure_trust.png")):
                touch(self.get_image("infrastructure_trust.png"))
                time.sleep(1.5)
            if exists(self.get_image("infrastructure_to_do.png")):
                touch(self.get_image("infrastructure_to_do.png"))
                time.sleep(3)
        # Center.
        touch(self.get_image("infrastructure_center.png"))
        time.sleep(5)
        self.__change_operator("center")
        # Trading - A.
        self.__change_operator("trade_a")
        # Trading - B.
        self.__change_operator("trade_b")
        # Manufacturing - A.
        self.__change_operator("manufacture_a")
        # Manufacturing - B.
        self.__change_operator("manufacture_b")
        # Manufacturing - C.
        self.__change_operator("manufacture_c")
        # Manufacturing - D.
        self.__change_operator("manufacture_d")
        # Dormitory - A.
        self.__change_operator("dormitory_a")
        # Dormitory - B.
        self.__change_operator("dormitory_b")
        # Dormitory - C.
        self.__change_operator("dormitory_c")
        # Dormitory - D.
        self.__change_operator("dormitory_d")
        # Office.
        self.__change_operator("office")
        # Back to the home page.
        for i in range(5):
            if exists(self.get_image("button_back.png")):
                touch(self.get_image("button_back.png"))
                time.sleep(3)
            else:
                break

    @task_log
    def __task_event_quest(self):
        task = self.get_task("event_quest")
        try:
            touch(self.get_image("menu_terminal.png"))
            time.sleep(5)
            # Last quest.
            task.coordinates["last_quest"].click()
            time.sleep(3)
            for i in range(100):
                touch(self.get_image("quest_formation.png"))
                time.sleep(3)
                if exists(self.get_image("quest_break.png")):
                    touch(self.get_image("quest_cancel.png"))
                    time.sleep(5)
                    break
                touch(self.get_image("quest_start.png"))
                time.sleep(10)
                wait(self.get_image("quest_finish.png"), timeout=360, interval=15)
                time.sleep(5)
                touch(self.get_image("quest_finish.png"))
                time.sleep(5)
            self.__event_quest = True
        except Exception as e:
            print_message("Error", "Some errors have occurred in the event quest.")
            print_message("Error", str(e))
            print_message("Error", repr(e))
        finally:
            # Back to the home page.
            for i in range(5):
                if exists(self.get_image("button_back.png")):
                    touch(self.get_image("button_back.png"))
                    time.sleep(3)
                else:
                    break

    @task_log
    def __task_daily_quest(self):
        # Determine if event quests have been completed.
        if self.__event_quest == False:
            touch(self.get_image("menu_terminal.png"))
            time.sleep(5)
            touch(self.get_image("daily_page.png"))
            time.sleep(1.5)
            # Coin quest.
            if exists(self.get_image("daily_coin.png")):
                touch(self.get_image("daily_coin.png"))
                time.sleep(3)
                touch(self.get_image("daily_coin_ce_6.png"))
                time.sleep(3)
                for i in range(100):
                    touch(self.get_image("quest_formation.png"))
                    time.sleep(3)
                    if exists(self.get_image("quest_break.png")):
                        touch(self.get_image("quest_cancel.png"))
                        time.sleep(5)
                        break
                    touch(self.get_image("quest_start.png"))
                    time.sleep(10)
                    wait(self.get_image("quest_finish.png"), timeout=360, interval=15)
                    time.sleep(1.5)
                    touch(self.get_image("quest_finish.png"))
                    time.sleep(5)
            # Exp quest.
            elif exists(self.get_image("daily_exp.png")):
                touch(self.get_image("daily_exp.png"))
                time.sleep(3)
                touch(self.get_image("daily_exp_ls_6.png"))
                time.sleep(3)
                for i in range(100):
                    touch(self.get_image("quest_formation.png"))
                    time.sleep(3)
                    if exists(self.get_image("quest_break.png")):
                        touch(self.get_image("quest_cancel.png"))
                        time.sleep(5)
                        break
                    touch(self.get_image("quest_start.png"))
                    time.sleep(10)
                    wait(self.get_image("quest_finish.png"), timeout=360, interval=15)
                    time.sleep(1.5)
                    touch(self.get_image("quest_finish.png"))
                    time.sleep(5)
            # Back to the home page.
            for i in range(5):
                if exists(self.get_image("button_back.png")):
                    touch(self.get_image("button_back.png"))
                    time.sleep(3)
                else:
                    break

    def __recruit_tag(self):
        self.get_image("recruit_tag_top_senior.png")
        tag_list = [
            # Star 6.
            self.get_image("recruit_tag_top_senior.png"),
            # Star 5.
            # self.get_image("recruit_tag_senior.png"),
            # self.get_image("recruit_tag_summon.png"),
            # Star 4.
            self.get_image("recruit_tag_weaken.png"),
            self.get_image("recruit_tag_erupt.png"),
            self.get_image("recruit_tag_resurrection.png"),
            self.get_image("recruit_tag_move.png"),
            self.get_image("recruit_tag_special.png")
        ]
        for tag in tag_list:
            # Check combinations of tags.
            if isinstance(tag, list):
                match_flag = False
                for t in tag:
                    if exists(t):
                        if t == tag[-1]:
                            # All tags matched.
                            match_flag = True
                        else:
                            continue
                    else:
                        break
                # Tags matched & Select combinations of tags.
                if match_flag:
                    for t in tag:
                        touch(t)
                        time.sleep(1.5)
                    break
            # Check single tag.
            else:
                if exists(tag):
                    if tag == tag_list[0]:
                        input("[Recruit] Top senior. Please check.")
                        time.sleep(1)
                        continue
                    touch(tag)
                    time.sleep(3)
                    break

    @task_log
    def __task_recruit_center(self):
        task = self.get_task("recruit_center")
        self.get_image("recruit_ensure.png")


        touch(self.get_image("menu_recruit.png"))
        time.sleep(5)
        # Check whether acceleration is required.
        for i in range(4):
            if exists(self.get_image("recruit_accelerate.png")):
                touch(self.get_image("recruit_accelerate.png"))
                time.sleep(1.5)
                if exists(self.get_image("button_ensure.png")):
                    touch(self.get_image("button_ensure.png"))
                    time.sleep(3)
                else:
                    break
            else:
                break
        # Recruit the operator.
        for i in range(4):
            if exists(self.get_image("recruit_complete.png")):
                touch(self.get_image("recruit_complete.png"))
                time.sleep(5)
                touch(self.get_image("button_skip.png"))
                time.sleep(7)
                task.coordinates["blank_area"].click()
                time.sleep(3)
            else:
                break
        # Add recruit order.
        index = ["first", "second", "third", "fourth"]
        for i in range(len(index)):
            task.coordinates["{0}_archive".format(index[i])].click()
            time.sleep(3)
            task.coordinates["max_time"].click()
            time.sleep(1.5)
            self.__recruit_tag()
            time.sleep(3)
            touch(self.get_image("recruit_ensure.png"))
            time.sleep(1.5)
        # Back to the home page.
        for i in range(5):
            if exists(self.get_image("button_back.png")):
                touch(self.get_image("button_back.png"))
                time.sleep(3)
            else:
                break

    @task_log
    def __task_complete(self):
        touch(self.get_image("menu_task.png"))
        time.sleep(3)
        touch(self.get_image("task_receive.png"))
        time.sleep(1)

    def run_task(self):
        switch_tasks  = {
            "login": self.__task_login,
            "source_center": self.__task_source_center,
            "infrastructure": self.__task_infrastructure,
            "event_quest": self.__task_event_quest,
            "daily_quest": self.__task_daily_quest,
            "recruit_center": self.__task_recruit_center,
            "complete": self.__task_complete
        }

        self.task_process(switch_tasks)