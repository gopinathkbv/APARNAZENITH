from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
import scroll_layout

Builder.load_string("""
<SixTowerData>:
    orientation: 'vertical'
    size_hint_x: None
    width: 400
    # This is a place holder replace this with a widget that displays a tower of data
    
    canvas:
        Color:
            rgba: 0,0,0,.5
        Line:
            width: 2
            rectangle: (*self.pos, *self.size)
    Label:
        text:root.tower_name
        bold:True
        font_size:20
        markup:True
        size_hint_y: None
        height: 24
    BoxLayout:
        id: elevator_bank
        spacing: 10
        SixTowerSignals:
            id: signals
           
<ThreeTowerData>:
    orientation: 'vertical'
    size_hint_x: None
    width: 200
    
    canvas:
        Color:
            #rgb: 1, 1, 1
            rgba: 0,0,0,.5
        Line:
            width: 2
            rectangle: (*self.pos, *self.size)
    Label:
        text:root.tower_name
        bold:True
        font_size:20
        markup:True
        size_hint_y: None
        height: 24
    BoxLayout:
        id: elevator_bank
        spacing: 5
        ThreeTowerSignals:
            id: signals
            
        
            
    
<StatusMonitoring>:    
    BoxLayout: # Root Widget
        orientation: 'vertical'
        Label:
            text: 'Status Monitoring'
            size_hint_y: None
            height: 40
        BoxLayout:
            BoxLayout:
                orientation: 'vertical' # Layout to hold the labels
                size_hint_x: None
                width: 180
                Label:
                    text: 'Tower_name'  # remove the text
                    size_hint_y: None 
                    height: 24   # matches size of tower name
                Label:
                    text: 'Signals'
                    bold:True
                Label:
                    text: 'CAR POSITION'
                    bold:True
                
                Label:
                    text: 'DOOR_STATUS(OPEN/CLOSE)'
                    bold:True
                Label:
                    text: 'OVERLOAD'
                    bold:True
                Label:
                    text: 'INSPECTION/MANUAL'
                    bold:True
                Label:
                    text: 'ATTENDANT SERVICE'
                    bold:True
                Label:
                    text: 'INDEPENDENT MODE'
                    bold:True
                Label:
                    text: 'RUN/STOP'
                    bold:True
                Label:
                    text: 'FIREMAN SWITCH STATUS'
                    bold:True
                Label:
                    text: 'FIREMAN EMERGENCY OPERATION'
                    bold:True
                Label:
                    text: 'FIREMAN RETURN STATUS'
                    bold:True
                Label:
                    text: 'MALFUNCTION'
                    bold:True
                Label:
                    text: 'FLOOR'
                    bold:True

                Label:
                    text: 'CAR-DIRECTION(UP/DOWN)'
                    bold:True

                
                
                
            ScrollView:
                do_scroll_x: True
                do_scroll_y: False
                scroll_type: ['bars', 'content']
                bar_width: 20
                TowersScrollBox:
                    id: sv_box
                    size_hint_x: None
                    width: self.minimum_width

                    SixTowerData:
                        tower_name:'Tower-A'

                    SixTowerData:
                        tower_name:'Tower-B'

                    SixTowerData:
                        tower_name:'Tower-C'

                    SixTowerData:
                        tower_name:'Tower-D'

                    SixTowerData:
                        tower_name:'Tower-E'

                    SixTowerData:
                        tower_name:'Tower-F'

                    SixTowerData:
                        tower_name:'Tower-G'

                    SixTowerData:
                        tower_name:'Tower-H'

                    SixTowerData:
                        tower_name:'Tower-I'

                    SixTowerData:
                        tower_name:'Tower-J'

                    SixTowerData:
                        tower_name:'Tower-K'

                    SixTowerData:
                        tower_name:'Tower-L'

                    ThreeTowerData:
                        tower_name:'Tower-M'

                
                
                
            
""")


class SixTowerData(BoxLayout):
    #  this is a place holder for the tower data, replace this with the data for one tower
    text = StringProperty()
    tower_name = StringProperty()


class ThreeTowerData(BoxLayout):
    #  this is a place holder for the tower data, replace this with the data for one tower
    text = StringProperty()
    tower_name = StringProperty()


class TowersScrollBox(BoxLayout):
    pass


class StatusMonitoring(Screen):
    pass


if __name__ == '__main__':

    class StatusMonitoringApp(App):
        def build(self):
            return StatusMonitoring()

    StatusMonitoringApp().run()




