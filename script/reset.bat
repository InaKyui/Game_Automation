@REM Initialize the code environment.
SET batPath=%~dp0
CD %batPath%
CD ..
IF EXIST last_result.json (
    DEL last_result.json
)
CD games
FOR /f %%i IN ('dir /ad /b') DO (
    CD %%i
    IF EXIST config (
        DEL /s /q config
        RD /s /q config
    )
    CD ..
)