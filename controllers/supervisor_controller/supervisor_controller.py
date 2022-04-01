"""supervisor_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor


TIME_STEP = 32

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


i = 0

bb8_node = robot.getFromDef('BB-8')
translation_field = bb8_node.getField('translation')


root_node = robot.getRoot()
children_field = root_node.getField('children')
children_field.importMFNode(-1,"custom_ball.wbo")
ball_node=robot.getFromDef("BALL")
appearance_node = robot.getFromDef("SPHERE_COLOR")
color_field = appearance_node.getField("baseColor")


while robot.step(timestep) != -1:
   
    position = ball_node.getPosition()
    print('Ball position: %f %f %f\n' %(position[0], position[1], position[2]))
   
    """ 
    if i == 0:
      new_value = [2.5, 0, 0]
      translation_field.setSFVec3f(new_value)       
    #if i==10:
      #  bb8_node.remove()
    if i == 20:
        children_field.importMFNodeFromString(-1, 'Nao {translation 2.5 0 0.334}')
    """
    if position[2] < 0.2:
      red_color = [1, 0, 0]
      color_field.setSFColor(red_color)

       
    i+= 1      
     

   
