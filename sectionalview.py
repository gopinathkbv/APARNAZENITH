import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, OptionProperty, NumericProperty
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

kv = """
#:import utils kivy.utils
#:set burnt_orange 0.784, 0.443, 0.216, 1        
#:set black [0, 0, 0]
#:set white [1, 1, 1]
# using lists to append with alpha value
#:set gray [0.5, 0.5, 0.5]
#:set yellow [1, 1, 0]
#:set red [1, 0, 0]
#:set green [0, 1, 0]
#:set lt_blue [.678, .847, 90.2]  # light blue67.8% red, 84.7% green and 90.2% blue.

<ElevatorDoor>:
    # size_hint: None, None
    # size: 75, 30
    right_door_x: self.right - self.width/3
    left_door_width: self.width/3
    right_door_width: self.width/3
    
    canvas:
        Color:  # no_car
            rgba:white  + [self.state not in ('open', 'closed')]
        Rectangle:
            size: self.width / 3, self.height
            pos: self.x + self.width / 3, self.y
        Color: # outline
            rgb: black
        Line:
            width: 1
            rectangle: (*self.pos,*self.size)
        Color:  # call signal
            rgba: yellow + [self.state == 'call']   #  state to control opacity
        Ellipse:
            size: (self.width / 3) * .8, self.height * .8
            pos: self.center_x - (((self.width / 3) * .8 )/ 2), self.y + (self.height/2) * .2
        Color:  # down arrow
            rgba: red + [self.state == 'down']
        Triangle:
            points: (self.x, self.top, \
                     self.right, self.top, \
                     self.center_x, self.y)
        Color:  # up arrow
            rgba: green + [self.state == 'up']
        Triangle:
            points: (*self.pos, \
                     self.right, self.y, \
                     self.center_x, self.top)
                     
        Color: # doors open or closed
            rgba: lt_blue + [self.state in ('open', 'closed')]
        Rectangle:  # left door
            size: self.left_door_width - 2, self.height - 2
            pos: self.x + 1, self.y + 1
        Rectangle:  # right door
            size: self.right_door_width - 2, self.height -2
            pos: self.right_door_x + 1, self.y + 1
            
        Color:
            rgba: black + [self.state in ('open', 'closed')]
            
        Line: # left door edge
            width: 1
            points: (self.x + self.left_door_width, self.top, \
                     self.x + self.left_door_width, self.y)
                     
        Line: # right door edge
            width: 1
            points: (self.right_door_x, self.top, \
                     self.right_door_x, self.y)
    
<ElevatorShaft>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 5
        padding: 10
        
        
        ElevatorDoor:
            id: door_23
        ElevatorDoor:
            id: door_22
        ElevatorDoor:
            id: door_21 
        ElevatorDoor:
            id: door_20
        ElevatorDoor:
            id: door_19
        ElevatorDoor:
            id: door_18
        ElevatorDoor:
            id: door_17
        ElevatorDoor:
            id: door_16
        ElevatorDoor:
            id: door_15 
        ElevatorDoor:
            id: door_14
        ElevatorDoor:
            id: door_13
        ElevatorDoor:
            id: door_12
        ElevatorDoor:
            id: door_11
        ElevatorDoor:
            id: door_10
        ElevatorDoor:
            id: door_9 
        ElevatorDoor:
            id: door_8
        ElevatorDoor:
            id: door_7
        ElevatorDoor:
            id: door_6
        ElevatorDoor:
            id: door_5
        ElevatorDoor:
            id: door_4
        ElevatorDoor:
            id: door_3 
        ElevatorDoor:
            id: door_2
        ElevatorDoor:
            id: door_1
        

<FloorLabels>:
    orientation: 'vertical'
    size_hint_x: 0.5

<BackgroundText>:
    color: black + [1]
    canvas.before:
        Color:
            rgb:root.background_color
            #rgb: 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    bold:True
    
<SixInfoDisplay>:
    size_hint_y:None
    height: 25
    spacing:5
    BoxLayout:
        id: box
        spacing:2
        Label:
            text: root.text
            size_hint_x: 0.5
            
<ThreeInfoDisplay>:
    size_hint_y:None
    height: 25
    spacing:5
    BoxLayout:
        id: three
        spacing:2
        Label:
            text: root.text
            size_hint_x: 0.5
            
<Blank@Screen>:

<ScreenSixInfo@Screen>: 
    BoxLayout:
        orientation: 'vertical'
        spacing: 5
        SixInfoDisplay:
            id: cars
            text: 'Car'
        SixInfoDisplay:
            id:floor
            text: 'Floor'
        SixInfoDisplay:
            id:status
            text: 'Status'
        SixInfoDisplay:
            id:capacity
            text: 'Load'
        
        BoxLayout:
            FloorLabels:
            
            ElevatorShaft:
                id: shaft_1
            
            ElevatorShaft:
                id:shaft_2
                
            ElevatorShaft:
                id: shaft_3

            ElevatorShaft:
                id:shaft_4
            
            ElevatorShaft:
                id:shaft_5
            
            ElevatorShaft:
                id:shaft_6

            
            FloorLabels:
        
                
<ScreenThreeInfo@Screen>: 
    BoxLayout:
        orientation: 'vertical'
        spacing: 5
        ThreeInfoDisplay:
            id: cars
            text: 'Car'
        ThreeInfoDisplay:
            id:floor
            text: 'Floor'
        ThreeInfoDisplay:
            id:status
            text: 'Status'
        ThreeInfoDisplay:
            id:capacity
            text: 'Load'
        
        BoxLayout:
            FloorLabels:
            ElevatorShaft:
                id: shaft_1
            
            ElevatorShaft:
                id:shaft_2
                
            ElevatorShaft:
                id: shaft_3

            ElevatorShaft:
                id:shaft_4
            
            ElevatorShaft:
                id:shaft_5
            
            ElevatorShaft:
                id:shaft_6

            ElevatorShaft:
                id:shaft_7
            
            
            FloorLabels:
        
<SectionalView>:
    MySection:
        orientation:'vertical'
        canvas:
            Color:
                rgba:0.8274509803921568, 0.8274509803921568, 0.8274509803921568, 1
                
            Rectangle:
                size: self.size
                pos: self.pos
        
        Spinner:
            id: tower_select
            size_hint_y: None
            height:35
            background_color: .678, .847, 90.2,.45
            text: 'TOWERS'
            values: ('Tower-A', 'Tower-B', 'Tower-C', 'Tower-D', 'Tower-E', 'Tower-F', 'Tower-G', 'Tower-H', 'Tower-I', \
                 'Tower-J', 'Tower-K', 'Tower-L', 'Tower-M')
            on_text:
                sm.current = self.text[-1]
                root.select_tower(self.text[-1])
                
        ScreenManager:
            id: sm
            Blank:
                name: 'blank'
            ScreenSixInfo:
                name: 'A'
            ScreenSixInfo:
                name: 'B'
            ScreenSixInfo:
                name: 'C'
            ScreenSixInfo:
                name: 'D'
            ScreenSixInfo:
                name: 'E'
            ScreenSixInfo:
                name: 'F'
            ScreenSixInfo:
                name: 'G'
            ScreenSixInfo:
                name: 'H'
            ScreenSixInfo:
                name: 'I'
            ScreenSixInfo:
                name: 'J'
            ScreenSixInfo:
                name: 'K'
            ScreenSixInfo:
                name: 'L'
            ScreenThreeInfo:
                name: 'M' 
        
"""
Builder.load_string(kv)


