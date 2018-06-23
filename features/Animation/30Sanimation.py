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
    glFrontFace(GL_CW)


def changeSize(w,h):
    if h==0:
        h=1

    glViewport(0,0,w,h)#设置机口
    glMatrixMode(GL_PROJECTION)#指定哪一个矩阵时当前矩阵
    glLoadIdentity()
    gluPerspective(45.0,w/h,0.01,200)#创建透视投影矩阵
    glMatrixMode(GL_MODELVIEW)

def reSize(w,h):
    glViewport(0,0,w,h)#设置机口


