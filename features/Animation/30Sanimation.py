from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    #GLfloat light_position [ ] = { 1.0, 1.0, 1.0, 0.0 }
    #GLfloat mat_diffuse[] = { 1.0, 1.0, 1.0, 1.0 }
    glClearColor ( 0.0,0.0,0.0, 0.0 ) #设置背景色为蓝色
    glShadeModel ( GL_SMOOTH )#选择平面明暗模式或光滑明暗模式

    glLightfv ( GL_LIGHT0, GL_POSITION,[1.0, 1.0, 1.0, 0.0])
    glEnable (GL_LIGHTING)
    glEnable (GL_LIGHT0)
    glEnable(GL_CULL_FACE)
    glEnable (GL_DEPTH_TEST)



