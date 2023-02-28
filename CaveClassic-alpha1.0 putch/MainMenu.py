from ursina import *

app = Ursina(title="CaveClassicAlphaVersion-Menu")

# создаем объект на базе Entity, настраиваем камеру и бэкграунд
class MenuMenu(Entity):
   def __init__(self, **kwargs):
       super().__init__(parent=camera.ui, ignore_paused=True)

       self.main_menu = Entity(parent=self, enabled=True)
       self.background = Sky(model = "cube", double_sided = True, texture = Texture("UrsinaLighting/textures/skybox1.jpg"), rotation = (0, 90, 0))

# стартовая надпись Minecraft
       Text("CaveClassicAlphaVersion", parent = self.main_menu, y=0.4, x=0, origin=(0,0))

       def switch(menu1, menu2):
           menu1.enable()
           menu2.disable()

# вместо print_on_screen можно вписать lambda-функцию для запуска игры
       ButtonList(button_dict={
           "Start": Func(print_on_screen,"You clicked on Start button!", position=(0,.2), origin=(0,0)),
           "Exit": Func(lambda: application.quit())
       },y=0,parent=self.main_menu)

main_menu = MenuMenu()

app.run()