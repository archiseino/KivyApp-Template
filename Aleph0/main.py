from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import StringProperty, NumericProperty, ListProperty, BooleanProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from datetime import datetime
import random

# Import our custom buttons
from widgets.rounded_buttons import RoundedButton, DarkRoundedButton, CircleButton

class DataRow(RecycleDataViewBehavior, BoxLayout):
    datetime = StringProperty("")
    heart_rate = StringProperty("")
    blood_pressure = StringProperty("")
    skin_conductance = StringProperty("")
    stress_level = StringProperty("")
    index = NumericProperty(0)
    is_even = BooleanProperty(False)
    
    def refresh_view_attrs(self, rv, index, data):
        """Called when view is created or when data changes"""
        # Set all properties from the data dictionary
        self.index = index
        self.is_even = index % 2 == 0
        
        # Explicitly set properties from data dictionary
        self.datetime = data.get('datetime', '')
        self.heart_rate = data.get('heart_rate', '')
        self.blood_pressure = data.get('blood_pressure', '')
        self.skin_conductance = data.get('skin_conductance', '')
        self.stress_level = data.get('stress_level', '')
        
        return super(DataRow, self).refresh_view_attrs(rv, index, data)
    
class DataView(RecycleView):
    data = ListProperty([])  # This now properly triggers updates
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_initial_data()
    
    def add_initial_data(self):
        """Add 3 initial sample rows"""
        for i in range(3):
            self.add_data_point()
    
    def add_data_point(self):
        """Add a single data point with current timestamp"""
        new_data = {
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'heart_rate': f"{random.randint(70, 100)} bpm",
            'blood_pressure': f"{random.randint(110, 140)}/{random.randint(70, 90)} mmHg",
            'skin_conductance': f"{random.uniform(1.0, 5.0):.1f} μS",
            'stress_level': random.choice(["Low", "Medium", "High"]),
            'index': len(self.data)
        }
        
        # Create new list to trigger property change
        self.data = self.data + [new_data]

        self.refresh_from_data()

class StressMonitorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(StressMonitorLayout, self).__init__(**kwargs)
        self.total_entries = 150  # Simulate having 150 total entries
    
    def add_dummy_data(self):
        """Callback for the Add Data button"""
        self.ids.data_view.add_data_point()
        # Update counter with formatted text matching the design
        self.ids.counter_label.text = f"Showing {len(self.ids.data_view.data)} of {self.total_entries} entries"

class StressMonitorApp(App):
    def build(self):
        return StressMonitorLayout()

if __name__ == '__main__':
    StressMonitorApp().run()