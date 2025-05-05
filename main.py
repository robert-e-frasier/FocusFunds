from kivy.app import App
from gui.screen_manager import AppScreenManager

class FinanceApp(App):
    def build(self):
        return AppScreenManager()
    
if __name__ == "__main__":
    FinanceApp().run()