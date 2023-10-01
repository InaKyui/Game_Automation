#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : princess_connect_re_dive_cn.py
[Time]        : 2023/10/01 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.6
[Description] : Princess connect re:dive project.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.6"

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
                                        1).get_coordinate_dict()
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
                                         0.5).get_coordinate_dict()
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
                                            1.5).get_coordinate_dict()
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
                # "level_button": Coordinate(round(795/rcr_rsl[0], 4),
                #                            round(280/rcr_rsl[1], 4),
                #                            round(10/rcr_rsl[0], 4),
                #                            round(10/rcr_rsl[1], 4),
                #                            1.5).get_coordinate_dict()
                # Last.
                "level_button": Coordinate(round(1100/rcr_rsl[0], 4),
                                           round(280/rcr_rsl[1], 4),
                                           round(10/rcr_rsl[0], 4),
                                           round(10/rcr_rsl[1], 4),
                                           1.5).get_coordinate_dict()
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
                                         1.5).get_coordinate_dict()
            },
            {
                "top_player": Coordinate(round(940/rcr_rsl[0], 4),
                                         round(225/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         3).get_coordinate_dict()
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
                                         1.5).get_coordinate_dict()
            },
            {
                "top_player": Coordinate(round(940/rcr_rsl[0], 4),
                                         round(225/rcr_rsl[1], 4),
                                         round(3/rcr_rsl[0], 4),
                                         round(3/rcr_rsl[1], 4),
                                         3).get_coordinate_dict()
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
                                         0.1).get_coordinate_dict()
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
        self.wait("login_menu", timeout=300, interval=10)
        task.coordinates["blank_area"].click()
        # Check if there is an update and update if available.
        self.exists_and_touch("button_confirm_blue", 60)
        # Check special events such as birthdays and events.
        for _ in range(10):
            if self.exists_and_touch("login_skip", 1.5):
                # TODO Check Birthdays event.
                self.exists_and_touch("button_confirm_white")
            elif self.exists_and_touch("button_close", 1.5):
                pass
            else:
                if self.exists("bar_main_active"):
                    break
                else:
                    task.coordinates["blank_area"].click()

    @task_log
    def __task_explore(self):
        task = self.get_task("explore")
        if not self.exists_and_touch("bar_adventure_active", 2.5):
            self.touch("bar_adventure", 2.5)
        self.touch("entrance_explore", 1.5)
        self.touch("explore_exp")
        task.coordinates["top_level"].click()
        self.touch("explore_attack", 1.5)
        self.touch("button_confirm_blue", 3)
        self.touch("explore_mana")
        task.coordinates["top_level"].click()
        self.touch("explore_attack", 1.5)
        self.touch("button_confirm_blue", 3)
        self.touch("explore_return")

    @task_log
    def __task_shopping(self):
        task = self.get_task("shopping")
        if not self.exists_and_touch("bar_main_active", 2.5):
            self.touch("bar_main", 2.5)
        self.touch("menu_shop", 1.5)
        self.touch("shop_all")
        task.coordinates["buy_button"].click()
        self.touch("button_confirm_blue")
        self.touch("button_confirm_blue")

    @task_log
    def __task_guild(self):
        if self.exists_and_touch("bar_main_active", 2.5):
            self.touch("bar_main", 2.5)
        self.touch("menu_guild", 3)
        for _ in range(3):
            if self.exists_and_touch("button_close", 1.5):
                pass
            elif self.exists_and_touch("button_confirm_white", 1.5):
                pass
            else:
                break
        self.touch("guild_member", 3)
        self.touch("guild_like")
        self.touch("button_confirm_blue")

    @task_log
    def __task_home(self):
        self.touch("bar_home", 2.5)
        self.exists_and_touch("button_close")
        self.touch("home_receive")
        self.touch("button_close")

    @task_log
    def __task_gashapon(self):
        task = self.get_task("gashapon")
        self.touch("bar_gashapon", 3)
        self.exists_and_touch("button_close")
        task.coordinates["normal_button"].click()
        self.touch("gashapon_free")
        self.touch("button_confirm_blue", 3)
        self.touch("button_confirm_white")

    @task_log
    def __task_dungeons(self):
        task = self.get_task("dungeons")
        if not self.exists_and_touch("bar_adventure_active", 2.5):
            self.touch("bar_adventure", 2.5)
        self.touch("entrance_dungeons")
        task.coordinates["level_button"].click()
        self.touch("dungeons_skip", 7)
        self.touch("button_confirm_white")

    @task_log
    def __task_arena(self):
        task = self.get_task("arena")
        if not self.exists_and_touch("bar_adventure_active", 2.5):
            self.touch("bar_adventure", 2.5)
        self.touch("entrance_arena", 3)
        for _ in range(3):
            if self.exists_and_touch("arena_receive"):
                self.touch("button_confirm_white")
                break
            else:
                task.coordinates["blank_area"].click()
        task.coordinates["top_player"].click()
        self.touch("button_attack")
        self.wait("arena_skip", timeout=30, interval=3)
        for _ in range(3):
            try:
                self.touch("arena_skip", 3)
                self.wait("button_next", timeout=15, interval=3)
                break
            except:
                continue
        self.touch("button_next", 3)
        # Ranking move up.
        self.exists_and_touch("button_confirm_white")

    @task_log
    def __task_princess_arena(self):
        task = self.get_task("princess_arena")
        if not self.exists_and_touch("bar_adventure_active", 2.5):
            self.touch("bar_adventure", 2.5)
        self.touch("entrance_princess_arena", 3)
        for _ in range(3):
            if self.exists_and_touch("arena_receive"):
                self.touch("button_confirm_white")
                break
            else:
                task.coordinates["blank_area"].click()
        task.coordinates["top_player"].click()
        self.touch("arena_team2")
        self.touch("arena_team3")
        self.touch("button_attack")
        self.wait("arena_skip", timeout=30, interval=3)
        for _ in range(3):
            try:
                self.touch("arena_skip", 3)
                self.wait("button_next", timeout=15, interval=3)
                break
            except:
                continue
        self.touch("button_next", 3)
        # Ranking move up.
        self.exists_and_touch("button_confirm_white")

    @task_log
    def __task_quest(self):
        task = self.get_task("quest")
        if not self.exists_and_touch("bar_adventure_active", 2.5):
            self.touch("bar_adventure", 2.5)
        # Checking the existence of the events.
        if self.exists("quest_entrance"):
            self.touch("quest_entrance", 3)
        elif self.exists("quest_rerun_entrance"):
            self.touch("quest_rerun_entrance", 3)
        else:
            return
        # Special scenario dialogues appear.
        if self.exists("button_menu"):
            self.touch("button_menu")
            self.touch("button_auto")
            self.wait("button_close", timeout=180, interval=5)
            self.touch("button_close", 1.5)
            self.touch("quest_map", 3)
        # No special scenario.
        else:
            self.exists_and_touch("button_close", 1.5)
        self.touch("quest_very_hard_boss")
        self.touch("quest_challenge")
        self.touch("button_attack", 10)
        # Check acceleration and auto are on.
        if self.exists("quest_acceleration_off") and \
           not self.exists("quest_acceleration_on"):
            self.touch("quest_acceleration_off")
        if self.exists("quest_auto_off") and \
           not self.exists("quest_auto_on"):
            self.touch("quest_auto_off")
        self.wait("button_next", timeout=60, interval=5)
        self.touch("button_next", 7)
        self.touch("button_next", 3)
        # Defeat a certain number of bosses to trigger special conversations.
        if self.exists_and_touch("button_menu"):
            self.touch("button_auto")
            # TODO Check button.
            self.wait("quest_map", timeout=60, interval=5)
            self.touch("quest_map", 3)
        self.touch("quest_character")
        for cycle in range(5):
            for _ in range(2):
                self.touch("quest_add")
            self.touch("quest_skip")
            self.touch("button_confirm_blue", 5)
            self.touch("button_confirm_white", 1.5)
            # Special stores appear.
            if self.exists("quest_shop_buy"):
                self.touch("quest_shop_cancel")
            if cycle < 4:
                task.coordinates["next_quest"].click()
            else:
                self.touch("quest_cancel")
        self.touch("quest_task", 1.5)
        self.touch("task_receive")
        self.touch("button_close")

    @task_log
    def __task_complete(self):
        if not self.exists_and_touch("bar_main_active", 2.5):
            self.touch("bar_main", 2.5)
        self.touch("menu_task")
        self.touch("task_receive")

    def run_task(self, task:str=None, special_task:str=None):
        # Collection of tasks and special tasks.
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