from ctypes import alignment
from gui.widgets.my_widgets import TextBoxWindow, TextBox, MyPushButton
from qt_core import *



class UI_ApplicationPage1(object):
    def setupUi(self, application_pages, warning_label: QLabel):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")

        # PAGE 1 CONTENT
        self.page = QWidget()
        self.verticalLayout = QVBoxLayout(self.page)

        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: grey")

        self.central_layout = QVBoxLayout(self.central_frame)
        self.central_layout.setSpacing(72)

        self.line_edit_1 = TextBoxWindow(
            label_text="Private keys:",
            btn1_text="Generate keys",
            btn1_width=120,
            btn2_text="clear",
            window_resize=False
        )
        self.line_edit_1.setMaximumHeight(120)

        self.text_box_2 = TextBox()
        self.text_box_3 = TextBox()
        self.line_edit_1.add_text_box(self.text_box_2)
        self.line_edit_1.add_text_box(self.text_box_3)

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
        self.line_edit_2.setMaximumHeight(120)
    
        self.text_box_4 = TextBox(text_box_color="#44475a", read_only=True)
        self.line_edit_2.add_text_box(self.text_box_4)

        self.spacer = QSpacerItem(0, 0, QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)    

        self.central_layout.addSpacerItem(self.spacer)
        self.central_layout.addWidget(self.line_edit_1)
        self.central_layout.addWidget(self.line_edit_2)
        self.central_layout.addSpacerItem(self.spacer)

        self.verticalLayout.addWidget(self.central_frame)

        
        application_pages.addWidget(self.page)
