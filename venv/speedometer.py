from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App

class SpeedWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

KV = """

WindowManager:
    SpeedWindow:

<SpeedWindow>:
    angle: 90    # angle for needle
    name: 'speedometer'    # every Screen needs a name

    Image:
        source: 'cadran.png'
        size_hint: None, None
        size: 400, 400
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    Image:
        source: 'needle.png'
        size_hint: None, None
        size: 300, 300
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}   
        # apply rotation matrix to this Image                                                                                                                                            
        canvas.before:                                                                                                                                             
            PushMatrix                                                                                                                                             
            Rotate:                                                                                                                                                
                angle: root.angle                                                                                                                                  
                axis: (0, 0, 1)                                                                                                                                    
                origin: (self.center_x, self.center_y - self.norm_image_size[1]/2, 0)                                                                                                                              
        canvas.after:                                                                                                                                              
            PopMatrix                           

"""



class MyMainApp(App):
    def build(self):
        Clock.schedule_once(self.animate_needle, 2.0)  # start the animation in 2 seconds
        return  Builder.load_string(KV)

    def animate_needle(self, dt):
        # animate the needle from +90 to -90 and then back to +90
        self.anim = Animation(angle=-90.0) + Animation(angle=90)
        self.anim.repeat = True    # repeat forever
        speedometer = self.root.get_screen('speedometer')
        self.anim.start(speedometer)

if __name__ == "__main__":
    MyMainApp().run()