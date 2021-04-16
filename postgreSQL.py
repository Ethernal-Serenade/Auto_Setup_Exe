import os
import time
from pywinauto.application import Application

os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})

# Cài phần mềm PostgreSQL (run file bat trước vì soft yêu cầu quyền cao nhất)
# time.sleep(30)
# pg = Application(backend="uia").connect(title = 'Setup')
# print(pg.window(best_match='').print_control_identifiers())

# import win32gui
# def winEnumHandler(hwnd, ctx):
#     if win32gui.IsWindowVisible(hwnd):
#        print(hex(hwnd), win32gui.GetWindowText(hwnd))
# win32gui.EnumWindows(winEnumHandler, None)

pg = Application(backend="uia").connect(path="")
# print(pg.window(best_match='Setup').print_control_identifiers())