import sys
import os
import time
import threading

from qt_core import *
from app.char_codec import CharCodec
from gui.widgets.my_widgets import ExpandAnimation, HiddenMenu

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSA Cryptography")
        self.setWindowIcon(QIcon("gui/images/icons/RSA.ico"))
        self.setAcceptDrops(True)
        
        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()  
        self.ui.setup_ui(self)

        # LEFT HIDDEN MENU
        self.mw = HiddenMenu(self.ui.main_frame)
        self.mw.set_opacity_animation()

        # LEFT MENU ANIMATION
        self.left_menu_animation = ExpandAnimation(
            self.ui.left_menu,
            start_width = 50,
            end_width = 240,
            duration = 150
        )        
        
        # CLICK EVENTS
        # Toggle button 
        self.ui.toggle_btn.clicked.connect(self.left_menu_animation.reset)
        
        # Show pages
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.show_page_2)
        self.ui.btn_3.clicked.connect(self.show_page_3)
        # Open file
        self.ui.btn_4.clicked.connect(self.open_file)
        # Save file
        self.ui.btn_5.clicked.connect(self.save_file)
        # Show/hide settings
        self.ui.settings_btn.clicked.connect(self.mw.start)
        self.mw.hidden_btn.clicked.connect(self.mw.start)
        
        # EXIBE A APLICAÇÂO
        self.show()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_page1.page)
        self.ui.top_left_label.setText("Generate keys manually or automatically.")
        self.ui.warning_label.setText("")
        self.ui.top_right_label.setText("Keys")
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_page2.page)
        self.ui.top_left_label.setText("Write a message to encrypt or drop a file.")
        self.ui.warning_label.setText("")
        self.ui.top_right_label.setText("Encrypt")
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_page3.page)
        self.ui.top_left_label.setText("Write a massage to decrypt or drop a file.")
        self.ui.warning_label.setText("")
        self.ui.top_right_label.setText("Decrypt")
        self.ui.btn_3.set_active(True)
        
    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        event.setDropAction(Qt.CopyAction)
        try:      
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.read_file(file_path)
            self.insertTextToProperlyPage(file_path)

        except FileNotFoundError:
            print("File or directory not found")
        event.accept()

    def open_file(self):
        default_path = os.path.expanduser("~")

        try:
            file_path = QFileDialog.getOpenFileName(self, "Open File", dir=default_path + "/desktop")[0]
            print(file_path)
            self.read_file(file_path)
            self.insertTextToProperlyPage(file_path)

        except FileNotFoundError:
            print("File or directory not found")

    def insertTextToProperlyPage(self, file_path):
        if ".rsa" in file_path:
            self.show_page_3()
            self.ui.ui_page3.decrypt_box_1.text_box.insertPlainText(self.printable_content)
        else:
            self.show_page_2()
            self.ui.ui_page2.encrypt_box_1.text_box.insertPlainText(self.printable_content)

    def read_file(self, file_path):
        file = open(file_path, 'rb')

        file_content = CharCodec()
        self.file_content = file_content.bytesToStr(file)
        print(self.file_content)

        file.seek(0)

        printable_content = CharCodec()
        self.printable_content = printable_content.bytesToStr(file, remove_char=0)

        file.close()

    def save_file(self):
        try:
            self.text
        except AttributeError:
            print("Not a file to save!")
            return

        default_path = os.path.expanduser("~")
        save_path = QFileDialog.getSaveFileName(self, "Save As", dir=default_path + "/untitled.txt")[0]      

        try:
            file = open(save_path, "w")
            file.write(self.text)
            file.close()
        except FileNotFoundError:
            print("File or directory not found")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
