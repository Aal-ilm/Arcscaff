@echo off
REM Navigate to the batch file directory
cd /d %~dp0

REM Run main.py as a module (to fix import errors)
python -m src.main

REM Pause so you can see output
pause
