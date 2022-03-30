from ctypes import alignment
from qt_core import *
from gui.widgets.my_widgets import MyWidgets


class UI_ApplicationPage1(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        

        # PAGE 1 CONTENT
        self.page = QWidget()
        self.verticalLayout = QVBoxLayout(self.page)
        application_pages.addWidget(self.page)