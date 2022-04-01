from ctypes import alignment
from qt_core import *



class UI_ApplicationPage3(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")

        # PAGE 3 CONTENT
        self.page = QWidget()
        self.main_layout = QHBoxLayout(self.page)

        self.central_frame = QFrame()
        self.central_frame.setMaximumHeight(250)
        self.central_frame.setMaximumWidth(500)
        
        self.central_layout = QHBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.central_layout.setSpacing(10)

        # self.decrypt_box_1 = MyWidgets()
        # self.decrypt_box_1.textBox(self.page, "Write something to decrypt:", "Done", QSize(500, 250))
        # self.decrypt_box_2 = MyWidgets()
        # self.decrypt_box_2.textBox(self.page, "Decrypted message:", "Save", QSize(0, 250),  "#44475a")

        # self.central_layout.addWidget(self.decrypt_box_1.text_box_frame, 0, Qt.AlignCenter)
        # self.central_layout.addWidget(self.decrypt_box_2.text_box_frame, 0, Qt.AlignLeft)
        
        self.main_layout.addWidget(self.central_frame)

        application_pages.addWidget(self.page)

        #self.decrypt_box_1.done_btn.clicked.connect(self.done_handle)

    def done_handle(self):
        pass