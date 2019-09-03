#import pyglet
import pyglet
#Define image
image = pyglet.resource.image('Twi.png')
#Make Window
window = pyglet.window.Window()
#Make Label
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
#Draw thing I guess
@window.event
def on_draw():
    window.clear()
	image.blit(0, 0)
    label.draw()
#Run Window
pyglet.app.run()
