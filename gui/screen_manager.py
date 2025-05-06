from kivy.uix.screenmanager import ScreenManager, Screen
from gui.views.main_menu import MainMenu

class AppScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainMenu(name="main"))