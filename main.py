import pyglet
pyglet.options["shadow_window"]= False
pyglet.options["debug_gl"]= False

import pyglet.gl as gl

#class extending pyglet.window.Window
class Window((pyglet.window.Window)):
    def __init__(self,**args):
        super().__init__(**args)

    def on_draw(self):
        gl.glClearColor(1.0, 0.5,1.0, 1.0)
        self.clear()

    def on_resize(self, width, height):
        print(f"resize: {width} x {height}")

class Game:
    def __init__(self):
        self.config = gl.Config(double_buffer = True, major_version = 3, minor_version = 3)
        self.window = Window(config = self.config, width = 700, height = 450, resizable = True)
    
    def run(self):
        pyglet.app.run()

#run game only if source file being run
if __name__ == "__main__":
    game = Game()
    game.run()