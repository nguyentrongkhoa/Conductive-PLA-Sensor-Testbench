@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 37780)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 41900)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 29476)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 39132)

del /F cleanup-ansys-LAPTOP-4PM7MF9K-39132.bat
