# ai_detection_publisher

Publishes fake AI detections on a ros topic

## related info

- Run ROSBridge, a WebSocket interface layer to ROS, and read the messages in C#
- DotNet detection-manager prototype: https://github.com/henrywarhurst/detection-manager

## to run this code

- Make a ros workspace if you don't already have one: `mkdir -p ~/dev_ws/src && cd ~/dev_ws/src`
- Build the package:
```
cd ~/dev_ws
git clone <this repo>
cd ..
colcon build --packages-select ai_detection_publisher
source ~/dev_ws/install/setup.bash
```

- Run the package
```
ros2 run ai_detection_publisher publisher
```

## Prerequisite: set up ROS in docker

```
docker pull ros:foxy
 docker run -it --name my-ros-foxy-container -p 9090:9090 ros:foxy 
apt-get update && apt-get install -y ros-foxy-rosbridge-server
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```

## Background: how was this repo created?

```
mkdir -p ~/dev_ws/src
cd ~/dev_ws/src
ros2 pkg create --build-type ament_python ai_detection_publisher --dependencies rclpy std_msgs
cd ai_detection_publisher
```

#### make publisher.py:

```
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Replace with your message type
import json
import time

class DummyPublisher(Node):
    def __init__(self):
        super().__init__('dummy_ai_publisher')
        self.publisher_ = self.create_publisher(String, 'ai_detections', 10)  # Replace String with your message type
        self.timer = self.create_timer(1, self.publish_dummy_data)

    def publish_dummy_data(self):
        fake_detection = {
            "timestamp": time.time(),
            "top_left": [100, 200],
            "width": 50,
            "height": 100
        }
        self.publisher_.publish(String(data=json.dumps(fake_detection)))  # Replace String with your custom message type
        self.get_logger().info('Publishing: "%s"' % fake_detection)

def main(args=None):
    rclpy.init(args=args)
    dummy_publisher = DummyPublisher()
    rclpy.spin(dummy_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

#### make setup.py in the same dir

```
from setuptools import setup

package_name = 'ai_detection_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Example package for AI Detection Publisher',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = ai_detection_publisher.publisher:main'
        ],
    },
)
```
