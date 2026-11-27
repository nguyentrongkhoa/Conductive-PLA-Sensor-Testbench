@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 24260)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 32784)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 27268)
if /i "%LOCALHOST%"=="LAPTOP-4PM7MF9K" (taskkill /f /pid 11460)

del /F cleanup-ansys-LAPTOP-4PM7MF9K-11460.bat
