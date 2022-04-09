from ctypes import alignment
from turtle import pos
from gui.widgets.my_widgets import TextBoxWindow, TextBox, MyPushButton, MyJumperSlider
from qt_core import *

from app.rsa import RSA


class UI_ApplicationPage1(object):


    def setupUi(self, application_pages, warning_label: QLabel):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        

        # PAGE 1 CONTENT
        self.page = QWidget()
        
        self.verticalLayout = QVBoxLayout(self.page)

        self.central_frame = QFrame()
        #self.central_frame.setStyleSheet("background-color: grey")

        self.central_layout = QVBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(72, 0, 72, 0)
        self.central_layout.setSpacing(72)

        self.line_edit_1 = TextBoxWindow(
            label_text="Private keys:",
            btn1_text="Generate keys",
            btn1_width=120,
            btn2_text="clear",
            window_resize=None
        )

        self.text_box_2 = TextBox(scroll_mim_height=15)
        self.text_box_3 = TextBox(scroll_mim_height=15)

        self.line_edit_1.add_text_box(self.text_box_2)
        self.line_edit_1.add_text_box(self.text_box_3)
        self.line_edit_1.setMaximumHeight(150)

        self.line_edit_2 = TextBoxWindow(
            label_text="Public keys:",
            btn1_text="Save",
            hide_btn1=True,
            btn1_width=120,
            btn2_text="Save As",
            window_resize=False,
            text_box_color="#44475a",
            read_only=True
        )
        
        self.text_box_4 = TextBox(text_box_color="#44475a", read_only=True, scroll_mim_height=15)

        self.line_edit_2.add_text_box(self.text_box_4)
        self.line_edit_2.setMaximumHeight(150)

        self.vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.horizontal_spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.slider_frame = QFrame()        
        self.slider_layout = QVBoxLayout(self.slider_frame)
        self.label_layout = QHBoxLayout()

        # SLIDER LABEL TEXT
        self.security_level_label = QLabel()
        self.security_level_label.setText("Security level:")
        self.security_level_label.setStyleSheet("font: 700 12pt Segoe UI; color: rgb(255, 255, 255)")

        self.status_label = QLabel()
        self.status_label.setText("safest")
        self.status_label.setStyleSheet("font: italic 700 12pt Segoe UI; color: green")

        self.slider = MyJumperSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setMaximumWidth(200)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(34)
        self.slider.set_steps(3)
        self.slider.valueChanged.connect(self.set_security_level)

        self.label_layout.addWidget(self.security_level_label)
        self.label_layout.addWidget(self.status_label)
        self.label_layout.addSpacerItem(self.horizontal_spacer)
        
        self.slider_layout.addLayout(self.label_layout)
        self.slider_layout.addWidget(self.slider)
        self.slider_layout.addSpacerItem(self.vertical_spacer) 

        self.central_layout.addSpacerItem(self.vertical_spacer)
        self.central_layout.addWidget(self.line_edit_1)
        self.central_layout.addWidget(self.line_edit_2)
        self.central_layout.addWidget(self.slider_frame)
        self.central_layout.addSpacerItem(self.vertical_spacer)

        self.verticalLayout.addWidget(self.central_frame)
        
        application_pages.addWidget(self.page)

        # CLICK EVENTS
        self.line_edit_1.btn_1.clicked.connect(self.generate_keys)
        self.level = 3

    def set_security_level(self):
        first_step = self.slider.maximum() / self.slider.get_steps()

        level = [3, 2, 1, 0]
        status = ["safest", "safe", "balanced", "less safe"]
        color = ["green", "yellow", "orange", "red"]

        slider_pos = round(self.slider.value() / first_step)

        self.level = level[slider_pos]
        self.status = status[slider_pos]
        self.color = color[slider_pos]

        self.status_label.setText(self.status)
        self.status_label.setStyleSheet(f"font: italic 700 12pt Segoe UI; color: {self.color}")

    def generate_keys(self):

        rsa = RSA()
        try:
            rsa.generateKeys(self.level)
        except AttributeError:
            self.set_security_level()
            self.generate_keys()

        # PRIVATE KEYS
        self.line_edit_1.text_box.setPlainText(rsa.get_key_P())
        self.text_box_2.setPlainText(rsa.get_key_Q())
        self.text_box_3.setPlainText(rsa.get_key_D())

        # PUBLIC KEYS
        self.line_edit_2.text_box.setPlainText(rsa.get_key_N())
        self.text_box_4.setPlainText(rsa.get_key_E())
        
        

    

        