from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import StringProperty
from kivy.app import App

"""
🚪 Root Container for Future build.

This is the main container for the App. 

Kivy can be scaled as Desktop app, so one potential update is making a Navigation for other feature. 
But I'll leave as a Trivia for you

"""
class StressMonitorLayout(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

class NavTab(ToggleButtonBehavior, BoxLayout):
    """ A tab for the navigation bar. """
    text = StringProperty("")
    icon = StringProperty("")
    icon_active = StringProperty("")
    screen_name = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def switch_screen(self, *args):
        """ Switch to the screen associated with this tab. """
        app = App.get_running_app()
        if app:
            app.root.ids.screen_manager.current = self.screen_name