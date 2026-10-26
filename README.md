# ROS 2 LiDAR Obstacle Detection

A Python-based robotics project that detects nearby obstacles using LiDAR scan data in ROS 2 Humble.

## Features
- Subscribes to the /scan topic.
- Processes LaserScan measurements.
- Filters invalid distance readings.
- Finds the nearest measured obstacle.
- Uses a configurable detection threshold.
- Reports obstacle detection and clear-path status.

## Technology Stack
- ROS 2 Humble
- Python 3
- rclpy
- sensor_msgs
- Ubuntu Linux

## Installation

```bash
source /opt/ros/humble/setup.bash
cd ~/ros2_portfolio_ws
colcon build --packages-select lidar_obstacle_detector
source install/setup.bash
ros2 run lidar_obstacle_detector obstacle_detector
source /opt/ros/humble/setup.bash
ros2 topic pub -r 2 /scan sensor_msgs/msg/LaserScan "{header: {frame_id: laser}, angle_min: -1.57, angle_max: 1.57, angle_increment: 0.01, range_min: 0.1, range_max: 10.0, ranges: [0.4, 1.5, 2.0, 3.0]}"

## Step 2 — Create a GitHub repository

Open [GitHub](https://github.com?utm_source=chatgpt.com).

1. Sign in.
2. Click **New repository**.
3. Name it `ros2-lidar-obstacle-detection`.
4. Select **Public**.
5. Click **Create repository**.

## Step 3 — Upload your code

Back in the terminal:

```bash
cd ~/ros2_portfolio_ws

cat > .gitignore <<'EOF'
build/
install/
log/
__pycache__/
*.pyc
