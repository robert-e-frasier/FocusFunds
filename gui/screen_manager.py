from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from gui.views.main_menu import MainMenu

Builder.load_file("focusfunds/gui/kv/main_menu.kv")

class AppScreenManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        # Load Navigation Panel
        self.nav_panel = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    size_hint_x: 0.22
    padding: 10
    spacing: 10
    canvas.before:
        Color:
            rgba: 21/255, 75/255, 14/255, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')
        
        from kivy.uix.button import Button
        from kivy.utils import get_color_from_hex

        self.screens = {
            "Dashboard": "dashboard",
            "Accounts": "accounts",
            "Transactions": "transactions",
            "Get Help": "help",
            "Settings": "settings"
        }

        self.screen_manager = ScreenManager()

        for label, screen_id in self.screens.items():
            btn = Button(
                text=label,
                size_hint_y=None,
                height=45,
                background_normal='',
                background_color=(0, 0, 0, 0),
                color=get_color_from_hex("#FFFFFF")
            )
            btn.bind(on_release=lambda btn, scr=screen_id: self.switch_to(scr))
            self.nav_panel.add_widget(btn)
            self.screen_manager.add_widget(MainMenu(name=screen_id))

        self.add_widget(self.nav_panel)
        self.add_widget(self.screen_manager)

    def switch_to(self, screen_name):
        self.screen_manager.current = screen_name