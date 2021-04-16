import os
from pywinauto.application import Application
os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})

# Cài phần mềm Xampp
xampp_install = r"Stack Software WebGIS\xampp-windows-x64-7.4.12-0-VC15-installer.exe"
xampp = Application(backend="uia").start(xampp_install)

# Khi cài phần mềm mới không sử dụng đoạn này
# xampp.Question['Yes Enter'].click()

xampp.Warning['OK Enter'].click()
xampp.Setup['Next >'].click()
xampp.Setup['Next >'].click()

# (Khi cài phần mềm mới không sử dụng đoạn này)
# xampp.Setup['Select a folderButton'].click()
# xampp.Setup['DATA (D:)'].double_click_input(button='left')
# xampp.Setup['Xampp'].double_click_input(button='left')
# xampp.Setup['Select FolderButton'].click()

xampp.Setup['Next >'].click()
xampp.Setup['Next >'].click()
xampp.Setup['Next >'].click()
xampp.Setup['Next >'].click()
# Finish Xampp
xampp.Setup['Finish'].click()

