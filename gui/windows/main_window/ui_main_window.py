from ctypes import alignment
from gui.widgets.my_widgets import MyWidgets
from qt_core import *

# IMPORT PAGES
from gui.pages.ui_page1 import UI_ApplicationPage1
from gui.pages.ui_page2 import UI_ApplicationPage2
from gui.pages.ui_page3 import UI_ApplicationPage3

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

# MAIN WINDOW
class UI_MainWindow(object):

    def setup_ui(self, parent):
        
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INCINALS PARAMETERS
        parent.resize(1280, 720)
        parent.setMinimumSize(720, 480)

        # CREATE MAIN FRAME
        self.main_frame = QFrame()

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36")

        self.extern_layout = QVBoxLayout(self.central_frame)
        self.extern_layout.setContentsMargins(0,0,0,0)
        self.extern_layout.setSpacing(0)

        # LEFT MENU
        #////////////////////////////////////////////////////////////////////
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMinimumWidth(50)
        self.left_menu.setMaximumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        # self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        # self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red; }")
        
        # TOP FRAME MENU LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        # PUSH BTNS
        self.toggle_btn = PyPushButton(
            text = "Menu",
            icon_path = "icon_menu.svg"
        )
        self.btn_1 = PyPushButton(
            text = "Keys",
            is_active = True,
            icon_path = "cil-key.png",
        )
        self.btn_2 = PyPushButton(
            text = "Encrypt",
            icon_path = "cil-lock.png"
        )
        self.btn_3 = PyPushButton(
            text = "Decrypt",
            icon_path = "cil-unlock.png"
        )
        self.btn_4 = PyPushButton(
            text = "Open File",
            icon_path = "cil-folder.png"
        )
        self.btn_5 = PyPushButton(
            text = "Save As",
            icon_path = "cil-save.png"
        )

        # ADD PUSH BTNS TO LAOUT
        self.left_menu_top_layout.addWidget(self.toggle_btn)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        self.left_menu_top_layout.addWidget(self.btn_3)
        self.left_menu_top_layout.addWidget(self.btn_4)
        self.left_menu_top_layout.addWidget(self.btn_5)

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        # self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        # self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red }")
        
        # BOTTOM FRAME MENU LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        # PUSH SETTINGS BTN
        self.settings_btn = PyPushButton(
            text = "Settings",
            icon_path = "icon_settings.svg"
        )

        # ADD PUSH BTN CONFIG TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0")
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf") 
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(15)
        self.left_menu_label_version.setMaximumHeight(15)

        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(25)
        self.top_bar.setMinimumHeight(25)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(5,0,5,0)

        # left label
        self.top_left_label = QLabel("Generate keys manually or automatically.")

        # spacer
        self.spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # right label
        self.top_right_label = QLabel("Keys")
        self.top_right_label.setStyleSheet("font: 700 9pt 'Segoe UI'")

        # add labels to top bar layout
        self.top_bar_layout.addWidget(self.top_left_label)
        self.top_bar_layout.addSpacerItem(self.spacer)
        self.top_bar_layout.addWidget(self.top_right_label)

        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.pages.setWindowTitle("application_pages")
        self.pages.resize(622, 515)
        self.ui_page1 = UI_ApplicationPage1()
        self.ui_page1.setupUi(self.pages)
        self.ui_page2 = UI_ApplicationPage2()
        self.ui_page2.setupUi(self.pages)
        self.ui_page3 = UI_ApplicationPage3()
        self.ui_page3.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_page1.page)

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(15)
        self.bottom_bar.setMinimumHeight(15)
        # self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar.setStyleSheet("background-color: #343644; color: #6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(5,0,5,0)

        # left label
        self.bottom_left_label = QLabel("MBN Enterprises")

        # spacer
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # right label
        self.bottom_right_label = QLabel("© 2022")

        # add labels to top bar layout
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addSpacerItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_right_label)

        # ADD WIDGETS TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)

        # ADD WIDGETS TO MAIN LAYOUT
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # ADD WIDGETS TO CENTRAL FRAME
        self.extern_layout.addWidget(self.main_frame)
        self.extern_layout.addWidget(self.bottom_bar)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
        

