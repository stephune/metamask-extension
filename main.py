import kivy
kivy.require('2.0.0') # Specify Kivy version if necessary

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle, Mesh
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window as KivyWindow # To avoid name clash with our AcidWindow

import math
import random

class AcidWindow(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = kwargs.get('title', 'Acid Window')
        self.padding = [20, 20, 20, 40] # top, right, bottom, left - giving space for title bar at bottom for now

        with self.canvas.before:
            # Window Background
            self.bg_color = Color(0.1, 0.1, 0.15, 1) # Dark background
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

            # Border Color - will be animated
            self.border_color = Color(random.random(), random.random(), random.random(), 1)
            self.border_line = Line(width=2) # Will set points later

        # Content Area - simple placeholder
        self.content_area = FloatLayout(size_hint=(1,1)) # Occupies space within padding
        # self.add_widget(self.content_area) # Add content area after canvas setup

        # Title Bar (drawn on canvas for now, could be a separate widget)
        # For simplicity, drawing title bar elements directly on the canvas.
        # A real title bar would handle drag, close buttons etc.
        self.title_label = Label(text=self.title, font_size='15sp', size_hint=(None, None), height=30)
        # Position will be updated in on_size

        self.bind(pos=self._update_graphics, size=self._update_graphics)

        # Start animation for border
        Clock.schedule_interval(self._animate_border, 1/30) # 30 FPS for smoother animation
        self._update_graphics() # Initial draw

    def _animate_border(self, dt):
        # Animate border color
        r, g, b, a = self.border_color.rgba
        r = (r + random.uniform(-0.05, 0.05)) % 1.0
        g = (g + random.uniform(-0.05, 0.05)) % 1.0
        b = (b + random.uniform(-0.05, 0.05)) % 1.0
        self.border_color.rgba = [max(0, min(1, val)) for val in (r,g,b)] + [a] # Clamp between 0 and 1

        # Animate border points slightly for a "wobbly" effect
        # This will re-trigger _update_graphics if we directly change self.pos or self.size
        # For now, let's just update the points directly in the Line instruction
        # This is less "Kivy-idiomatic" for complex changes but fine for this.
        new_points = []
        for i in range(0, len(self.border_line.points), 2):
            px, py = self.border_line.points[i], self.border_line.points[i+1]
            # Compare with original base points from self.border_points if structure was different
            # Here, we just make them slightly jitter around their current position
            # For a more controlled "breathing" use math.sin or similar with Clock.get_time()
            new_points.extend([
                px + random.uniform(-0.5, 0.5),
                py + random.uniform(-0.5, 0.5)
            ])
        # To ensure the loop closes correctly, make the last point same as first
        if len(new_points) > 1:
            new_points[-2], new_points[-1] = new_points[0], new_points[1]
        self.border_line.points = new_points


    def _update_graphics(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

        # Simple rectangular border for now
        x, y = self.pos
        w, h = self.size

        # Define points for a slightly irregular border
        # For a truly "blobby" border, a Mesh would be better, but Line is simpler for a start
        self.border_points = [
            x + random.uniform(-1,1)*2, y + random.uniform(-1,1)*2,  # bottom-left
            x + w + random.uniform(-1,1)*2, y + random.uniform(-1,1)*2,  # bottom-right
            x + w + random.uniform(-1,1)*2, y + h + random.uniform(-1,1)*2,  # top-right
            x + random.uniform(-1,1)*2, y + h + random.uniform(-1,1)*2,  # top-left
            x + random.uniform(-1,1)*2, y + random.uniform(-1,1)*2  # close loop
        ]
        self.border_line.points = self.border_points
        self.canvas.before.add(self.border_color) # Ensure color is updated if changed
        self.canvas.before.add(self.border_line)

        # Update title label position (simple bottom title bar for now)
        self.title_label.text = self.title
        self.title_label.size = self.title_label.texture_size
        self.title_label.pos = (self.x + (self.width - self.title_label.width)/2 , self.y + 5)

        # Ensure title is drawn on top of the background and border
        # This is a bit tricky with canvas.before. For robust layering,
        # child widgets or canvas.after would be better for the title.
        # For now, we'll add it as a widget so it's drawn after canvas.before.
        if self.title_label not in self.children:
             self.add_widget(self.title_label)
        if self.content_area not in self.children: # Add content area
            self.add_widget(self.content_area)
            # Example content:
            # self.content_area.add_widget(Label(text="Window Content Here", center_x=self.content_area.center_x, center_y=self.content_area.center_y))


class AcidTripApp(App):
    def build(self):
        KivyWindow.clearcolor = (0.05, 0.05, 0.05, 1) # Dark app background
        root = FloatLayout()

        # Instantiate AcidWindow
        self.acid_window = AcidWindow(title="My First Acid Window",
                                      size_hint=(0.7, 0.6),
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Add some placeholder content to the AcidWindow's content_area
        content_label = Label(text="This is the content area!\n\nIt should respect the window's padding.",
                              halign='center', valign='middle',
                              text_size=(self.acid_window.width * 0.8, None)) # Enable wrapping

        # We need to delay adding the content label until acid_window's content_area is sized
        def add_content_label(*args):
            content_label.text_size=(self.acid_window.content_area.width * 0.9, None)
            content_label.center_x = self.acid_window.content_area.center_x
            content_label.center_y = self.acid_window.content_area.center_y
            self.acid_window.content_area.add_widget(content_label)

        Clock.schedule_once(add_content_label, 0.1) # Schedule after initial layout

        root.add_widget(self.acid_window)
        return root

if __name__ == '__main__':
    AcidTripApp().run()
