#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : princess_connect_re_dive_cn.py
[Time]        : 2023/09/10 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.3
[Description] : Princess connect re:dive project.
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

class PrincessConnectReDive(Game):
    def __init__(self, name="Princess_Connect_Re_Dive", country="Cn"):
        super().__init__(name, country)
        # Define game attribute.
        self.package_name = "com.bilibili.priconne"
        self.activity_name = "com.bilibili.permission.PermissionActivity"
        self.resolution = (1280, 720)

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
        task_coordinates = [
            {
                "blank_area": Coordinate(round(20/rcr_rsl[0], 4),
                                         round(135/rcr_rsl[1], 4),
                                         round(5/rcr_rsl[0], 4),
                                         round(5/rcr_rsl[1], 4),
                                         10).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Explore.
        task_name = "explore"
        task_mode = "random_task"
        task_coordinates = [
            {
                "top_level": Coordinate(round(950/rcr_rsl[0], 4),
                                        round(200/rcr_rsl[1], 4),
                                        round(5/rcr_rsl[0], 4),
                                        round(5/rcr_rsl[1], 4),
                                        3).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Shopping.
        task_name = "shopping"
        task_mode = "random_task"
        task_coordinates = [
            {
                "buy_button": Coordinate(round(1050/rcr_rsl[0], 4),
                                         round(585/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         3).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Guild.
        task_name = "guild"
        task_mode = "random_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Home.
        task_name = "home"
        task_mode = "random_task"
        task = Task(task_name)
        self.tasks[task_mode].append(task)

        # Gashapon.
        task_name = "gashapon"
        task_mode = "random_task"
        task_coordinates = [
            {
                "normal_button": Coordinate(round(1150/rcr_rsl[0], 4),
                                            round(95/rcr_rsl[1], 4),
                                            round(3/rcr_rsl[0], 4),
                                            round(3/rcr_rsl[1], 4),
                                            3).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Dungeons.
        task_name = "dungeons"
        task_mode = "random_task"
        task_coordinates = [
            {
                # Penultimate.
                "level_button": Coordinate(round(795/rcr_rsl[0], 4),
                                           round(280/rcr_rsl[1], 4),
                                           round(10/rcr_rsl[0], 4),
                                           round(10/rcr_rsl[1], 4),
                                           3).get_coordinate_dict()
                # Last.
                # "level_button": Coordinate(round(1100/rcr_rsl[0], 4),
                #                            round(280/rcr_rsl[1], 4),
                #                            round(10/rcr_rsl[0], 4),
                #                            round(10/rcr_rsl[1], 4),
                #                            10).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Arena.
        task_name = "arena"
        task_mode = "random_task"
        task_coordinates = [
            {
                "blank_area": Coordinate(round(20/rcr_rsl[0], 4),
                                         round(175/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         3).get_coordinate_dict()
            },
            {
                "top_player": Coordinate(round(940/rcr_rsl[0], 4),
                                         round(225/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Princess arena.
        task_name = "princess_arena"
        task_mode = "finish_task"
        task_coordinates = [
            {
                "blank_area": Coordinate(round(20/rcr_rsl[0], 4),
                                         round(175/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         3).get_coordinate_dict()
            },
            {
                "top_player": Coordinate(round(940/rcr_rsl[0], 4),
                                         round(225/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         5).get_coordinate_dict()
            }
        ]
        task = Task(task_name, task_coordinates)
        self.tasks[task_mode].append(task)

        # Quest.
        task_name = "quest"
        task_mode = "finish_task"
        task_coordinates = [
            {
                "next_quest": Coordinate(round(45/rcr_rsl[0], 4),
                                         round(370/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         3).get_coordinate_dict()
            }
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
        task = self.get_task("login")
        wait(self.get_image("login_menu.png"), timeout=360, interval=15)
        time.sleep(1)
        task.coordinates["blank_area"].click()
        # Check if there is an update and update if available.
        if exists(self.get_image("button_confirm_blue.png")):
            touch(self.get_image("button_confirm_blue.png"))
            time.sleep(60)
        # Check special events such as birthdays and events.
        for _ in range(10):
            if exists(self.get_image("login_skip.png")):
                touch(self.get_image("login_skip.png"))
                time.sleep(7)
                if exists(self.get_image("button_close.png")):
                    touch(self.get_image("button_close.png"))
                    time.sleep(3)
            else:
                # Already logged in today.
                if exists(self.get_image("button_close.png")):
                    touch(self.get_image("button_close.png"))
                    time.sleep(3)
            if exists(self.get_image("bar_main_active.png")):
                break
            else:
                task.coordinates["blank_area"].click()
            time.sleep(3)

    @task_log
    def __task_explore(self):
        task = self.get_task("explore")
        if exists(self.get_image("bar_adventure_active.png")):
            touch(self.get_image("bar_adventure_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_adventure.png"))
            time.sleep(5)
        touch(self.get_image("entrance_explore.png"))
        time.sleep(3)
        touch(self.get_image("explore_exp.png"))
        time.sleep(3)
        task.coordinates["top_level"].click()
        touch(self.get_image("explore_attack.png"))
        time.sleep(1.5)
        touch(self.get_image("button_confirm_blue.png"))
        time.sleep(5)
        touch(self.get_image("explore_mana.png"))
        time.sleep(3)
        task.coordinates["top_level"].click()
        touch(self.get_image("explore_attack.png"))
        time.sleep(1.5)
        touch(self.get_image("button_confirm_blue.png"))
        time.sleep(5)
        touch(self.get_image("explore_return.png"))
        time.sleep(3)

    @task_log
    def __task_shopping(self):
        task = self.get_task("shopping")
        if exists(self.get_image("bar_main_active.png")):
            touch(self.get_image("bar_main_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_main.png"))
            time.sleep(5)
        touch(self.get_image("menu_shop.png"))
        time.sleep(3)
        touch(self.get_image("shop_all.png"))
        time.sleep(1)
        task.coordinates["buy_button"].click()
        touch(self.get_image("button_confirm_blue.png"))
        time.sleep(3)
        touch(self.get_image("button_confirm_blue.png"))
        time.sleep(3)

    @task_log
    def __task_guild(self):
        if exists(self.get_image("bar_main_active.png")):
            touch(self.get_image("bar_main_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_main.png"))
            time.sleep(5)
        touch(self.get_image("menu_guild.png"))
        time.sleep(7)
        if exists(self.get_image("button_close.png")):
            touch(self.get_image("button_close.png"))
            time.sleep(3)
        if exists(self.get_image("button_confirm_white.png")):
            touch(self.get_image("button_confirm_white.png"))
            time.sleep(3)
        touch(self.get_image("guild_member.png"))
        time.sleep(3)
        touch(self.get_image("guild_like.png"))
        time.sleep(1.5)
        touch(self.get_image("button_confirm_blue.png"))
        time.sleep(3)

    @task_log
    def __task_home(self):
        touch(self.get_image("bar_home.png"))
        time.sleep(3)
        if exists(self.get_image("button_close.png")):
            touch(self.get_image("button_close.png"))
            time.sleep(3)
        touch(self.get_image("home_receive.png"))
        time.sleep(3)
        touch(self.get_image("button_close.png"))
        time.sleep(1.5)

    @task_log
    def __task_gashapon(self):
        task = self.get_task("gashapon")
        touch(self.get_image("bar_gashapon.png"))
        time.sleep(5)
        if exists(self.get_image("button_close.png")):
            touch(self.get_image("button_close.png"))
            time.sleep(3)
        task.coordinates["normal_button"].click()
        touch(self.get_image("gashapon_free.png"))
        time.sleep(1.5)
        touch(self.get_image("button_confirm_blue.png"))
        time.sleep(5)
        touch(self.get_image("button_confirm_white.png"))
        time.sleep(3)

    @task_log
    def __task_dungeons(self):
        task = self.get_task("dungeons")
        if exists(self.get_image("bar_adventure_active.png")):
            touch(self.get_image("bar_adventure_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_adventure.png"))
            time.sleep(5)
        touch(self.get_image("entrance_dungeons.png"))
        time.sleep(3)
        task.coordinates["level_button"].click()
        touch(self.get_image("dungeons_skip.png"))
        time.sleep(10)
        touch(self.get_image("button_confirm_white.png"))
        time.sleep(3)

    @task_log
    def __task_arena(self):
        task = self.get_task("arena")
        if exists(self.get_image("bar_adventure_active.png")):
            touch(self.get_image("bar_adventure_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_adventure.png"))
            time.sleep(5)
        touch(self.get_image("entrance_arena.png"))
        time.sleep(5)
        task.coordinates["blank_area"].click()
        touch(self.get_image("arena_receive.png"))
        time.sleep(3)
        touch(self.get_image("button_confirm_white.png"))
        time.sleep(3)
        task.coordinates["top_player"].click()
        time.sleep(3)
        touch(self.get_image("button_attack.png"))
        time.sleep(10)
        if exists(self.get_image("arena_skip.png")):
            touch(self.get_image("arena_skip.png"))
            time.sleep(3)
        else:
            wait(self.get_image("button_next.png"), timeout=360, interval=15)
            time.sleep(1)
        touch(self.get_image("button_next.png"))
        time.sleep(5)
        if exists(self.get_image("button_confirm_white.png")):
            touch(self.get_image("button_confirm_white.png"))
            time.sleep(3)

    @task_log
    def __task_princess_arena(self):
        task = self.get_task("princess_arena")
        if exists(self.get_image("bar_adventure_active.png")):
            touch(self.get_image("bar_adventure_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_adventure.png"))
            time.sleep(5)
        touch(self.get_image("entrance_princess_arena.png"))
        time.sleep(5)
        task.coordinates["blank_area"].click()
        touch(self.get_image("arena_receive.png"))
        time.sleep(3)
        touch(self.get_image("button_confirm_white.png"))
        time.sleep(3)
        task.coordinates["top_player"].click()
        time.sleep(3)
        touch(self.get_image("arena_team2.png"))
        time.sleep(3)
        touch(self.get_image("arena_team3.png"))
        time.sleep(3)
        touch(self.get_image("button_attack.png"))
        time.sleep(15)
        if exists(self.get_image("arena_skip.png")):
            touch(self.get_image("arena_skip.png"))
            time.sleep(3)
        else:
            wait(self.get_image("button_next.png"), timeout=360, interval=15)
            time.sleep(1)
        touch(self.get_image("button_next.png"))
        time.sleep(5)
        if exists(self.get_image("button_confirm_white.png")):
            touch(self.get_image("button_confirm_white.png"))
            time.sleep(3)

    @task_log
    def __task_quest(self):
        task = self.get_task("quest")
        if exists(self.get_image("bar_adventure_active.png")):
            touch(self.get_image("bar_adventure_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_adventure.png"))
            time.sleep(5)
        pass
        if exists(self.get_image("quest_entrance.png")):
            touch(self.get_image("quest_entrance.png"))
            time.sleep(5)
            if exists(self.get_image("button_menu.png")):
                touch(self.get_image("button_menu.png"))
                time.sleep(5)
                touch(self.get_image("button_auto.png"))
                time.sleep(5)
                wait(self.get_image("quest_map.png"))
                time.sleep(1)
                # ???.
                if exists(self.get_image("button_close.png")):
                    touch(self.get_image("button_close.png"))
                    time.sleep(5)
                touch(self.get_image("quest_map.png"))
                time.sleep(5)
            # ???.
            touch(self.get_image("quest_very_hard_boss.png"))
            time.sleep(5)
            touch(self.get_image("quest_challenge.png"))
            time.sleep(5)
            touch(self.get_image("button_attack.png"))
            time.sleep(5)
            wait(self.get_image("button_next.png"))
            time.sleep(1)
            for _ in range(2):
                touch(self.get_image("button_next.png"))
                time.sleep(3)
            if exists(self.get_image("button_menu.png")):
                touch(self.get_image("button_menu.png"))
                time.sleep(5)
                touch(self.get_image("button_auto.png"))
                time.sleep(5)
                wait(self.get_image("quest_map.png"))
                time.sleep(1)
                touch(self.get_image("quest_map.png"))
                time.sleep(5)
            touch(self.get_image("quest_character.png"))
            time.sleep(5)
            for _ in range(5):
                for _ in range(2):
                    touch(self.get_image("quest_add.png"))
                    time.sleep(1)
                touch(self.get_image("quest_skip.png"))
                time.sleep(3)
                touch(self.get_image("button_confirm_blue.png"))
                time.sleep(5)
                touch(self.get_image("button_confirm_white.png"))
                time.sleep(5)
                if exists(self.get_image("button_confirm_white.png")):
                    touch(self.get_image("button_confirm_white.png"))
                    time.sleep(5)
                # ??? shop.
                if exists(self.get_image("quest_buy.png")):
                    touch(self.get_image("quest_cancel.png"))
                    time.sleep(5)
                task.coordinates["next_quest"].click()
            touch(self.get_image("quest_cancel.png"))
            time.sleep(5)
            touch(self.get_image("task_receive.png"))
            time.sleep(5)
            touch(self.get_image("button_close.png"))
            time.sleep(5)

    @task_log
    def __task_complete(self):
        if exists(self.get_image("bar_main_active.png")):
            touch(self.get_image("bar_main_active.png"))
            time.sleep(5)
        else:
            touch(self.get_image("bar_main.png"))
            time.sleep(5)
        touch(self.get_image("menu_task.png"))
        time.sleep(5)
        touch(self.get_image("task_receive.png"))
        time.sleep(3)

    def run_task(self):
        switch_tasks  = {
            "login": self.__task_login,
            "explore": self.__task_explore,
            "shopping": self.__task_shopping,
            "guild": self.__task_guild,
            "home": self.__task_home,
            "gashapon": self.__task_gashapon,
            "dungeons": self.__task_dungeons,
            "arena": self.__task_arena,
            "princess_arena": self.__task_princess_arena,
            "quest": self.__task_quest,
            "complete": self.__task_complete
        }

        self.task_process(switch_tasks)