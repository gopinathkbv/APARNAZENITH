"""
PROGRAM DESCRIPTION:
    The application is used to display the status of 75 Elevators available in  thirteen blocks.The 12 blocks are filled with six elevators and the final block contains
    three blocks in it.The application can be divide int three modes of view a).Plan_view b).Sectional_view c).status_monitoring 
planview:
     This section is used to display the floor number,direction of the elevator travelling and the status of the door[opening/closing] 
sectional_view:
      This section helps to display the simulation of the elevator travelling in either upwards/downwards, floor number of the elevator, Name of the elevators,load
      occupied in the elevator.
status_monitoring:
    This secton is used to display the state[Enabled/Disabled] of the 13 signal defined for each tower  
NOTE:
   Using random module we can generate the signals for the simulation purpose. In future the random signals are to be replaced by the real time signals collected from
   the thirteen blocks.
  
"""
"""
MODULES USED:

python 3.8

kivy 1.11.0

"""
"""
In main.py file the output window is divided with three screens using Screenmanager in kivy based on the selecion done by the user to display the operations narrated
in the PROGRAM DESCRIPTION.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from planview import PlanView
from sectionalview import SectionalView
from statusmonitoring import StatusMonitoring
kv = """
BoxLayout:
    orientation: 'vertical'
    BoxLayout: #This layout is used to dispaly  the project title
        size_hint_y: None
        height: 48
        Label:
            text:"APARNA-ZENITH TOWERS HYDERABAD"
            bold:True
            font_size:40
            markup:True
    BoxLayout:  #This layout defined for the selection of the mode to display the modes are defined with the togglebutton 
        size_hint_y: None
        height: 48
        ToggleButton: #The ToggleButton widget acts like a checkbox. When you touch or click it, the state toggles between ‘normal’ and ‘down’
                      #(as opposed to a Button that is only ‘down’ as long as it is pressed).
                      #Toggle buttons can be grouped to make radio buttons - only one button in a group can be in a ‘down’ state.
                      #The group name can be a string or any other hashable Python object
            text: 'Plan View'
            group: 'top'
            state: 'down'
            on_release: top_sm.current = 'plan_view'
        ToggleButton:
            text: 'Sectional View'
            group: 'top'
            on_release: top_sm.current = 'sectional_view'
        ToggleButton:
            text: 'Status_Monitoring'
            group: 'top'
            on_release: top_sm.current = 'status_monitoring'
    ScreenManager:  #This layout is defined for connecting the corresponding display of the mode using id's in kivy based on the toggle button selected by the user
        id: top_sm
        PlanView:
            name: 'plan_view'
        SectionalView:
            name: 'sectional_view'
            on_enter: if not app.schedule: app.small_simulation()
        StatusMonitoring:
            name: 'status_monitoring'
            id:status_monitor_id
        
"""


class PlanView(Screen): # This class is used to draw the layout for dispalying the functions of Planview
    pass


class SectionalMonitoring(Screen):#This class is used to draw the layout for dispalying functions of sectionalview
    pass


class StatusMonitoring(Screen):#This class is used to draw the layout for dispalying the functions of statusmonitoring
    pass


class MonitoringApp(App):  #This is the base class defined for the app
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_floor = 2  # for small simulation example
        self.schedule = None  # used to hold the clock schedule

    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        Clock.schedule_interval(self.update_all_towers, 2)  # update the towers every 2 seconds@ planview
        Clock.schedule_interval(self.update_all_status, 2) #update the screen for every 2 second@status_monitoring
        
    def update_all_towers(self, *args):#this function helps to update the staus of the Planview window selected by the user
        # create a list of the tower ids
        towers = [f'tower_{n}' for n in range(1, 14)]
        for tower in towers:
            self.root.ids.top_sm.get_screen('plan_view').ids[tower].update()
        
    def update_all_status(self, *args): #this function helps to update the status of the status_monitoring window selected by the user
        for w in self.root.ids.top_sm.get_screen('status_monitoring').ids.sv_box.children:
            w.ids.signals.set_new_state()
            

    def small_simulation(self): #This function is used to perform the simulation in the sectional_view
        #called from on_enter to start simulation when the screen is selected
        #If the selection of the spinner is TOWER-A then Tower_A is travelled from the 2nd floor to 6thfloor and the door is kept closed with 45% load while starting the simulation
        #once it reaches the 6th floor the door is kept open and the load capacity is set to zero.
        print('simulation started')
        self.current_floor = 2
        p = self.root.ids.top_sm.get_screen('sectional_view').ids
        p.tower_select.text = 'Tower-A'
        shafts = ['shaft_' + str(i) for i in range(2,7)]
        for shaft in shafts:
            p.sm.get_screen('A').ids[shaft].ids.door_1.state = 'open'
            p.sm.get_screen('A').ids.floor.set_info(int(shaft[-1]), '1')
            p.sm.get_screen('A').ids.capacity.set_info(int(shaft[-1]), '0%')
        ps = p.sm.get_screen('A').ids.shaft_1.ids
        ps.door_5.state = 'call'
        ps.door_2.state = 'open'
        p.sm.get_screen('A').ids.floor.set_info(1, '2')
        self.schedule = Clock.schedule_once(self.step_1, 3)

    def step_1(self, dt):
        p = self.root.ids.top_sm.get_screen('sectional_view').ids.sm.get_screen('A').ids.shaft_1.ids
        p.door_2.close_doors()
        p.door_2.state = 'closed'
        p.door_3.state = 'up'
        self.root.ids.top_sm.get_screen('sectional_view').ids.sm.get_screen('A').ids.capacity.set_info(1, '45%')
        self.schedule = Clock.schedule_once(self.step_2, 3)

    def step_2(self, dt):
        p = self.root.ids.top_sm.get_screen('sectional_view').ids.sm.get_screen('A').ids.shaft_1.ids
        if self.current_floor == 5:
            p.door_6.state = 'no car'
            p.door_5.open_doors()
            self.schedule = Clock.schedule_once(self.step_3, 2)
            return
        floors = [0, 1, 'door_2', 'door_3', 'door_4', 'door_5', 'door_6']
        self.current_floor += 1
        self.root.ids.top_sm.get_screen('sectional_view').ids.sm.get_screen('A').ids.floor.set_info(1, str(self.current_floor))
        p[floors[self.current_floor + 1]].state = 'up'
        p[floors[self.current_floor]].state = 'closed'
        p[floors[self.current_floor - 1]].state = 'no car'
        self.schedule = Clock.schedule_once(self.step_2, 2)

    def step_3(self, dt):
        p = self.root.ids.top_sm.get_screen('sectional_view').ids.sm.get_screen('A').ids
        p.capacity.set_info(1, '0%')
        shafts = ['shaft_' + str(i) for i in range(2, 7)]
        for shaft in shafts:
            p[shaft].ids.door_1.close_doors()
        self.schedule = Clock.schedule_once(self.step_4, 2)

    def step_4(self, dt):       
        p = self.root.ids.top_sm.get_screen('sectional_view').ids.sm.get_screen('A').ids
        shafts = ['shaft_' + str(i) for i in range(2, 7)]
        for shaft in shafts:
            p[shaft].ids.door_1.open_doors()
        print('Simulation Complete')
        self.schedule = None


sample_app = MonitoringApp()
sample_app.run()
