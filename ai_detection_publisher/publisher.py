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

