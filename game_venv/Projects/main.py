#-*- encoding: utf-8 -*-
#!/usr/bin/game_venv python3.7
"""
[File]        : main.py
[Time]        : 2023/05/01 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 2.0
[Description] : Code entrance.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 2.0"

import os
import time
import subprocess
from base.common import *
from airtest.core.api import *

def main():
    # Load config.
    config_path = os.path.join(os.getcwd(), "config", "main.json")
    config_dict = load_config(config_path)
    emulator_path = config_dict["emulator_path"]

    # Start emulator.
    obj = subprocess.Popen(emulator_path,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
    time.sleep(30)

    # Connect airtest module.
    import logging
    logger = logging.getLogger("airtest")
    logger.setLevel(logging.ERROR)
    retry_cnt = 3
    for i in range(retry_cnt + 1):
        try:
            dev = connect_device("Android:///")
            # Connected successfully.
            print_message("Success", "Android device connected.")
            break
        except Exception as e:
            # Connection failed, retry three times.
            if i < retry_cnt:
                print_message("Fail", "Android devices lost, {} time retry.".format(str(i + 1)))
                time.sleep(30)
                continue
            else:
                print_message("Error", "Android devices lost.")
                raise IndexError("Android devices lost.")

    # Execute scripts.
    if "princess_connect_re_dive_cn" in config_dict["game_list"]:
        from games.princess_connect_re_dive_cn import princess_connect_re_dive_cn

        pcr_cn = princess_connect_re_dive_cn.PrincessConnectReDive()
        pcr_cn.run_task()
    if "arknights_cn" in config_dict["game_list"]:
        from games.arknights_cn import arknights_cn

        akn_cn = arknights_cn.Arknights()
        akn_cn.run_task()
    if "honkai_impact_3_cn" in config_dict["game_list"]:
        from games.honkai_impact_3_cn import honkai_impact_3_cn

        hki_cn = honkai_impact_3_cn.HonkaiImpact3()
        hki_cn.run_task()
    if "fate_grand_order_cn" in config_dict["game_list"]:
        from games.fate_grand_order_cn import fate_grand_order_cn

        fgo_cn = fate_grand_order_cn.FateGrandOrder()
        fgo_cn.run_task()

if __name__ == "__main__":
    main()