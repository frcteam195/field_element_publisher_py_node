#!/usr/bin/env python3

import tf
import tf2_ros
import geometry_msgs.msg
import rospy
import field_element_publisher_py_node.field_elements.constants as constants



def get_transforms():
    returned_transforms = []

    red_link_transform = geometry_msgs.msg.TransformStamped()
    red_link_transform.header.stamp = rospy.Time.now()
    red_link_transform.header.frame_id = "map"
    red_link_transform.child_frame_id = "red_link"
    red_link_transform.transform.translation.x = float(0)
    red_link_transform.transform.translation.y = float(0)
    red_link_transform.transform.translation.z = float(0)
    quat = tf.transformations.quaternion_from_euler(float(0),float(0),float(0))
    red_link_transform.transform.rotation.x = quat[0]
    red_link_transform.transform.rotation.y = quat[1]
    red_link_transform.transform.rotation.z = quat[2]
    red_link_transform.transform.rotation.w = quat[3]
    returned_transforms.append(red_link_transform)

    return returned_transforms