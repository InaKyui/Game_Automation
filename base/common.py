#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : common.py
[Time]        : 2023/10/01 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.6
[Description] : Common methods.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.6"

import os
import cv2
import json
import time
import numpy as np
from paddleocr import PaddleOCR
from functools import wraps

def print_message(status:str, message:str):
    """
        Print message.
        Template:
            [Time][Status] message.
    """
    print("[{0}][{1}]".format(time.strftime("%H:%M:%S", time.localtime()),
            status).ljust(20, " ") + " {}".format(message))

def image_to_string(img: np.ndarray) -> str:
    """
        Text recognition.
    """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)
    ocr = PaddleOCR(use_angle_cls=True, use_gpu=False, show_log=False, lang="ch")
    text = ocr.ocr(dst, cls=True)
    try:
        return text[0][0][1][0]
    except:
        return None

def path_exists(path:str):
    """
        Ensure the file path exists.
    """
    try:
        if not os.path.exists(path):
            print_message("Fail", "Can't find path: " + path)
            os.mkdir(path)
            print_message("Success", "Create path: " + path)
    except:
        print_message("Error", "Can't operate path: " + path)
        raise FileExistsError

def delete_directory(dir_path:str, dir_exist:bool=False):
    """
        Delete all files and directory in the target directory.
        Attributes:
            dir_path - directory path.
            dir_exist - [True] Retain the target directory.
                      - [False] Delete the target directory itself.
    """
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            delete_directory(os.path.join(root, dir))
    if not dir_exist:
        os.rmdir(dir_path)


def get_class_attribute(attribute:dict):
    """
        Convert class attributes to text.
    """
    attrib_info = ""
    key_length = max(len(key) for key in attribute) + 1
    for key in attribute:
        attrib_info += "{0}:{1}\n".format(key.capitalize().ljust(key_length, " "),
                                        str(attribute[key]))
    return attrib_info


def load_config(config_path:str):
    """
        Load the configuration file as a dictionary.
    """
    if os.path.exists(config_path):
        with open(config_path, "r") as fr:
            config_content = fr.read()
        config_dict = json.loads(config_content)
        print_message("Success", "[{}] Config information loaded!".format(config_path))
        return config_dict
    else:
        print_message("Error", "[{}] Config information lost!".format(config_path))
        raise IOError("Please check config path.")


def task_log(func):
    """
        Monitor the beginning and end of a task function.
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        print_message("Start", func.__name__.replace("__task_", ""))
        ret = func(*args,**kwargs)
        print_message("Finish", func.__name__.replace("__task_", ""))
        return ret
    return wrapper