from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from pathlib import Path

kv_path = Path(__file__).parent / "main_menu.kv"
Builder.load_file(str(kv_path))

class MainMenu(Screen):
    pass