#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

import pygame
from pygame.locals import *

gyro_x_val=0
gyro_y_val=0
gyro_z_val=0

accel_x_val=0
accel_y_val=0
accel_z_val=0

mag_x_val=0
mag_y_val=0
mag_z_val=0

def gx_callback(data):
  global gyro_x_val
  gyro_x_val=data.data

def gy_callback(data):
  global gyro_y_val
  gyro_y_val=data.data

def gz_callback(data):
  global gyro_z_val
  gyro_z_val=data.data

def ax_callback(data):
  global accel_x_val
  accel_x_val=data.data

def ay_callback(data):
  global accel_y_val
  accel_y_val=data.data

def az_callback(data):
  global accel_z_val
  accel_z_val=data.data

def mx_callback(data):
  global mag_x_val
  mag_x_val=data.data

def my_callback(data):
  global mag_y_val
  mag_y_val=data.data

def mz_callback(data):
  global mag_z_val
  mag_z_val=data.data


class Display:
    def __init__(self):
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber("gyro_x", Int16, gx_callback)
        rospy.Subscriber("gyro_y", Int16, gy_callback)
        rospy.Subscriber("gyro_z", Int16, gz_callback)
        rospy.Subscriber("accel_x", Int16, ax_callback)
        rospy.Subscriber("accel_y", Int16, ay_callback)
        rospy.Subscriber("accel_z", Int16, az_callback)
        rospy.Subscriber("mag_x", Int16, mx_callback)
        rospy.Subscriber("mag_y", Int16, my_callback)
        rospy.Subscriber("mag_z", Int16, mz_callback)

        pygame.init()
        pygame.display.set_caption("python ROV Display")
        
        self.screen = pygame.display.set_mode((800,600))
        self.font = pygame.font.SysFont("Courier", 12)

    def draw_text(self, text, x, y, color):
        surface = self.font.render(text, True, color, (0,0,0))
        surface.set_colorkey((0,0,0))
        self.screen.blit(surface, (x,y))

    def main(self):
        while True:
            self.in_keys = pygame.event.get()
            self.screen.fill(0)

            for event in self.in_keys:
                if (event.type ==KEYDOWN and event.key == K_ESCAPE):
                    self.quit()
                    return
                elif event.type == QUIT:
                    self.quit()
                    return
                 
            #ser.write(chr(254))
            self.draw_text("gyroX: %i," % int(gyro_x_val),  5,5,(255,127,255))
            self.draw_text("gyroY: %i," % int(gyro_y_val),205,5,(255,127,255))
            self.draw_text("gyroZ: %i"  % int(gyro_z_val),405,5,(255,127,255))

            self.draw_text("accelX: %i," % int(accel_x_val),  5,25,(127,255,255))
            self.draw_text("accelY: %i," % int(accel_y_val),205,25,(127,255,255))
            self.draw_text("accelZ: %i"  % int(accel_z_val),405,25,(127,255,255))

            self.draw_text("magX: %i," % int(mag_x_val),  5,45,(255,255,127))
            self.draw_text("magY: %i," % int(mag_y_val),205,45,(255,255,127))
            self.draw_text("magZ: %i"  % int(mag_z_val),405,45,(255,255,127))

            pygame.display.flip()
    
    def quit(self):
        pygame.display.quit()
        self.ser.close()

display = Display()
display.main()
            













