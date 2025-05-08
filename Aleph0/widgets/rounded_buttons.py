from kivy.uix.button import Button
from kivy.properties import ListProperty, ColorProperty, NumericProperty
from kivy.lang import Builder

# Load KV file
Builder.load_file('d:/Stuff That I Need to Do/Template-Phys/Aleph0/widgets/rounded_buttons.kv')

class RoundedButton(Button):
    """A button with rounded corners."""
    color_normal = ColorProperty([0.9, 0.9, 0.9, 1])
    color_down = ColorProperty([0.8, 0.8, 0.8, 1])
    color_text = ColorProperty([0.3, 0.3, 0.3, 1])
    border_radius = NumericProperty(18)
    border_color = ColorProperty([0.8, 0.8, 0.8, 1])
    
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]  # Transparent background
        self.background_normal = ''
        self.background_down = ''
        
class DarkRoundedButton(RoundedButton):
    """A dark-themed rounded button."""
    def __init__(self, **kwargs):
        super(DarkRoundedButton, self).__init__(**kwargs)
        self.color_normal = [0.2, 0.2, 0.2, 1]
        self.color_down = [0.3, 0.3, 0.3, 1]
        self.color_text = [1, 1, 1, 1]
        self.border_color = [0.2, 0.2, 0.2, 1]

class CircleButton(Button):
    """A small circular button, typically used for actions."""
    color_normal = ColorProperty([0.95, 0.95, 0.95, 1])
    color_down = ColorProperty([0.85, 0.85, 0.85, 1])
    color_text = ColorProperty([0.5, 0.5, 0.5, 1])
    border_radius = NumericProperty(10)
    
    def __init__(self, **kwargs):
        super(CircleButton, self).__init__(**kwargs)
        self.background_color = [0, 0, 0, 0]  # Transparent background
        self.background_normal = ''
        self.background_down = ''