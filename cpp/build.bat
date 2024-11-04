@echo off
@set SOURCE=main.cpp
@set OUT_EXE=main
@set OUT_DIR=build
@set LIBS=
@set INCLUDES=/Isrc\libs\ /Isrc\libs\imgui
@set ARGS=/std:c++20

IF NOT EXIST %OUT_DIR%\ MKDIR %OUT_DIR% 

cl -Zi %ARGS% %INCLUDES% %SOURCE% /Fe%OUT_DIR%/%OUT_EXE%.exe /Fo%OUT_DIR%/ /link %LIBS%