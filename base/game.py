#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : game.py
[Time]        : 2023/06/07 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.3
[Description] : Class game.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.3"

import os
import json
import random
import datetime
from base.common import *
from base.task import Task
from airtest.core.api import auto_setup, home, start_app, stop_app, touch, Template
from airtest.report.report import simple_report

class Game:
    """
        Attributes:
            [Common]
                name - Game name.
                country - Country of the game.
                package_name - Android application package name.
                activity_name - Android application activity name.
                resolution - Resolution at coordinate recording.
                tasks - Task set, containing three phases: start, random and finish.
            [Statistics]
                pass_count - Total successful count.
                fail_count - Total failed count.
                pass_rate - Success rate = pass_count / (pass_count + fail_count).
                avg_time - Average time.

    """

    def __init__(self, name:str, country:str):
        self.name = name
        self.country = country
        self.package_name = ""
        self.activity_name = ""
        self.resolution = (1920, 1080)
        self.tasks = {
            "start_task": [],
            "random_task": [],
            "finish_task": []
        }

        self.pass_count = 0
        self.fail_count = 0
        self.pass_rate = 0
        self.avg_time = 0

        # Recode profile status.
        self.config_ext = False
        self.config_attrib = ["name",
                              "country",
                              "resolution",
                              "package_name",
                              "activity_name"]
        self.log_attrib = ["pass_count",
                           "fail_count",
                           "pass_rate",
                           "avg_time"]
        self.game_path = os.path.join(os.getcwd(), "games",
                                      "{0}_{1}".format(self.name, self.country))

        # Load config & log.
        self.__load_config()
        self.__load_log()

    def __repr__(self):
        """
            Print class property.
        """

        attrib_info = get_class_attribute(self.__dict__)
        return attrib_info

    def __del__(self):
        """
            Save information before release.
        """

        self.__save_config()
        self.__save_log()
        # self.finish()

    def __load_config(self):
        """
            Load config information.
        """

        config_path = os.path.join(self.game_path, "config",
                                   "{0}_{1}.json".format(self.name, self.country))
        if os.path.exists(config_path):
            self.config_ext = True
            config_dict = load_config(config_path)
            for sci in self.config_attrib:
                self.__dict__[sci] = config_dict[sci]

            # Converting task dictionaries to classes.
            for task_mode in config_dict["tasks"].keys():
                for task_dict in config_dict["tasks"][task_mode]:
                    task = Task(task_dict["name"], task_dict["coordinates"])
                    self.tasks[task_mode].append(task)

            print_message("Success", "[{}] Config information loaded!".format(self.name))
        else:
            print_message("Warning", "[{}] Config information lost!".format(self.name))

    def __save_config(self):
        """
            Save config information.
        """

        # Make sure config path exists.
        path_exists(os.path.join(self.game_path, "config"))
        config_path = os.path.join(self.game_path, "config",
                                   "{0}_{1}.json".format(self.name, self.country))
        with open(config_path, "wt", encoding="utf-8") as fw:
            # Record of basic parameters.
            json_dict = {}
            for sci in self.config_attrib:
                json_dict[sci] = self.__dict__[sci]
            json_dict["tasks"] = {}

            # Record of task parameters.
            for task_mode in self.tasks.keys():
                task_list = []
                for task in self.tasks[task_mode]:
                    task_dict = task.get_config_dict()
                    task_list.append(task_dict)
                json_dict["tasks"][task_mode] = task_list
            json_str = json.dumps(json_dict, indent=4)
            fw.write(json_str)

        print_message("Success", "[{}] Config information saved!".format(self.name))

    def __load_log(self):
        """
            Load log.
        """

        log_path = os.path.join(self.game_path, "log",
                                "{0}_{1}.json".format(self.name, self.country))
        if os.path.exists(log_path) and self.config_ext:
            log_dict = load_config(log_path)
            for sti in self.log_attrib:
                self.__dict__[sti] = log_dict[sti]

            for task_mode in self.tasks.keys():
                for task in self.tasks[task_mode]:
                    for si in self.log_attrib:
                        task.__dict__[si] = log_dict["tasks"][task.name][si]

            print_message("Success", "[{}] Log loaded!".format(self.name))
        else:
            print_message("Warning", "[{}] Log lost!".format(self.name))

    def __save_log(self):
        """
            Save log.
        """

        # Make sure log path exists.
        path_exists(os.path.join(self.game_path, "log"))
        log_path = os.path.join(self.game_path, "log",
                                "{0}_{1}.json".format(self.name, self.country))
        with open(log_path, "wt", encoding="utf-8") as fw:
            json_dict = {}
            for sci in self.log_attrib:
                json_dict[sci] = self.__dict__[sci]
            json_dict["tasks"] = {}

            for task_mode in self.tasks.keys():
                for task in self.tasks[task_mode]:
                    task_dict = task.get_log_dict()
                    json_dict["tasks"][task.name] = task_dict
            json_str = json.dumps(json_dict, indent=4)
            fw.write(json_str)

        print_message("Success", "[{}] Log saved!".format(self.name))

    def __update_result(self, game_result:str):
        """
            Update the results of the game.
        """
        result_dict = {}
        result_path = os.path.join(os.getcwd(), "last_result.json")
        # Load results.
        if os.path.exists(result_path):
            with open(result_path, "r") as fr:
                result_dict = json.load(fr)
        # Add current result.
        result_dict[self.name] = game_result
        with open(result_path, "w", encoding="utf-8") as fw:
            json_str = json.dumps(result_dict, indent=4)
            fw.write(json_str)

    @task_log
    def start(self):
        """
            Start the application by package name.
        """

        try:
            start_app(self.package_name)
        except:
            home()
            time.sleep(5)
            touch(self.get_image("{0}_{1}.png".format(self.name, self.country)))
        time.sleep(30)

    @task_log
    def finish(self):
        """
            Stop the application by package name.
        """

        # stop_app(self.package_name)
        time.sleep(5)

    @task_log
    def task_init(self):
        """
            Initial game information, game tasks, coordinates etc.
        """

        pass

    def get_task(self, task_name:str):
        """
            Get task class by task name.
        """

        for task_mode in self.tasks:
            for task in self.tasks[task_mode]:
                if task.name == task_name:
                    return task
        raise IndexError("Please check task mode and name.")

    def get_image(self, image_name:str):
        """
            Get image by image name.
        """
        image_path = os.path.join(self.game_path, "image", image_name)
        return Template(filename=image_path, resolution=self.resolution)

    def task_process(self, switch_tasks:dict):
        """
            Task process.
        """
        if not self.config_ext:
            # Configuration file does not exist, initialize.
            self.task_init()

        total_count = self.pass_count + self.fail_count
        start_time = datetime.datetime.now()
        start_time_str = start_time.strftime("%Y_%m_%d_%H_%M_%S")
        # Create log directory, and initialize airtest.
        log_dir = os.path.join(self.game_path, "log", start_time_str)
        os.makedirs(log_dir)
        auto_setup(basedir=os.path.join(self.game_path, "{}_{}.py".format(self.name, self.country)),
                   logdir=log_dir)

        # Run according to the configuration file.
        try:
            # Start game.
            self.start()

            # Execute task according to task name.
            for task_mode in self.tasks.keys():
                task_list = self.tasks[task_mode]
                if task_mode == "random_task":
                    # Randomize list order.
                    # random.shuffle(task_list)
                    pass
                for task in task_list:
                    try:
                        task_start_time = datetime.datetime.now()
                        switch_tasks.get(task.name)()
                        task.pass_count = task.pass_count + 1
                        task_end_time = datetime.datetime.now()
                        task_duration_time = (task_end_time - task_start_time).seconds
                        task_total_count = task.pass_count + task.fail_count
                        task.avg_time = round(((task_total_count * task.avg_time) + task_duration_time) / (task_total_count + 1), 2)
                        print_message("Log", "↑ Time taken {} seconds.".format(str(task_duration_time)))
                    except Exception as e:
                        print_message("Error", "Some errors have occurred in the task ({}).".format(task.name))
                        print_message("Error", str(e))
                        print_message("Error", repr(e))
                        task.fail_count = task.fail_count + 1
                    finally:
                        task.pass_rate = round(task.pass_count / (task.pass_count + task.fail_count), 4) * 100

            self.pass_count = self.pass_count + 1
            end_time = datetime.datetime.now()
            duration_time = (end_time - start_time).seconds
            self.avg_time = round(((total_count * self.avg_time) + duration_time) / (total_count + 1), 2)
            self.finish()
            self.__update_result("Success")
        except Exception as e:
            print_message("Error", "Some errors have occurred in the game {}.".format(self.name))
            print_message("Error", str(e))
            print_message("Error", repr(e))
            self.fail_count = self.fail_count + 1
            self.__update_result("Fail")
        finally:
            self.pass_rate = round(self.pass_count / (self.pass_count + self.fail_count), 4) * 100
            # Generate log reports.
            simple_report(filepath=os.path.join(self.game_path, "{0}_{1}.py".format(self.name, self.country)),
                          logpath=log_dir,
                          logfile=os.path.join(log_dir, "log.txt"),
                          output=os.path.join(log_dir,
                                              "{0}_{1}_{2}.html".format(self.name, self.country, start_time_str)))