#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : arknights.py
[Time]        : 2023/09/17 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.5
[Description] : Arknights project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.5"

import re
import requests
from base.game import Game
from base.task import Task
from base.common import *
from base.coordinate import Coordinate
from typing import Dict, List, Tuple
from airtest.core.api import *
from airtest.aircv import *

class Arknights(Game):
    def __init__(self, name="Arknights", country="Cn"):
        super().__init__(name, country)
        # Define game attribute.
        self.package_name = "com.hypergryph.arknights"
        self.resolution = (1920, 1080)
        # Recruit information.
        self.recruit_info = {
            "tags": [],
            "operators": {}
        }

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
                                     1.5).get_coordinate_dict()
            },
            {
                "trade_a": Coordinate(round(65/rcr_rsl[0], 4),
                                      round(310/rcr_rsl[1], 4),
                                      round(3/rcr_rsl[0], 4),
                                      round(3/rcr_rsl[1], 4),
                                      1.5).get_coordinate_dict()
            },
            {
                "trade_b": Coordinate(round(280/rcr_rsl[0], 4),
                                      round(310/rcr_rsl[1], 4),
                                      round(3/rcr_rsl[0], 4),
                                      round(3/rcr_rsl[1], 4),
                                      1.5).get_coordinate_dict()
            },
            {
                "manufacture_a": Coordinate(round(495/rcr_rsl[0], 4),
                                            round(310/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            1.5).get_coordinate_dict()
            },
            {
                "manufacture_b": Coordinate(round(65/rcr_rsl[0], 4),
                                            round(520/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            1.5).get_coordinate_dict()
            },
            {
                "manufacture_c": Coordinate(round(280/rcr_rsl[0], 4),
                                            round(520/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            1.5).get_coordinate_dict()
            },
            {
                "manufacture_d": Coordinate(round(495/rcr_rsl[0], 4),
                                            round(520/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            1.5).get_coordinate_dict()
            },
            {
                "dormitory_a": Coordinate(round(800/rcr_rsl[0], 4),
                                          round(310/rcr_rsl[1], 4),
                                          round(3/rcr_rsl[0], 4),
                                          round(3/rcr_rsl[1], 4),
                                          1.5).get_coordinate_dict()
            },
            {
                "dormitory_b": Coordinate(round(915/rcr_rsl[0], 4),
                                         round(415/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         1.5).get_coordinate_dict()
            },
            {
                "dormitory_c": Coordinate(round(800/rcr_rsl[0], 4),
                                         round(520/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         1.5).get_coordinate_dict()
            },
            {
                "dormitory_d": Coordinate(round(915/rcr_rsl[0], 4),
                                         round(625/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         1.5).get_coordinate_dict()
            },
            {
                "office": Coordinate(round(1265/rcr_rsl[0], 4),
                                     round(415/rcr_rsl[1], 4),
                                     round(3/rcr_rsl[0], 4),
                                     round(3/rcr_rsl[1], 4),
                                     1.5).get_coordinate_dict()
            },
            {
                "first_operator": Coordinate(round(485/rcr_rsl[0], 4),
                                             round(205/rcr_rsl[1], 4),
                                             round(3/rcr_rsl[0], 4),
                                             round(3/rcr_rsl[1], 4),
                                             0.5).get_coordinate_dict()
            },
            {
                "second_operator": Coordinate(round(485/rcr_rsl[0], 4),
                                              round(480/rcr_rsl[1], 4),
                                              round(3/rcr_rsl[0], 4),
                                              round(3/rcr_rsl[1], 4),
                                              0.5).get_coordinate_dict()
            },
            {
                "third_operator": Coordinate(round(625/rcr_rsl[0], 4),
                                             round(205/rcr_rsl[1], 4),
                                             round(3/rcr_rsl[0], 4),
                                             round(3/rcr_rsl[1], 4),
                                             0.5).get_coordinate_dict()
            },
            {
                "fourth_operator": Coordinate(round(625/rcr_rsl[0], 4),
                                              round(480/rcr_rsl[1], 4),
                                              round(3/rcr_rsl[0], 4),
                                              round(3/rcr_rsl[1], 4),
                                              0.5).get_coordinate_dict()
            },
            {
                "fifth_operator": Coordinate(round(765/rcr_rsl[0], 4),
                                             round(205/rcr_rsl[1], 4),
                                             round(3/rcr_rsl[0], 4),
                                             round(3/rcr_rsl[1], 4),
                                             0.5).get_coordinate_dict()
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
                                         3).get_coordinate_dict()
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
                                         3).get_coordinate_dict()
            },
            {
                "first_archive": Coordinate(round(325/rcr_rsl[0], 4),
                                            round(290/rcr_rsl[1], 4),
                                            round(5/rcr_rsl[0], 4),
                                            round(5/rcr_rsl[1], 4),
                                            1).get_coordinate_dict()
            },
            {
                "second_archive": Coordinate(round(955/rcr_rsl[0], 4),
                                             round(290/rcr_rsl[1], 4),
                                             round(5/rcr_rsl[0], 4),
                                             round(5/rcr_rsl[1], 4),
                                             1).get_coordinate_dict()
            },
            {
                "third_archive": Coordinate(round(325/rcr_rsl[0], 4),
                                            round(570/rcr_rsl[1], 4),
                                            round(5/rcr_rsl[0], 4),
                                            round(5/rcr_rsl[1], 4),
                                            1).get_coordinate_dict()
            },
            {
                "fourth_archive": Coordinate(round(955/rcr_rsl[0], 4),
                                             round(570/rcr_rsl[1], 4),
                                             round(5/rcr_rsl[0], 4),
                                             round(5/rcr_rsl[1], 4),
                                             1).get_coordinate_dict()
            },
            {
                "first_tag": Coordinate(round(450/rcr_rsl[0], 4),
                                        round(385/rcr_rsl[1], 4),
                                        round(60/rcr_rsl[0], 4),
                                        round(20/rcr_rsl[1], 4),
                                        0.5).get_coordinate_dict()
            },
            {
                "second_tag": Coordinate(round(615/rcr_rsl[0], 4),
                                         round(385/rcr_rsl[1], 4),
                                         round(60/rcr_rsl[0], 4),
                                         round(20/rcr_rsl[1], 4),
                                         0.5).get_coordinate_dict()
            },
            {
                "third_tag": Coordinate(round(780/rcr_rsl[0], 4),
                                        round(385/rcr_rsl[1], 4),
                                        round(60/rcr_rsl[0], 4),
                                        round(20/rcr_rsl[1], 4),
                                        0.5).get_coordinate_dict()
            },
            {
                "fourth_tag": Coordinate(round(450/rcr_rsl[0], 4),
                                         round(455/rcr_rsl[1], 4),
                                         round(60/rcr_rsl[0], 4),
                                         round(20/rcr_rsl[1], 4),
                                         0.5).get_coordinate_dict()
            },
            {
                "fifth_tag": Coordinate(round(615/rcr_rsl[0], 4),
                                        round(455/rcr_rsl[1], 4),
                                        round(60/rcr_rsl[0], 4),
                                        round(20/rcr_rsl[1], 4),
                                        0.5).get_coordinate_dict()
            },
            {
                "max_time": Coordinate(round(450/rcr_rsl[0], 4),
                                       round(295/rcr_rsl[1], 4),
                                       round(3/rcr_rsl[0], 4),
                                       round(3/rcr_rsl[1], 4),
                                       0.5).get_coordinate_dict()
            },
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Complete.
        task_name = "complete"
        task_mode = "finish_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

    def __back_homepage(self):
        """
            Back to the home page.
        """

        for _ in range(5):
            if self.exists("button_back"):
                self.touch("button_back", 1.5)
            else:
                break

    @task_log
    def __task_login(self):
        # Game updates will cause the program error.
        self.wait("login_start", timeout=300, interval=10)
        self.touch("login_start", 5)
        self.touch("login_enter", 30)
        if self.exists("login_rewards"):
            # Receive login rewards
            self.touch("login_rewards", 1.5)
        # Close event announcement.
        for _ in range(5):
            if self.exists("login_close"):
                self.touch("login_close", 3)
            else:
                break

    @task_log
    def __task_source_center(self):
        self.touch("menu_source_center")
        self.touch("source_exchange")
        self.touch("source_harvest")
        self.touch("source_receive")
        # TODO Exchange item.
        self.__back_homepage()

    def __change_operator(self, room:str):
        task = self.get_task("infrastructure")
        for _ in range(3):
            task.coordinates[room].click()
            if self.exists("operator_info"):
                break
        # Release the operator.
        if not self.exists("operator_release"):
            self.touch("operator_info")
        self.touch("operator_release")
        if self.exists("button_ensure"):
            self.touch("button_ensure")
        # Deploy the operator.
        self.touch("operator_deploy")
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
        if operator_count[room] >= 2:
            task.coordinates["second_operator"].click()
        if operator_count[room] >= 3:
            task.coordinates["third_operator"].click()
        if operator_count[room] >= 4:
            task.coordinates["fourth_operator"].click()
        if operator_count[room] >= 5:
            task.coordinates["fifth_operator"].click()
        self.touch("operator_confirm")
        if self.exists("operator_double_confirm"):
            self.touch("operator_double_confirm")
        if self.exists("button_back"):
            self.touch("button_back", 1.5)

    @task_log
    def __task_infrastructure(self):
        self.touch("menu_infrastructure", 3)
        if self.exists("infrastructure_notification"):
            self.touch("infrastructure_notification")
            if self.exists("infrastructure_resource"):
                self.touch("infrastructure_resource")
            if self.exists("infrastructure_coin"):
                self.touch("infrastructure_coin")
            if self.exists("infrastructure_trust"):
                self.touch("infrastructure_trust")
            if self.exists("infrastructure_to_do"):
                self.touch("infrastructure_to_do")
        # Center.
        self.touch("infrastructure_center")
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
        self.__back_homepage()

    @task_log
    def __task_event_quest(self):
        task = self.get_task("event_quest")
        try:
            self.touch("menu_terminal", 1.5)
            # Last quest.
            task.coordinates["last_quest"].click()
            for _ in range(100):
                self.touch("quest_formation", 1.5)
                if self.exists("quest_break_pharmacist") or self.exists("quest_break_stone"):
                    self.touch("quest_cancel")
                    break
                self.touch("quest_start")
                try:
                    self.wait("quest_finish", timeout=300, interval=10)
                except:
                    if self.exists("quest_level_up"):
                        self.touch("quest_level_up", 1.5)
                self.touch("quest_finish", 3)
            self.__event_quest = True
        except Exception as e:
            print_message("Error", "Some errors have occurred in the event quest.")
            print_message("Error", str(e))
            print_message("Error", repr(e))
        finally:
            self.__back_homepage()


    @task_log
    def __task_daily_quest(self):
        # Determine if event quests have been completed.
        if self.__event_quest == False:
            self.touch("menu_terminal", 1.5)
            self.touch("daily_page", 1.5)
            # Coin quest.
            if self.exists("daily_coin"):
                self.touch("daily_coin", 1.5)
                self.touch("daily_coin_ce_6", 1.5)
            # Exp quest.
            elif self.exists("daily_exp"):
                self.touch("daily_exp", 1.5)
                self.touch("daily_exp_ls_6", 1.5)

            for _ in range(100):
                self.touch("quest_formation", 1.5)
                if self.exists("quest_break_pharmacist") or self.exists("quest_break_stone"):
                    self.touch("quest_cancel")
                    break
                self.touch("quest_start")
                try:
                    self.wait("quest_finish", timeout=300, interval=10)
                except:
                    if self.exists("quest_level_up"):
                        self.touch("quest_level_up", 1.5)
                self.touch("quest_finish", 3)
            self.__back_homepage()

    def get_operators(self) -> Tuple[List[str], List[dict]]:
        """
            Get the list of all tags and operators information by crawling the official wiki.
        """

        tags = []
        operators = []
        session = requests.Session()
        headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                    "Referer": "https://www.pixiv.net/"
                }
        official_website = r"https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88"
        rsp = session.get(url=official_website, headers=headers, verify=False)
        # Get operators information by regularizing the response text.
        data_ptn = re.compile("data-zh=.*? data-group=\".*?\"")
        operator_property = data_ptn.findall(rsp.text)
        operators_info = []
        for op in operator_property:
            operator_info = {}
            for kv in op.split("\" "):
                operator_info[kv.split("=")[0]] = kv.split("\"")[1]
            operators_info.append(operator_info)
        for operator_info in operators_info:
            # Only count publicly recruited operator. e.g. data-obtain_method="公开招募, 主线剧情".
            if "公开招募" in operator_info["data-obtain_method"] and 0 < int(operator_info["data-rarity"]) < 5:
                operator = {}
                # e.g. data-zh="Lancet-2".
                operator["name"] = operator_info["data-zh"]
                # e.g. data-rarity="0".
                operator["rarity"] = int(operator_info["data-rarity"]) + 1
                # e.g. data-profession="医疗" data-position="远程位" data-tag="支援机械 治疗"
                operator["tag"] = [operator_info["data-profession"] + "干员", operator_info["data-position"]] +\
                                operator_info["data-tag"].split(" ")
                for ot in operator["tag"]:
                    if ot not in tags:
                        tags.append(ot)
                operators.append(operator)
        return tags, operators

    def __recruit_tag(self, coordinates: Dict[str, Coordinate]):
        """
            Get the best tag combination and click.

            Attributes:
                coordinates - Used to get the tag area based on the actual coordinates.
        """

        # Get the list of all tags and operators information.
        if self.recruit_info["tags"] == [] and self.recruit_info["operators"] == {}:
            self.recruit_info["tags"], self.recruit_info["operators"] = self.get_operators()
        # Initialize tag information.
        tags_info = [
            { "name": "first_tag",
              "content": "",
              "rectangle": coordinates["first_tag"].get_click_area() },
            { "name": "second_tag",
              "content": "",
              "rectangle": coordinates["second_tag"].get_click_area() },
            { "name": "third_tag",
              "content": "",
              "rectangle": coordinates["third_tag"].get_click_area() },
            { "name": "fourth_tag",
              "content": "",
              "rectangle": coordinates["fourth_tag"].get_click_area() },
            { "name": "fifth_tag",
              "content": "",
              "rectangle": coordinates["fifth_tag"].get_click_area() },
        ]

        # Get screenshot.
        screen = G.DEVICE.snapshot()
        for ti in tags_info:
            # Crop tag area.
            tag_image = aircv.crop_image(screen, ti["rectangle"])
            tag_content = image_to_string(tag_image)
            if tag_content in self.recruit_info["tags"]:
                ti["content"] = tag_content

        # Get all possible combinations.
        tag_combo = []
        for ti in tags_info:
            if ti["content"] != "":
                if len(tag_combo) > 0:
                    tag_combo = tag_combo + [tcl + [ti["content"]] for tcl in tag_combo] + [[ti["content"]]]
                else:
                    tag_combo.append([ti["content"]])

        scoring_sheet = {}
        for tc in tag_combo:
            for operator in self.recruit_info["operators"]:
                if all(tct in operator["tag"] for tct in tc):
                    if ",".join(tc) not in scoring_sheet.keys():
                        scoring_sheet[",".join(tc)] = [operator["rarity"]]
                    else:
                        scoring_sheet[",".join(tc)].append(operator["rarity"])
                else:
                    continue
        for ssk in scoring_sheet.keys():
            scoring_sheet[ssk] = round(len([x for x in scoring_sheet[ssk] if x > 3 or x == 1]) / len(scoring_sheet[ssk]) , 4) * 100
        # Sort tag combinations by probability.
        target_tag = sorted(scoring_sheet.items(), key=lambda x:x[1])[-1][0].split(",")
        print(target_tag)
        for ti in tags_info:
            if ti["content"] in target_tag:
                coordinates[ti["name"]].click()

    def __recruit(self, task):
        # Check whether acceleration is required.
        for _ in range(4):
            if self.exists("recruit_accelerate"):
                self.touch("recruit_accelerate")
                if self.exists("button_ensure"):
                    self.touch("button_ensure")
                else:
                    break
            else:
                break

        # Recruit the operator.
        for _ in range(4):
            if self.exists("recruit_complete"):
                self.touch("recruit_complete", 5)
                self.touch("button_skip", 3)
                task.coordinates["blank_area"].click()
            else:
                break

        # Add recruit order.
        index = ["first", "second", "third", "fourth"]
        for i in range(len(index)):
            task.coordinates["{0}_archive".format(index[i])].click()
            # Human-operated recruitment of six-star operator.
            if self.exists("recruit_tag_top_senior"):
                self.touch("button_back", 1.5)
                continue
            else:
                task.coordinates["max_time"].click()
                self.__recruit_tag(task.coordinates)
                self.touch("recruit_ensure")

    @task_log
    def __task_recruit_center(self):
        task = self.get_task("recruit_center")
        self.touch("menu_recruit", 3)
        self.__recruit(task)
        self.__back_homepage()

    @task_log
    def __task_complete(self):
        self.touch("menu_task", 1.5)
        self.touch("task_receive")

    def __special_task_recruit(self):
        task = self.get_task("recruit_center")
        for _ in range(100):
            self.__recruit(task)

    def run_task(self, task:List[str]=None, special_task:List[str]=None):
        # Collection of tasks and special tasks.
        switch_tasks  = {
            "login": self.__task_login,
            "source_center": self.__task_source_center,
            "infrastructure": self.__task_infrastructure,
            "event_quest": self.__task_event_quest,
            "daily_quest": self.__task_daily_quest,
            "recruit_center": self.__task_recruit_center,
            "complete": self.__task_complete,
            "[special]recruit": self.__special_task_recruit
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