import sys
import os
import time
import threading
from turtle import width
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSA Cryptography")
        self.setAcceptDrops(True)

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()  
        self.ui.setup_ui(self)
        
        # Toggle button 
        self.ui.toggle_btn.clicked.connect(self.toggle_button)
        # Show pages
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.show_page_2)
        self.ui.btn_3.clicked.connect(self.show_page_3)
        # Open file
        self.ui.btn_4.clicked.connect(self.open_file)
        # Save file
        self.ui.btn_5.clicked.connect(self.save_file)
        # Show settings
        self.ui.settings_btn.clicked.connect(self.hidden_menu)

        # Get text encrypt box
        self.ui.ui_pages.text_ok_btn.clicked.connect(self.get_text)

        # LEFT HIDDEN MENU
        self.mw = MyWidgets()
        self.mw.leftHiddenMenu(self.ui.main_frame)
        self.mw.hidden_btn.clicked.connect(self.hidden_menu)
        
        # EXIBE A APLICAÇÂO
        self.show()

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        event.setDropAction(Qt.CopyAction)        
        file_path = event.mimeData().urls()[0].toLocalFile()

        self.read_file(file_path)

        if ".rsa" in file_path:
            self.show_page_3()
        else:
            self.show_page_2()
            self.ui.ui_pages.text_box.insertPlainText(self.file_content)
            

        event.accept()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.top_left_label.setText("Generate keys manually or automatically.")
        self.ui.top_right_label.setText("Keys")
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.top_left_label.setText("Write a message to encrypt or drop a file.")
        self.ui.top_right_label.setText("Encrypt")
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.top_left_label.setText("Write a massage to decrypt or drop a file.")
        self.ui.top_right_label.setText("Decrypt")
        self.ui.btn_3.set_active(True)

    def toggle_button(self):
        # Get left menu width
        menu_width = self.ui.left_menu.width()

        # Check width
        width = 50
        if menu_width == 50:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(150)
        self.animation.start()

    @Slot()
    def hidden_menu(self):
        # Get hidden menu width
        menu_width = self.mw.hidden_menu.width()
        
        self.animation = QPropertyAnimation(self.mw.hidden_menu, b"minimumWidth")   

        # Check width
        if menu_width != 240:
            self.mw.hidden_frame.show()
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(240)
            self.animation.setDuration(150)
            self.animation.start()
        
        else:
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(0)
            self.animation.setDuration(150)
            self.animation.finished.connect(self.mw.hidden_frame.hide)
            self.animation.start()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File")
        print(file_name)

    def read_file(self, file_path):
        file = open(file_path, 'r')
        self.file_content = file.read()
        file.close()

    def save_file(self):
        save_path = QFileDialog.getExistingDirectory(self, "Save As")
        print(save_path)

    def get_text(self):
        text = self.ui.ui_pages.text_box.toPlainText()
        self.ui.ui_pages.text_box.insertPlainText("muito doido")
        print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
