""" from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore """

from ctypes import alignment
from qt_core import *


class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(622, 515)
        application_pages.setWindowTitle("application_pages")

        self.page_1 = QWidget()
        self.verticalLayout = QVBoxLayout(self.page_1)
        # self.label_3 = QLabel(self.page_1)
        # self.label_3.setAlignment(Qt.AlignCenter)
        # self.label_3.setText("Divices")
        # self.verticalLayout.addWidget(self.label_3)
        application_pages.addWidget(self.page_1)

        self.page_2 = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        # self.label_2 = QLabel(self.page_2)
        # self.label_2.setAlignment(Qt.AlignCenter)
        # self.label_2.setText("ASCADA")
        # self.verticalLayout_2.addWidget(self.label_2)

        self.text_box_frame = QFrame(self.page_2)
        self.text_box_frame.setStyleSheet("background-color: #44475a; border-radius: 5")
        self.text_box_frame.setMaximumSize(QSize(500, 250))
        self.text_box_frame.setMinimumSize(QSize(500, 250))

        self.text_label = QLabel(self.text_box_frame)
        self.text_label.setText("Write something:")
        self.text_label.setStyleSheet("font: 700 12pt Segoe UI; color: rgb(255, 255, 255)")

        self.scroll_bar = QScrollBar()
        self.scroll_bar.setStyleSheet("""
            /*VERTICAL SCROLL BAR*/
            QScrollBar:vertical {
                border: none;
                background-color: #282a36;
                width: 10px;
                margin: 10px 0 10px 0;
                border-radius: 0px;
            }

            /*VERTICAL SCROLL BAR HENDLE*/
            QScrollBar::handle:vertical {
                background-color: #8489a6;
                min-height: 30px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #c3ccdf;
            }
            QScrollBar::handle:vertical:pressed {
                background-color: #44475a
            }

            /*SCROLL BAR TOP BUTTOM*/
            QScrollBar::sub-line:vertical {
                border: none;
                background-color: #8489a6;
                height: 10px;
                /*
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                */
                border-radius: 5px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical:hover {
                background-color: #c3ccdf;
            }
            QScrollBar::sub-line:vertical:pressed {
                background-color: #44475a;
            }

            /*SCROLL BAR BOTTOM BUTTOM*/
            QScrollBar::add-line:vertical {
                border: none;
                background-color: #8489a6;
                height: 10px;
                /*
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
                */
                border-radius: 5px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::add-line:vertical:hover {
                background-color: #c3ccdf;
            }
            QScrollBar::add-line:vertical:pressed {
                background-color: #44475a;
            }

            /*RESET ARROW*/
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)

        self.text_box = QTextEdit(self.text_box_frame)
        self.text_box.setStyleSheet("""color: white; font-size: 12pt; border-radius: 5; background-color: #282a36""")
        self.text_box.setVerticalScrollBar(self.scroll_bar)
        self.text_box.setAcceptRichText(False)
        self.text_ok_btn = QPushButton("Done")
        self.text_ok_btn.setStyleSheet("""
            QPushButton {
                background-color: #8489a6;
                border-radius: 10px;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #c3ccdf;
            }    
            QPushButton:pressed {
                background-color: #44475a;
            }        
        """)
        self.text_ok_btn.setMaximumWidth(72)
        self.text_ok_btn.setMaximumHeight(20)

        self.text_box_layout = QVBoxLayout(self.text_box_frame)
        self.text_box_layout.addWidget(self.text_label)
        self.text_box_layout.addWidget(self.text_box)
        self.text_box_layout.addWidget(self.text_ok_btn)

        self.verticalLayout_2.addWidget(self.text_box_frame, 0, Qt.AlignCenter)
        application_pages.addWidget(self.page_2)

        self.page_3 = QWidget()
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.label = QLabel(self.page_3)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Charts")
        self.verticalLayout_3.addWidget(self.label)
        application_pages.addWidget(self.page_3)

        # QMetaObject.connectSlotsByName(application_pages)
    # setupUi
