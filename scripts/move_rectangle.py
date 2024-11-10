#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def move_rectangle():
    # Initialize the ROS node
    rospy.init_node('move_turtle_rectangle_node', anonymous=True)
    
    # velocity commands to the turtle
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    #rate at which the loop will run (20 Hz for more precision)
    rate = rospy.Rate(20)
    
    #Twist message to set linear and angular velocity
    vel_msg = Twist()
    
    # parameters for rectangle movement
    linear_speed = 0.5  # Slower speed for more accuracy
    angular_speed = 0.6  # Adjusted for more precise turns
    side_length_x = 4.0  # Length of rectangle
    side_length_y = 2.0  # Width of rectangle
    PI = 3.14159265359
    
    # Initialize velocities to zero
    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0
    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0
    
    rospy.loginfo("Moving the turtle in a rectangle...")
    
    while not rospy.is_shutdown():
        # Move length (x)
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = 0.0
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        
        while current_distance < side_length_x:
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = linear_speed * (t1 - t0)
            rate.sleep()
            
        # Stop before turning
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)  # Short pause for stability
        
        # Turn 90 degrees
        vel_msg.angular.z = angular_speed
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        
        while current_angle < (PI/2):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
            rate.sleep()
            
        # Stop after turning
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)  # Short pause for stability
        
        # Move width (y)
        vel_msg.linear.x = linear_speed
        current_distance = 0
        t0 = rospy.Time.now().to_sec()
        
        while current_distance < side_length_y:
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = linear_speed * (t1 - t0)
            rate.sleep()
            
        # Stop before turning
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        
        # Turn 90 degrees
        vel_msg.angular.z = angular_speed
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        
        while current_angle < (PI/2):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
            rate.sleep()
            
        # Stop after turning
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        
        # Move length (x)
        vel_msg.linear.x = linear_speed
        current_distance = 0
        t0 = rospy.Time.now().to_sec()
        
        while current_distance < side_length_x:
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = linear_speed * (t1 - t0)
            rate.sleep()
            
        # Stop before turning
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        
        # Turn 90 degrees
        vel_msg.angular.z = angular_speed
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        
        while current_angle < (PI/2):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
            rate.sleep()
            
        # Stop after turning
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        
        # Move width (y)
        vel_msg.linear.x = linear_speed
        current_distance = 0
        t0 = rospy.Time.now().to_sec()
        
        while current_distance < side_length_y:
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = linear_speed * (t1 - t0)
            rate.sleep()
            
        # Stop before final turn
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.5)
        
        # Final 90 degree turn
        vel_msg.angular.z = angular_speed
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        
        while current_angle < (PI/2):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
            rate.sleep()
            
        # Stop after completing rectangle
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(1)  # Pause before next rectangle

if __name__ == '__main__':
    try:
        move_rectangle()
    except rospy.ROSInterruptException:
        pass
