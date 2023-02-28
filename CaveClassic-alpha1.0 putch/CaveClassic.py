from ursina import *
from ursina.prefabs. \
    first_person_controller \
    import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import basic_lighting_shader
from ursina.shaders import texture_blend_shader
from ursina.shaders import normals_shader
import UrsinaLighting
import time
import win32api

app = Ursina()
# lit = LitInit()

sky_texture = load_texture('sky2.jpg')
punch_sound = Audio('music/Calm1.m4a',loop = True, autoplay = True)

sky = Entity(
           model='sphere', texture=sky_texture,
           scale=1000, double_sided=True
       )

player = FirstPersonController()
tex = ""
boxes = []
normal_speed = 2
player.gravity = 0.0
scene.fog_density = (0, 700) #700
scene.fog_color = color.white
shift_click = 2


for x_dynamic in range(16):
   for z_dynamic in range(16):
       e = Entity(model=Mesh(), texture="texture/grass")


def input(key):

  if key == 'o':
    quit()

  if key == 'shift':
    global shift_click
    if shift_click % 2 == 0:
      player.speed = normal_speed + 3
      shift_click += 1
    else:
      player.speed = normal_speed
      shift_click += 1


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture="texture/grass"):
        super().__init__(
            parent=scene, model='cube',
            scale=1, texture=texture, position=position,
            origin_y=0.5, color=color.color(0, 0, random.uniform(0.9, 1))
        )


    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                Voxel(position=self.position + mouse.normal, texture="texture/grass")

            if key == 'left mouse down':
                destroy(self)



for x_dynamic in range(16):
    for z_dynamic in range(16):
        Voxel(position=(x_dynamic, 0, z_dynamic))



def update():
    print(player.x, player.y, player.z)



win32api.LoadKeyboardLayout("00000409",1)
app.run()