class BackgroundText(Label):
    background_color = ListProperty([1,1,1])


class SixInfoDisplay(BoxLayout):
    text = StringProperty()

    def on_kv_post(self, base_widget):
        box = self.ids.box
        print(box)
        for i in range(6):
            bt = BackgroundText(text='--',color=(0, 0, 0, 1))
            box.add_widget(bt)
        box.add_widget(Label(size_hint_x=0.5))

    def set_car_names(self, tower):
        for i, bt in enumerate(self.ids.box.children[6:0:-1]):
            bt.text = tower + str(i + 1)

    def set_floor_rnd(self):
        for bt in self.ids.box.children[6:0:-1]:
            result = random.randint(1, 24)
            position = str(result)
            bt.text = position

    def set_info(self, stack, data): # stack number 1-6, and data to display
        fields = [f for f in self.ids.box.children[6:0:-1]]  # a list of the widgets in stack order
        fields[stack - 1].text = data

    def set_load(self):
        for bt in self.ids.box.children[6:0:-1]:
            load = random.randint(1, 100)
            average = str(load)
            bt.text = average + '%'

    def set_status(self):
        value = 'AUTO'
        for bt in self.ids.box.children[6:0:-1]:
            bt.text = value

    def __str__(self):
        try:
            b = self.ids.box.children
            return f'{b[6].text:7}: {b[5].text:6} {b[4].text:6} {b[3].text:6} {b[2].text:6} {b[1].text:6} {b[0].text:6}'
        except AttributeError:
            return ''


