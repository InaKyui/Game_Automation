### 〓 Getting started 〓
1. Please install python3 and run "prepare.bat" before running it for the first time.
    - Download URL: https://www.python.org/downloads/release/python-31011/
    - Version 3.10.11 is recommended, otherwise the installation of the library may generate exceptions.
2. Modify the configuration file ".\Game_Automation\config\main.json".
    - [emulator_path] the file path of the Android emulator.
    - [game_list] the list of games that need to be executed.
3. Run "start.bat" to start.
    - If the tool requires administrator privileges to launch the emulator, please manually click "Yes" to launch the emulator.

### 〓 Command-line parameter 〓
- h/help
    - View command line prompts.
- debug/debug
    - Turn on debug mode. Do not start the simulator.
- g/game
    - Games name, more than one can be specified.
    - Exmaple: -g fate_grand_order_cn princess_connect_re_dive_cn
- s/speed
    - Waiting speed, the default speed is 1x. The bigger the number, the slower the speed and the higher the stability.
    - Example: -s 3
- t/task
    - Tasks for different games, more than one can be specified. Please refer to 〓 Tasks 〓.
    - Example: -t daily_quest complete
- st/special_task
    - Special tasks for different games, more than one can be specified. Please refer to 〓 Special tasks 〓.
    - Example: -st recruit

### 〓 Tasks 〓
- *Game_Name*
    - [ ] *task name*, *task explanation*
- All_Game
    - [x] start
    - [x] login, receive login bonus and enter the main interface
    - [x] finish, save log
- Arknights_Cn
    - [x] source_center
    - [x] infrastructure, harvest and redeploy
    - [x] event_quest, challenge the last quest
    - [x] daily_quest, challenge the coin/exp quest
    - [x] recruit_center, harvest and redeploy
    - [x] complete, receive daily task rewards
- Fate_Grand_Order_Cn
    - [x] daily_quest, coin quest
- Honkai_Impact_3_Cn
    - [x] energy, get daily energy
    - [x] home, home quest and story sweep
    - [x] fleet, application and submission of resource
    - [x] quest, daily resource quest
    - [ ] shopping, purchase fragment by coin
    - [x] complete, receive daily task rewards
- Princess_Connect_Re:Dive_Cn
    - [x] explore
    - [x] shopping, purchase experience
    - [x] guild, give "like"
    - [x] home, get energy
    - [x] gashapon
    - [x] dungeons, the hardest/penultimate level
    - [x] arena, harvest and attack the first person
    - [x] princess_arena, harvest and attack the first person
    - [x] quest, challenge very hard boss and clear hard quests
    - [x] complete, receive daily task rewards

### 〓 Special tasks 〓
- Arknights_Cn
    - [x] recruit, recurring recruitment with tickets.

### 〓 Tips 〓
- All_Game
    - In [login], some of the special login interface has been adapted, if tool still throws an error., please follow the steps below to retry:
        1. Manually login to the main interface.
        2. Close the game.
        3. Re-run the tool.

- Princess_Connect_Re:Dive_Cn
    - In [dungeons], you can modify "level_button" to achieve the penultimate level.
    - In [quest], automatically detects the presence of event quest.
    - In [quest], the default character is illya(christmas), and you can modify the material for your own character.

- Arknights_Cn
    - <*Critical*> When launching for the first time, make sure that the arknigths setting options.
        - [Off] reminder - deployment tips
        - [Off] reminder - infrastructure exit tips
        - [Off] reminder - manufacture harvest tips
        - [On] reminder - manufacture automatic replenishment
    - In [infrastructure], only ensure staff rotation and do not compute the optimal solution.
    - In [daily_quest], execute only after event quest failure, and prioritize coin quest.
    - In [recruit_center], calculate the optimal solution based on PRTS operator information.

- Honkai_Impact_3_Cn
    - <*Critical*> When launching for the first time, make sure that the quests resources have been downloaded.
    - In [fleet], please ensure that you have joined the fleet.
    - In [fleet], please ensure that sufficient resources exist for submission.

- Fate_Grand_Order_Cn
    - In [daily_quest], please ensure that you have a friend that caster is equipped with the craft essences monalisa lily.

### 〓 Expected updates 〓
1. Princess_Connect_Re:Dive_Cn(2023.10)
    - New area sweeping function;
    - Equipment shop purchase function;
2. Honkai_Impact_3_Cn(2023.10)
    - Coin shop purchase function.
3. <*New*> User_Interface(2023.10)
    - Interface operation options.

### 〓 Latest version 2.7 〓
1. [arknights] Fix the bug that small probability of failure for releasing operators in the infrastructure.
2. [arknights] Fix the bug that touching too fast on the quest settle interface.
3. [fate_grand_order] Fix the bug that touching too fast on the quest teaming interface.
4. [honkai_impact_3] Fix the bug that touching too fast on the home quest interface.
5. [honkai_impact_3] Fix the bug that touching too fast on the fleet submission interface.
6. [princess_connect_re_dive] Fix the bug that there is wrong logic in entering guild interface.
7. Optimized README.md and add a new history update file.