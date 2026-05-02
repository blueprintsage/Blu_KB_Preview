@echo off
setlocal

REM === Set target directory here ===
set "TARGET_DIR=D:\Repos\Blu_KB_Preview"

echo Deleting all .json files in: %TARGET_DIR% and subfolders...
echo.

del /s /q "%TARGET_DIR%\*.json"

echo.
echo Done.
pause