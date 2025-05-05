from kivy.uix.screenmanager import ScreenManager
from gui.screens.main_menu import MainMenu

class AppScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainMenu(name="main_menu"))
    