from gui.screen_manager import AppScreenManager
from kivy.app import App
from kivy.core.window import Window

class FinanceApp(App):
    def build(self):
        Window.clearcolor = (14/255, 47/255, 10/255, 1) # #0E2F0A
        return AppScreenManager()
    
if __name__ == "__main__":
    FinanceApp().run()