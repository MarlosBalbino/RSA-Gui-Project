from ctypes import alignment
from qt_core import *
from gui.widgets.my_widgets import TextBoxWindow, ExpandAnimation, FieldEmptyError, TextBox
from app.rsa import RSA



class UI_ApplicationPage3(object):
    
    def setupUi(self, application_pages, warning_label: QLabel):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")

        # WARNING LABEL (FROM UI MAIN WINDOW) 
        self.warning_label = warning_label

        # PAGE 3 CONTENT
        self.page = QWidget()
        self.main_layout = QHBoxLayout(self.page)

        self.central_frame = QFrame()
        self.central_frame.setMaximumHeight(250)
        self.central_frame.setMaximumWidth(500)
        
        self.central_layout = QHBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.central_layout.setSpacing(10)

        self.decrypt_box_1 = TextBoxWindow(
            self.page, 
            "Write a message to", 
            "decrypt:",
            tittle_color="#be2444",
            btn1_text="Done", 
            btn2_text="Clear", 
        )

        self.text_box_1 = TextBox()
        self.decrypt_box_1.add_text_box(self.text_box_1)

        self.decrypt_box_2 = TextBoxWindow(
            self.page, 
            "Decrypted message:", 
            btn1_text="Save",
            btn2_text="Save As",
            hide_btn2=False,
            window_resize=QSize(0, 250), 
            text_box_color="#44475a",
            read_only=True
        )

        self.text_box_2 = TextBox()
        self.decrypt_box_2.add_text_box(self.text_box_2)

        self.central_layout.addWidget(self.decrypt_box_1, 0, Qt.AlignCenter)
        self.central_layout.addWidget(self.decrypt_box_2, 0, Qt.AlignLeft)

        self.main_layout.addWidget(self.central_frame)

        application_pages.addWidget(self.page)

        # CREATING FRAME ANIMATIONS EXPAND/RETRACT
        self.text_box_animation = ExpandAnimation(
            self.decrypt_box_2,
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
        self.decrypt_box_1.btn_1.clicked.connect(self.done_handle)
        self.decrypt_box_1.btn_2.clicked.connect(self.clear_handle)
        self.text_box_1.textChanged.connect(self.warning_clear)

    def warning_clear(self):
        self.warning_label.setText("")
        self.get_text()
        if self.text == "":
            self.decrypt_box_1.btn_2.hide()
        else:
            self.decrypt_box_1.btn_2.show()
        
    def done_handle(self):        
        self.get_text()
        try:
            if self.text == "":
                raise FieldEmptyError("field empty")
            
            self.decrypt()

            if self.decrypt_box_2.width() == 0:                
                self.text_box_animation.reset()
                self.central_frame_animation.reset()       
            
        except FieldEmptyError:
            self.warning_label.setText("Warning: the field is empty!")
        except ValueError:
            self.warning_label.setText("Warning: insert a valid encrypted message!")

    def clear_handle(self):
        self.text_box_1.clear()
        self.text_box_2.clear()
        self.decrypt_box_1.btn_2.hide()
        if self.decrypt_box_2.width() != 0:
            self.text_box_animation.reset()
            self.central_frame_animation.reset()

    def get_text(self):
        self.text = self.text_box_1.toPlainText()        
        print("#")

    def decrypt(self):
        decrypter = RSA()
        self.decrypted_str = decrypter.decrypt(17, 23, 3, self.text)
        self.text_box_2.clear()
        self.text_box_2.insertPlainText(self.decrypted_str)
