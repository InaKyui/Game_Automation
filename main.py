#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.10
"""
[File]        : main.py
[Time]        : 2023/10/01 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.6
[Description] : Code entrance.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.6"

import os
import time
import logging
import argparse
import subprocess
from base.common import *
from airtest.core.api import *

def main(args:argparse.Namespace):
    # Load config.
    config_path = os.path.join(os.getcwd(), "config", "main.json")
    config_dict = load_config(config_path)
    emulator_path = config_dict["emulator_path"]

    # If in debug mode, skip starting the emulator.
    if not args.debug:
        # Delete the last result.
        if os.path.exists(os.path.join(os.getcwd(), "last_result.json")):
            os.remove(os.path.join(os.getcwd(), "last_result.json"))

        # Start emulator.
        subprocess.Popen(emulator_path,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
        time.sleep(30)
    # Connect airtest module.
    logger = logging.getLogger("airtest")
    logger.setLevel(logging.ERROR)
    retry_cnt = 3
    for i in range(retry_cnt + 1):
        try:
            try:
                # Link mumu emulator.
                connect_device("Android://127.0.0.1:5037/127.0.0.1:7555")
                time.sleep(5)
                # Turn off advertising.
                touch(Template(filename=os.path.join(os.getcwd(), "image", "button_close.png"),
                               resolution=(1280,720)))
                time.sleep(1)
            except:
                # Link normal emulators.
                connect_device("Android:///")
            # Connected successfully.
            print_message("Success", "Android device connected.")
            break
        except:
            # Connection failed, retry three times.
            if i < retry_cnt:
                print_message("Fail", "Android devices lost, {} time retry.".format(str(i + 1)))
                time.sleep(30)
                continue
            else:
                print_message("Error", "Android devices lost.")
                raise IndexError("Android devices lost.")
    # Load game list.
    game_list = []
    if not args.game:
        args.game = []
    # Prefer <args.game>, otherwise use <config_dict>.
    if not args.game and "princess_connect_re_dive_cn" in config_dict["game_list"] or "princess_connect_re_dive_cn" in args.game:
        from games.princess_connect_re_dive_cn import princess_connect_re_dive_cn
        pcr_cn = princess_connect_re_dive_cn.PrincessConnectReDive()
        game_list.append(pcr_cn)
    if not args.game and "arknights_cn" in config_dict["game_list"] or "arknights_cn" in args.game:
        from games.arknights_cn import arknights_cn
        akn_cn = arknights_cn.Arknights()
        game_list.append(akn_cn)
    if not args.game and "honkai_impact_3_cn" in config_dict["game_list"] or "honkai_impact_3_cn" in args.game:
        from games.honkai_impact_3_cn import honkai_impact_3_cn
        hki_cn = honkai_impact_3_cn.HonkaiImpact3()
        game_list.append(hki_cn)
    if not args.game and "fate_grand_order_cn" in config_dict["game_list"] or "fate_grand_order_cn" in args.game:
        from games.fate_grand_order_cn import fate_grand_order_cn
        fgo_cn = fate_grand_order_cn.FateGrandOrder()
        game_list.append(fgo_cn)
    # Execute scripts.
    for game in game_list:
        game.speed = args.speed
        game.run_task(task=args.task, special_task=args.special_task)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-debug", "--debug", action="store_true", help="Turn on debug mode.")
    parser.add_argument("-g", "--game", type=str, nargs="+", help="Game name. e.g. arknights_cn, honkai_impact_3_cn, fate_grand_order_cn, princess_connect_re_dive_cn")
    parser.add_argument("-s", "--speed", type=int, default=1, help="Waiting speed, the default speed is 1x. The bigger the number, the slower the speed and the higher the stability.")
    parser.add_argument("-t", "--task", type=str, nargs="+", help="Tasks for different games. Please refer to the \"README.md\" for details.")
    parser.add_argument("-st", "--special_task", type=str, nargs="+", help="Special tasks for different games. Please refer to the \"README.md\" for details.")
    args = parser.parse_args()
    main(args)