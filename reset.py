#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.10
"""
[File]        : reset.py
[Time]        : 2023/09/15 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.5
[Description] : Reset operating environment.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.5"

import os
from base.common import delete_directory


def main():
    if os.path.exists(os.path.join(os.getcwd(), "last_result.json")):
        os.remove(os.path.join(os.getcwd(), "last_result.json"))
    if os.path.exists(os.path.join("\\".join(os.getcwd().split("\\")[:-1]), "Scripts", "__pycache__")):
        delete_directory(dir_path=os.path.join("\\".join(os.getcwd().split("\\")[:-1]), "Scripts", "__pycache__"),
                         dir_exist=False)
    if os.path.exists(os.path.join(os.getcwd(), "base", "__pycache__")):
        delete_directory(dir_path=os.path.join(os.getcwd(), "base", "__pycache__"),
                         dir_exist=False)

    games_path = os.path.join(os.getcwd(), "games")
    for game in os.listdir(games_path):
        if os.path.exists(os.path.join(games_path, game, "__pycache__")):
            delete_directory(dir_path=os.path.join(games_path, game, "__pycache__"),
                             dir_exist=False)
        if os.path.exists(os.path.join(games_path, game, "config")):
            delete_directory(dir_path=os.path.join(games_path, game, "config"),
                             dir_exist=False)
        if os.path.exists(os.path.join(games_path, game, "log")):
            delete_directory(dir_path=os.path.join(games_path, game, "log"),
                             dir_exist=False)


if __name__ == "__main__":
    main()