class ThreeInfoDisplay(BoxLayout):
    text = StringProperty()

    def on_kv_post(self, base_widget):
        three = self.ids.three
        for i in range(3):
            bt = BackgroundText(text='--')
            three.add_widget(bt)

        three.add_widget(Label(size_hint_x=0.5))

    def set_car_names(self, tower):
        print(self.ids.three.children)
        for i, bt in enumerate(self.ids.three.children[3:0:-1]):
            bt.text = tower + str(i + 1)

    def set_floor_rnd(self):
        for bt in self.ids.three.children[3:0:-1]:
            result = random.randint(1, 24)
            position = str(result)
            bt.text = position

    def set_info(self, stack, data): # stack number 1-6, and data to display
        fields = [f for f in self.ids.box.children[3:0:-1]]  # a list of the widgets in stack order
        fields[stack - 1].text = data

    def set_status(self):
        value = 'AUTO'
        for bt in self.ids.three.children[3:0:-1]:
            bt.text = value

    def set_load(self):
        for bt in self.ids.three.children[3:0:-1]:
            load = random.randint(1, 100)
            average = str(load)
            bt.text = average + '%'

    def __str__(self):
        try:
            b = self.ids.three.children
            return f'{b[3].text:7}: {b[2].text:6} {b[1].text:6} {b[0].text:6}'
        except AttributeError:
            return ''


class ElevatorDoor(BoxLayout):
    state = OptionProperty('no car', options=['no car', 'closed', 'open', 'call', 'up', 'down'])
    left_door_width = NumericProperty()
    right_door_width = NumericProperty()
    right_door_x = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.open_door_anim = None
        self.close_door_anim = None

    def open_doors(self):
        door_width = self.width / 3
        self.open_door_anim = Animation(left_door_width=door_width, right_door_width=door_width,
                                        right_door_x=self.right - door_width)
        self.open_door_anim.start(self)

    def close_doors(self):
        self.close_door_anim = Animation(left_door_width=self.width / 2, right_door_width=self.width / 2,
                                         right_door_x=self.center_x)
        self.close_door_anim.start(self)

    def on_state(self, instance, value):
        if value == 'closed':
            self.left_door_width = self.width / 2
            self.right_door_width = self.width / 2
            self.right_door_x = self.center_x


class ElevatorShaft(BoxLayout):
    pass


class FloorLabels(BoxLayout):
    def on_kv_post(self, base_widget):
        for i in range(23, 0, -1):
            self.add_widget(Label(text=str(i)))


class MySection(BoxLayout):
    pass
        

class SectionalView(Screen):
    def select_tower(self, tower):
        p = self.ids.sm.get_screen(tower).ids
        p.cars.set_car_names(tower)
        p.floor.set_floor_rnd()
        p.status.set_status()
        p.capacity.set_load()
        print(p.cars)
        print(p.floor)
        print(p.status)
        print(p.capacity)

    

    
    


if __name__ == '__main__':

    class SectionalViewApp(App):
        
        def build(self):
            return SectionalView()

    SectionalViewApp.run()

