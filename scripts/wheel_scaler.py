#!/usr/bin/env python3

"""
   wheel_scaler
   scales the wheel readings (and inverts the sign)
   
     Copyright (C) 2012 Jon Stephan. 
     
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
   
"""

import rospy
import roslib

from std_msgs.msg import Int16

def scaleWheel():
    rospy.init_node("wheel_scaler")
    rospy.loginfo("wheel_scaler started")
    
    scale = rospy.get_param('distance_scale', 1)
    rospy.loginfo("wheel_scaler scale: %0.2f", scale)
    
    lscaled_pub = rospy.Publisher("lwheel_scaled", Int16, queue_size=10)
    rscaled_pub = rospy.Publisher("rwheel_scaled", Int16, queue_size=10) 
    
    rospy.Subscriber("lwheel", Int16, lwheelCallback, (lscaled_pub, scale))
    rospy.Subscriber("rwheel", Int16, rwheelCallback, (rscaled_pub, scale))

    # ### testing sleep CPU usage
    # r = rospy.Rate(50) 
    # while not rospy.is_shutdown:
    #     r.sleep()
        
    rospy.spin()

def lwheelCallback(msg, args):
    args[0].publish( msg.data * -1 * args[1])

def rwheelCallback(msg, args):
    args[0].publish( msg.data * -1 * args[1])


if __name__ == '__main__':
    """main"""
    try:
        scaleWheel()
    except rospy.ROSInterruptException:
        pass
