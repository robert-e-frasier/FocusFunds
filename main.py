from kivy.app import App
from gui.screen_manager import AppScreenManager
from kivy.core.window import Window

Window.clearcolor = (14/255, 47/255, 10/255, 1) 

class FinanceApp(App):
    def build(self):
        return AppScreenManager()
    
if __name__ == "__main__":
    FinanceApp().run()