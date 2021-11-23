import random
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

kv = """
#:set label_width 120

<SignalImage>:
    source:self.rand_color()

<DirectionImage>:
    Label:
    Image:
        size_hint_x: 2
        source: {'Up': 'UP.png', 'Dn': 'DOWN.png'} [root.text]
    Label:
  
<RowHeader>:
    canvas:
        Color:
            rgba: .7, .7, .7, 1 # root.color was undefined.
        Rectangle:
            size:self.size
            pos:self.pos

<SixTowerSignals>:
    id:main_window
    orientation:'vertical'
    
    BoxLayout:
        BoxLayout:
            id:menus
            orientation:'vertical'
            RowHeader:
                id:options

            RowHeader:
                id:car_position

            RowHeader:
                id:door_status

            RowHeader:
                id:overload
                
            RowHeader:
                id:inspection
                
            RowHeader:
                id:service
                
            RowHeader:
                id:independent_mode
                
            RowHeader:
                id:run_stop

            RowHeader:
                id: fireman_switch

            RowHeader:
                id: fireman_emergency

            RowHeader:
                id: fireman_return


            RowHeader:
                id:malfunction

            RowHeader:
                id: floor

            RowHeader:
                id: direction

<ThreeTowerSignals>:
    id:main_window
    orientation:'vertical'
    
    BoxLayout:
        BoxLayout:
            id:menus
            orientation:'vertical'
            RowHeader:
                id:options

            RowHeader:
                id:car_position

            RowHeader:
                id:door_status

            RowHeader:
                id:overload
                
            RowHeader:
                id:inspection
                
            RowHeader:
                id:service
                
            RowHeader:
                id:independent_mode
                
            RowHeader:
                id:run_stop

            RowHeader:
                id: fireman_switch

            RowHeader:
                id: fireman_emergency

            RowHeader:
                id: fireman_return


            RowHeader:
                id:malfunction

            RowHeader:
                id: floor

            RowHeader:
                id: direction
 
"""
Builder.load_string(kv)


class DirectionImage(BoxLayout):
    text = StringProperty()


class RowHeader(BoxLayout):
    color = ListProperty()
    text = StringProperty()




class SignalImage(Image):
    text = StringProperty()  # stores value for printing

    def rand_color(self):
        colors = ['red_light.png', 'green_light.png']
        color = random.choice(colors)  # randomly assign a color to the input
        self.text = 'Red' if color.startswith('red') else 'Green'
        return color


class SixTowerSignals(BoxLayout):
    # Builds the matrix of data
    def on_kv_post(self, base_widget):
        for i in range(1, 7):
            t = f'E{i}'
            self.ids.options.add_widget(Label(text=t, bold=True))  # Headings

        names = [k for k in self.ids.keys()][2:13]  # Changed range for new layout
        print(len(names))
        print(names)
        for row in names:
            for i in range(1, 7):
                self.ids[row].add_widget(SignalImage())  # Signals
        for i in range(1, 7):
            self.ids.floor.add_widget(Label(text=self.set_floor(), markup=True,
                                            bold=True, font_size=30, color=(0, 0, 0, 1)))  # Floor
            self.ids.direction.add_widget(DirectionImage(text=self.set_direction()))  # Direction

    def get_signals(self, floor):
        floor = 6 - floor
        names = [k for k in self.ids.keys()][1:9]  # the names/id of each of the signals
        print("The name of the get_signals:"+names)
        return [self.ids[row].children[floor].text for row in names]

    @staticmethod
    def set_direction():
        direction = ['Up', 'Dn']
        return random.choice(direction)

    @staticmethod
    def set_floor():
        floor = random.randint(1, 23)
        floor_label = str(floor)
        return floor_label

    def get_direction(self, elevator):
        elevator = 6 - elevator
        return self.ids.direction.children[elevator].text

    def output(self, elevator):
        symbol = {'Up': u'\N{UPWARDS ARROW}', 'Dn': u'\N{DOWNWARDS ARROW}'}
        direction = symbol[self.get_direction(elevator)]
        signals = self.get_signals(elevator)
        return [str(elevator), signals, direction]

    def set_new_state(self):  # update all signals, floors and directions
        names = [k for k in self.ids.keys()][2:13]
        for row in names:
            for i in range(0, 6):
                self.ids[row].children[i].source = self.ids[row].children[i].rand_color()
        for i in range(0, 6):
            self.ids.floor.children[i].text = self.set_floor()  # Floor
            self.ids.direction.children[i].text = self.set_direction()  # Direction




class ThreeTowerSignals(BoxLayout):
    # Builds the matrix of data
    def on_kv_post(self, base_widget):
        for i in range(1, 4):
            t = f'E{i}'
            self.ids.options.add_widget(Label(text=t, bold=True))  # Headings

        names = [k for k in self.ids.keys()][2:13]  # Changed range for new layout
        for row in names:
            for i in range(1, 4):
                self.ids[row].add_widget(SignalImage())  # Signals
        for i in range(1, 4):
            self.ids.floor.add_widget(Label(text=self.set_floor(), markup=True,
                                            bold=True, font_size=30, color=(0, 0, 0, 1)))  # Floor
            self.ids.direction.add_widget(DirectionImage(text=self.set_direction()))  # Direction

    def get_signals(self, floor):
        floor = 3 - floor
        names = [k for k in self.ids.keys()][1:9]  # the names/id of each of the signals
        return [self.ids[row].children[floor].text for row in names]

    @staticmethod
    def set_direction():
        direction = ['Up', 'Dn']
        return random.choice(direction)

    @staticmethod
    def set_floor():
        floor = random.randint(1, 23)
        floor_label = str(floor)
        return floor_label

    def get_direction(self, elevator):
        elevator = 3 - elevator
        return self.ids.direction.children[elevator].text

    def output(self, elevator):
        symbol = {'Up': u'\N{UPWARDS ARROW}', 'Dn': u'\N{DOWNWARDS ARROW}'}
        direction = symbol[self.get_direction(elevator)]
        signals = self.get_signals(elevator)
        return [str(elevator), signals, direction]

    def set_new_state(self):  # update all signals, floors and directions
        names = [k for k in self.ids.keys()][2:13]
        for row in names:
            for i in range(0, 3):
                self.ids[row].children[i].source = self.ids[row].children[i].rand_color()
        for i in range(0, 3):
            self.ids.floor.children[i].text = self.set_floor()  # Floor
            self.ids.direction.children[i].text = self.set_direction()  # Direction
            


