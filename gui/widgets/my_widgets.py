from ctypes import alignment
from turtle import pos
from typing import Type

from qt_core import *
from gui.widgets.py_push_button import PyPushButton


class HiddenMenu(QFrame):
    # LEFT HIDDEN MENU
    #////////////////////////////////////////////////////////////////////
    def __init__(self, parent: QFrame) -> None:
        super().__init__(parent)

        # HIDDEN FRAME        
        self.setStyleSheet("background-color: transparent")
        self.setMaximumWidth(3840)
        self.setMinimumWidth(3840)
        self.setMinimumHeight(2160)
        self.hide()

        # HIDDEN FRAME LAYOUT
        self.hidden_layout = QHBoxLayout(self)
        self.hidden_layout.setContentsMargins(0,0,0,0)
        self.hidden_layout.setSpacing(0)

        # HIDDEN MENU
        self.hidden_menu = QFrame()
        self.hidden_menu.setStyleSheet("background-color: #44475a")
        self.hidden_menu.setMaximumWidth(0)
        self.hidden_menu.setMinimumWidth(0)
        self.hidden_menu.setMaximumHeight(2160)

        # OPACITY EFFECT
        self.effect = QGraphicsOpacityEffect(self.hidden_menu)
        self.effect.setOpacity(1.00)

        # SET HIDDEN MENU EFFECT
        self.hidden_menu.setGraphicsEffect(self.effect)
        self.hidden_menu.setAutoFillBackground(True)

        # HIDDEN BTN FRAME
        self.hidden_btn_frame = QFrame()
        self.hidden_btn_frame.setStyleSheet("background-color: transparent")
        self.hidden_btn_frame.setMaximumHeight(2160)

        # HIDDEN BTN
        self.hidden_btn = QPushButton(self.hidden_btn_frame)
        self.hidden_btn.setStyleSheet("background-color: transparent")
        self.hidden_btn.setFixedSize(3840, 3840)
        
        # ADD HIDDEN BTN TO HIDDEN FRAME
        self.hidden_layout.addWidget(self.hidden_menu)
        self.hidden_layout.addWidget(self.hidden_btn_frame)

    def set_opacity_animation(self):
        self.opacity_animation = OpacityEffectAnimation(
            self.effect, 
            self.hidden_menu
        )

    def start(self):
        # Get hidden menu width
        menu_width = self.hidden_menu.width()

        self.animation = QPropertyAnimation(
            self.hidden_menu,
            b"minimumWidth"
        )
        
        width = 400
        # Check width
        if menu_width != width:
            self.show()
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(width)
            self.animation.setDuration(150)
        
        else:
            self.animation.setStartValue(menu_width)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.hide)
            self.animation.setDuration(250)
        
        self.animation.start()
        try:
            self.opacity_animation.reset()
        except AttributeError:
            pass
        

class OpacityEffectAnimation(QPropertyAnimation):

    def __init__(self, effect: QGraphicsOpacityEffect, frame: QFrame):
        super().__init__(effect, b"opacity")

        self.setEasingCurve(QEasingCurve.InOutCubic)
        self.setDuration(250)

        self.effect = effect
        self.frame = frame

    def reset(self):
        # Current frame width
        frame_width = self.frame.width()

        # Check width
        if frame_width == 400:
            self.setStartValue(1.00)
            self.setEndValue(0)
            self.start()
        else:
            self.effect.setOpacity(1.00)


class TextBox(QTextEdit):

    def __init__(
        self,
        parent=None,
        text_box_color="#282a36",
        read_only=False,
        hide=False,
        scroll_mim_height=30
        ):
        
        super().__init__(parent)

        self.setStyleSheet(f"""
            QTextEdit {{ 
                color: white; font-size: 12pt; 
                border-radius: 5; background-color: {text_box_color};
            }}
        """
        )      
        self.setReadOnly(read_only)
        # CUSTOM VERTICAL SCROLL BAR
        self.vertical_scroll_bar = MyScrollBar(scroll_mim_height)
        self.setVerticalScrollBar(self.vertical_scroll_bar)
        self.setAcceptRichText(True)
        if hide is True:
            self.hide()


