from ctypes import alignment
from qt_core import *
from gui.widgets.my_widgets import MyWidgets, ExpandAnimation

from app.rsa import RSA


class UI_ApplicationPage2(object):
        
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")        

         # PAGE 2 CONTENT
        self.page = QWidget()
        self.main_layout = QHBoxLayout(self.page)

        self.central_frame = QFrame()
        self.central_frame.setMaximumHeight(250)
        self.central_frame.setMaximumWidth(500)
        
        self.central_layout = QHBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.central_layout.setSpacing(10)

        self.encrypt_box_1 = MyWidgets.TextBox(self.page, "Write something to encrypt:", "Done", QSize(500, 250))
        self.encrypt_box_2 = MyWidgets.TextBox(self.page, "Encrypted message:", "Save", QSize(0, 250), "#44475a")

        self.central_layout.addWidget(self.encrypt_box_1, 0, Qt.AlignCenter)
        self.central_layout.addWidget(self.encrypt_box_2, 0, Qt.AlignLeft)

        self.main_layout.addWidget(self.central_frame)

        application_pages.addWidget(self.page)

        # CREATING FRAME ANIMATIONS EXPAND/RETRACT
        self.text_box_animation = ExpandAnimation(
            self.encrypt_box_2,
            start_width = 0, 
            end_width = 500
        )        
        self.central_frame_animation = ExpandAnimation(
            self.central_frame,
            start_width = 500, 
            end_width = 1010
        )

        # CLICK EVENTS
        # Get text from text box
        self.encrypt_box_1.done_btn.clicked.connect(self.done_handle)
        
    def done_handle(self):        
        self.get_text()
        self.encrypt()
        if self.encrypt_box_2.width() == 0:
            self.text_box_animation.reset_and_start()
            self.central_frame_animation.reset_and_start()

    def get_text(self):
        self.text = self.encrypt_box_1.text_box.toPlainText()        
        print(self.text)

    def encrypt(self):
        encrypter = RSA()
        self.encrypted_str = encrypter.encrypt(391, 3, self.text)
        self.encrypt_box_2.text_box.clear()
        self.encrypt_box_2.text_box.insertPlainText(self.encrypted_str)
