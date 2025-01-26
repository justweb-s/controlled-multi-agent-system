import os
import math
import logging
import logging.config
import yaml

# Set base directory
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load configuration
config_path = os.path.join(base_dir, 'config', 'config.yaml')
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

# Setup logging
logging_config_path = os.path.join(base_dir, 'config', 'logging.yaml')
with open(logging_config_path, 'r') as file:
    logging_config = yaml.safe_load(file)
    logging.config.dictConfig(logging_config)

logger = logging.getLogger(__name__)
logger.info('Calcolatrice Scientifica avviata.')

class BasicOperations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


class AdvancedOperations:
    def exponential(self, a, b):
        return a ** b

    def logarithm(self, a, base):
        return math.log(a, base)

    def sine(self, angle):
        return math.sin(math.radians(angle))

    def cosine(self, angle):
        return math.cos(math.radians(angle))

    def tangent(self, angle):
        return math.tan(math.radians(angle))


def main():
    basic_ops = BasicOperations()
    advanced_ops = AdvancedOperations()

    # Test basic operations
    print("Addition: ", basic_ops.add(5, 3))
    print("Subtraction: ", basic_ops.subtract(5, 3))
    print("Multiplication: ", basic_ops.multiply(5, 3))
    try:
        print("Division: ", basic_ops.divide(5, 0))
    except ValueError as e:
        print(e)

    # Test advanced operations
    print("Exponential: ", advanced_ops.exponential(2, 3))
    print("Logarithm (base 10): ", advanced_ops.logarithm(100, 10))
    print("Sine (45 degrees): ", advanced_ops.sine(45))
    print("Cosine (45 degrees): ", advanced_ops.cosine(45))
    print("Tangent (45 degrees): ", advanced_ops.tangent(45))


if __name__ == "__main__":
    main()
