import os
import unittest
import subprocess

def generate_test_classes():
    directory = 'tosca_2_0/examples'
    test_classes = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                class_name = f"Test_{file.replace('.', '_')}"
                def test_method(self, file=file, root=root):
                    result = subprocess.run(['puccini-tosca', 'parse', os.path.join(root, file)], capture_output=True)
                    self.assertEqual(result.returncode, 0, f"puccini failed for {file}\n{result.stderr.decode()}")
                test_classes[class_name] = type(class_name, (unittest.TestCase,), {
                    'test_yaml_file': test_method
                })

    return test_classes

# Generate test classes and add them to the current module
test_classes = generate_test_classes()
globals().update(test_classes)

if __name__ == '__main__':
    unittest.main()