class MyPushButton(QPushButton):

    def __init__(
        self,
        text = "",
        color = "#8489a6", 
        border_radius = 10,
        font_size = 12,
        hover = "#c3ccdf",
        pressed = "#44475a",
        maximum_width = 72,
        maximum_heigth = 20,
        hide=False
    ):

        super().__init__()

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border-radius: {border_radius}px;
                font-size: {font_size}pt;
            }}
            QPushButton:hover {{
                background-color: {hover};
            }}
            QPushButton:pressed {{
                background-color: {pressed};
            }}    
        """
        )
        self.setText(text)
        
        self.setMaximumWidth(maximum_width)
        self.setMaximumHeight(maximum_heigth)
        if hide is True:
            self.hide()


class TextBoxWindow(QFrame):
    # TEXT BOX
    #////////////////////////////////////////////////////////////////////
    def __init__(
        self, 
        parent=None, 
        label_text="",
        label_tittle="",
        tittle_color="rgb(255, 255, 255)",
        btn1_text="",
        btn1_width=72,
        hide_btn1=False,
        btn2_text="",
        btn2_width=72,
        hide_btn2=True,
        window_resize=QSize(500, 250),
        text_box_color="#282a36",
        hide_text_box=False,
        read_only=False,
    ):
        super().__init__(parent)

        # TEXT BOX FRAME            
        self.setStyleSheet("background-color: #44475a; border-radius: 5")
        if window_resize:
            self.setMaximumSize(window_resize)
            self.setMinimumSize(window_resize)

        # TOP FRAME
        self.top_frame = QFrame()
        # self.top_frame.setStyleSheet("background-color: blue")

        # TOP FRAME LAYOUT
        self.top_frame_layout = QHBoxLayout(self.top_frame)
        self.top_frame_layout.setContentsMargins(0,0,0,0)

        # LABEL TEXT
        self.text_label = QLabel(self)
        self.text_label.setText(label_text)
        self.text_label.setStyleSheet("font: 700 12pt Segoe UI; color: rgb(255, 255, 255)")

        # LABEL TEXT
        self.label_tittle = QLabel(self)
        self.label_tittle.setText(label_tittle)
        self.label_tittle.setStyleSheet(f"font: 700 13pt Segoe UI; color: {tittle_color}")

        # SPACER
        self.spacer = QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)

        # ADD LABELS TO LAYOUT
        self.top_frame_layout.addWidget(self.text_label)
        self.top_frame_layout.addWidget(self.label_tittle)
        self.top_frame_layout.addSpacerItem(self.spacer)

        # CENTRAL FRAME
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: transparent")

        self.central_layout = QHBoxLayout(self.central_frame)
        self.central_layout.setContentsMargins(0,0,0,0)
        self.central_layout.setSpacing(9)

        # BTNS FRAME
        self.bottom_frame = QFrame()
        # self.bottom_frame.setStyleSheet("background-color: blue")

        # BTNS LAYOUT
        self.bottom_layout = QHBoxLayout(self.bottom_frame)
        self.bottom_layout.setContentsMargins(0,0,0,0)

        # DONE BUTTON
        self.btn_1 = MyPushButton(btn1_text, maximum_width=btn1_width, hide=hide_btn1)
        # CLEAR BUTTON
        self.btn_2 = MyPushButton(btn2_text, maximum_width=btn2_width, hide=hide_btn2)

        # SPACER FRAME
        self.spacer_frame = QFrame()
        
        # SPACER LAYOUT
        self.spacer_layout = QHBoxLayout(self.spacer_frame)
        self.spacer_layout.addSpacerItem(self.spacer)

        # ADD BTNS TO LAYOUT
        self.bottom_layout.addWidget(self.btn_1, 10)
        self.bottom_layout.addWidget(self.btn_2, 10)
        self.bottom_layout.addWidget(self.spacer_frame)

        # TEXT BOX LAYOUT
        self.text_box_layout = QVBoxLayout(self)
        self.text_box_layout.setContentsMargins(9,7,9,7) 
        self.text_box_layout.addWidget(self.top_frame)
        self.text_box_layout.addWidget(self.central_frame)
        self.text_box_layout.addWidget(self.bottom_frame)

    def add_text_box(self, text_box: Type[TextBox]) -> None:
        self.central_layout.addWidget(text_box)

    def add_button(self, button: Type[MyPushButton]) -> None:
        self.bottom_layout.addWidget(button)


class MyScrollBar(QScrollBar):

    def __init__(self, mim_height=30):
        super().__init__()

        self.setStyleSheet(f"""
            /*VERTICAL SCROLL BAR*/
            QScrollBar:vertical {{
                border: none;
                background-color: #282a36;
                width: 10px;
                margin: 10px 0 10px 0;
                border-radius: 0px;
            }}

            /*VERTICAL SCROLL BAR HENDLE*/
            QScrollBar::handle:vertical {{
                background-color: #8489a6;
                min-height: {mim_height}px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: #c3ccdf;
            }}
            QScrollBar::handle:vertical:pressed {{
                background-color: #44475a
            }}

            /*SCROLL BAR TOP BUTTOM*/
            QScrollBar::sub-line:vertical {{
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
            }}
            QScrollBar::sub-line:vertical:hover {{
                background-color: #c3ccdf;
            }}
            QScrollBar::sub-line:vertical:pressed {{
                background-color: #44475a;
            }}

            /*SCROLL BAR BOTTOM BUTTOM*/
            QScrollBar::add-line:vertical {{
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
            }}
            QScrollBar::add-line:vertical:hover {{
                background-color: #c3ccdf;
            }}
            QScrollBar::add-line:vertical:pressed {{
                background-color: #44475a;
            }}

            /*RESET ARROW*/
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
                background: none;
            }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;
            }}
        """)


class MySlider(QSlider):

    def __init__(
        self,
        margin = 3,
        bg_size = 10,
        bg_radius = 5,
        bg_color = "#1b1e23",
        bg_color_hover = "#1e2229",
        handle_margin = -3,
        handle_size = 16,
        handle_radius = 8,
        handle_color = "#8489a6",    
        handle_color_hover = "#c3ccdf",
        handle_color_pressed = "#44475a"
    ):
        super(MySlider, self).__init__()

        self.setStyleSheet(f"""
            QSlider {{ margin: {margin}px;}}

            /* HORIZONTAL */
            QSlider::groove:horizontal {{
                border-radius: {bg_radius}px;
                height: {bg_size}px;
                margin: 0px;
                background-color: {bg_color};
            }}
            QSlider::groove:horizontal:hover {{
                background-color: {bg_color_hover};
            }}
            QSlider::handle:horizontal {{
                border: node;
                height: 16px;
                width: 16px;
                margin: {handle_margin}px;
                border-radius: {handle_radius}px;
                background-color: {handle_color}
            }}
            QSlider::handle:horizontal:hover {{
                background-color: {handle_color_hover};
            }}
            QSlider::handle:horizontal:pressed {{
                background-color: {handle_color_pressed}
            }}

            /* VERTICAL */
            QSlider::groove:vertical {{
                border-radius: {bg_radius}px;
                height: {bg_size};
                margin: 0px;
                background-color: {bg_color};
            }}
            Qlider::groove:vertical:hover {{
                background-color: {bg_color_hover};
            }}
            Qlider::handle:vertical {{
                border: node;
                height: {handle_size}px;
                width: {handle_size}px;
                margin: {handle_margin}px;
                border-radius: {handle_radius}px;
                background-color: {handle_color};
            }}
            QSlider::handle:vertical:hover {{
                background-color: {handle_color_hover};
            }}
            QSlider::handle:vertical:pressed {{
                background-color: {handle_color_pressed}
            }}
        """
        )


class MyJumperSlider(MySlider):
    
    def __init__(self):
        super(MyJumperSlider, self).__init__()    

        self.steps = 0
        self.button_pressed = False

    def set_steps(self, steps: int):
        self.steps = steps
        self.multiples = [round(i*self.maximum()/steps) for i in range(0, steps + 1)]

    def get_steps(self):
        return self.steps

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.button_pressed = True
            
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.button_pressed:
            pos_x = round(event.pos().x() / (self.width()/self.maximum()))
            try:
                if pos_x in self.multiples:
                    self.setValue(pos_x)
            except:
                pass
      
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.button_pressed = False
    

class ExpandAnimation(QPropertyAnimation):

    def __init__(
        self, 
        parent: QFrame,
        start_width, 
        end_width, 
        duration=300
        ):

        super().__init__(parent, b"minimumWidth")

        self.frame = parent
        self.start_width = start_width
        self.end_width = end_width
        self._duration = duration

    def reset(self):
        # Current frame width
        frame_width = self.frame.width()

        # Check width
        width = self.start_width
        if frame_width == self.start_width:
            width = self.end_width

        # Set animation values
        self.setStartValue(frame_width)
        self.setEndValue(width)
        self.setDuration(self._duration)
        self.start()


class FieldEmptyError(Exception):
    pass
