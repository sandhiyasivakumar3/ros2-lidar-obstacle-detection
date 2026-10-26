import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class ObstacleDetector(Node):

    def __init__(self):
        super().__init__('lidar_obstacle_detector')

        self.declare_parameter('obstacle_distance', 0.75)

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info(
            'LiDAR Obstacle Detector started. Waiting for /scan...'
        )

    def scan_callback(self, msg):
        threshold = float(
            self.get_parameter('obstacle_distance').value
        )

        valid_ranges = [
            distance for distance in msg.ranges
            if math.isfinite(distance)
            and msg.range_min <= distance <= msg.range_max
        ]

        if not valid_ranges:
            self.get_logger().warning('No valid LiDAR measurements.')
            return

        closest = min(valid_ranges)

        if closest < threshold:
            self.get_logger().warning(
                f'OBSTACLE DETECTED | Distance: {closest:.2f} m'
            )
        else:
            self.get_logger().info(
                f'PATH CLEAR | Nearest obstacle: {closest:.2f} m'
            )


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleDetector()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
