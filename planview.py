"""
The PlanView section is used to display the floor number,direction of the elevator travelling and the status of the door[opening/closing]. 

"""
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

kv = """
#:import utils kivy.utils #Kivy has utils module with get_color_from_hex function

<SixElevatorTower>:  #This layout helps to draw the six elevator and it will be instantiated no of times it is called by the user
    orientation:'vertical'
    spacing:2
    padding: [10, 5]   #  [padding_horizontal, padding_vertical] Padding between the layout box and its children
    canvas: #this section is used to draw the line above the rectangle defined in the sixTower
        Color:
            rgba:0, 0, 0, 0.4
        Line:
            width: 1
            rectangle: (*self.pos, *self.size)
    Label: # This helps to display the Tower name 
        text:'Tower-'+root.tower_name
        bold:True
        font_size:22
        markup:True
        size_hint_y: None
        height: self.texture_size[1]
    
    BoxLayout: #This layout is used to generate the tower_label[A1....A6] for six elevators
        id: elevator_bank
        spacing: 10
        Elevator:
            elevator_name: root.tower_name + '1'
        Elevator:
            elevator_name: root.tower_name + '2'
        Elevator:
            elevator_name: root.tower_name + '3'
        Elevator:
            elevator_name: root.tower_name + '4'
        Elevator:
            elevator_name: root.tower_name + '5'
        Elevator:
            elevator_name: root.tower_name + '6'

    
<ThreeElevatorTower>: #This layout helps to draw the three elevator  and it will be instantiated no of times it is called by the user
    orientation:'vertical'
    spacing:4
    padding:[10, 5]   #  [padding_horizontal, padding_vertical] Padding between the layout box and its children
    canvas: #this section is used to draw the line above the rectangle defined
        Color:
            rgba:0, 0, 0, 0.4
        Line:
            width: 1
            rectangle: (*self.pos, *self.size)
    Label:  #this section is used to draw the line above the rectangle defined in threeTower
        text:'Tower-'+root.tower_name
        bold:True
        font_size:22
        markup:True
        size_hint_y: None
        height: self.texture_size[1]
        
    BoxLayout: #This layout is used to generate tower_label[A1....A3] for three elevators
        id: elevator_bank
        spacing: 5
        Elevator:
            elevator_name: root.tower_name + '1'
        Elevator:
            elevator_name:root.tower_name + '2'
        Elevator:
            elevator_name: root.tower_name + '3'
   
     
<Elevator>: #This layout is defined for displaying the elevator floor number, direction, door_status and elevator name
    orientation:'vertical'
    canvas.before:
        Color:
           rgb:utils.get_color_from_hex('#66CCFF')
        Rectangle:
            pos: self.pos
            size: self.size
    Image: #This is used to display the status of the door closed /open
        id: door
        source:'Door.png'
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height:20
        
    BoxLayout:
        padding: [0,4,0,0] # [padding_left, padding_top, padding_right, padding_bottom]
        Label: #This label is used to display the text of the elevator position
            id:floor
            text:str(root.elevator_position())
            bold:True
            markup:True
            font_size:30
            size_hint_x: None
            spacing:2
        Image: #it shows the direction of the elevator
            id:direction
            source:root.elevator_direction()
            valign:'middle'
            
    Label: #This label is used to display the text of the elevator name
        text: root.elevator_name
        size_hint_y:None
        height: self.texture_size[1]

<PlanView>: #This is the root class for the planview applications it comprises all the widget defined for the planviewapp it contains thirteen boxlayout
            #defined for the 13 towers inside the layout
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba:0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1
            Rectangle:
                size: self.size
                pos: self.pos

        BoxLayout:     
            orientation: 'vertical'
            spacing:8
            padding: 10
            BoxLayout:
                spacing: 8
                SixElevatorTower:
                    id:tower_1
                    tower_name: 'A'
    
                SixElevatorTower:
                    id:tower_2
                    tower_name: 'B'
            BoxLayout:
                spacing: 8
                SixElevatorTower:
                    id:tower_3
                    tower_name: 'C'
    
                SixElevatorTower:
                    id:tower_4
                    tower_name: 'D'
            BoxLayout:
                spacing: 8
                SixElevatorTower:
                    id:tower_5
                    tower_name: 'E'
    
                SixElevatorTower:
                    id:tower_6
                    tower_name: 'F'
            BoxLayout:
                spacing: 8
                SixElevatorTower:
                    id:tower_7
                    tower_name: 'G'
    
                SixElevatorTower:
                    id:tower_8
                    tower_name: 'H'
            BoxLayout:
                spacing: 8
                SixElevatorTower:
                    id:tower_9
                    tower_name: 'I'
    
                SixElevatorTower:
                    id:tower_10
                    tower_name: 'J'
            BoxLayout:
                spacing: 8
                SixElevatorTower:
                    id:tower_11
                    tower_name: 'K'
    
                SixElevatorTower:
                    id:tower_12
                    tower_name: 'L'

            BoxLayout:
                Label:
                    text: 'plan view_meleye'
                    bold:True
                    markup:True
                    font_size:20
                    
                ThreeElevatorTower:
                    size_hint_x: None
                    width: (tower_1.width / 2) + (2 * tower_1.spacing)
                    id:tower_13
                    tower_name: 'M'
                Image:
                    source:'capture.jpg'
                    
"""
Builder.load_string(kv)


class SixElevatorTower(BoxLayout):
    text = StringProperty()
    tower_name = StringProperty()

    def update(self):
        for elevator in self.ids.elevator_bank.children:  # children is a list of child widgets
            elevator.update()  # calling the elevator method that updates one elevator.


class ThreeElevatorTower(BoxLayout):
    text = StringProperty()
    tower_name = StringProperty()

    def update(self):
        for elevator in self.ids.elevator_bank.children:  # children is a list of child widgets
            elevator.update()  # calling the elevator method that updates one elevator.


class Elevator(BoxLayout):
    text = StringProperty()
    elevator_name = StringProperty()

    def elevator_direction(self):  # function to display the elevator_direction
        lst = ['Up.png', 'Down.png']
        movement = random.choice(lst)
        return movement

    def elevator_position(self):  # function to display the elevator_position
        for i in range(1, 7):
            result = random.randint(1, 6)
            position = str(result)
            return position

    def update(self): #function to update all the widgets defined in the elevator class
        self.ids.door.opacity = random.choice([0, 1])
        self.ids.direction.source = self.elevator_direction() #Remove the observer from the widget observer list bound with fbind. It removes the first match it finds, as opposed to unbind which searches for all matches.
        self.ids.floor.text = self.elevator_position()


class PlanView(Screen):
    pass


if __name__ == '__main__':

    class PlanViewApp(App):
        def build(self):
            return PlanView()

    PlanViewApp().run()

    
