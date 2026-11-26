@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 36804)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 26820)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 40276)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 7880)

del /F cleanup-ansys-LAPTOP-4PM7MF9K-7880.bat
