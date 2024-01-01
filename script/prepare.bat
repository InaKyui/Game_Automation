@REM Ensure that the virtual environment does not exist.
DEL /s /q venv
RD /s /q venv
@REM Creat a virtual environment and install libraries.
python -m venv venv
.\venv\Scripts\pip install airtest -i https://pypi.tuna.tsinghua.edu.cn/simple
.\venv\Scripts\pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
.\venv\Scripts\pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
.\venv\Scripts\pip install Pillow==9.5.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
ECHO [Success] Environment configuration completed.