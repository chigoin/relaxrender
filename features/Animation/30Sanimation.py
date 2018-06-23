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
    glMatrixMode(GL_PROJECTION)  # 指定哪一个矩阵时当前矩阵
    glLoadIdentity()
    gluPerspective(60.0, w / h, 1.0, 20)  # 创建透视投影矩阵
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 5, 5, 0, 0, 0, 0, 1, 0)

rotate_Y = 1

def drawFunc():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global rotate_Y
    rotate_Y = rotate_Y + 0.1
    glPushMatrix()
    glTranslate(0, 0, -3)  # 绘图函数，移动当前绘图原点
    glRotate(rotate_Y, 0, 1, 0)  # 是一个旋转矩阵乘以当前矩阵
    glMaterialfv(GL_BACK, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])  # 指定用于光照计算的当前材质属性
    # glMaterialfv(GL_FRONT, GL_AMBIENT, mat_specular)
    glutSolidTeapot(0.5)
    glutSolidSphere(1, 10, 8)
    glPopMatrix()
    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    glPushMatrix()
     glPushMatrix()
    #glTranslate(0, 0, -3)#绘图函数，移动当前绘图原点
    glutWireSphere(1, 20, 16)
    # glRotatef(0, 0, 1, 0 GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glPopMatrix()
   # glutSwapBuffers())
    # glTranslatef(3, 0, 0)
    # glRotatef(0, 0, 1, 0)

   # glMaterialfv(GL_BACK, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glPopMatrix()
   # glutSwapBuffers()
    glFlush()


glutInit()#固定格式
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA | GLUT_DEPTH)#缓存模式
glutInitWindowSize(400, 400)#显示框大小
glutInitWindowPosition(100, 100)#确定显示框左上角的位置
glutCreateWindow("30s animation")



