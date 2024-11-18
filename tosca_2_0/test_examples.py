import os
import subprocess
import unittest

def generate_test_classes():
    directory = 'tosca_2_0/examples'
    test_classes = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml'):
                class_name = f"Test_{file.replace('.', '_')}"
                test_classes[class_name] = type(class_name, (unittest.TestCase,), {
                    'test_yaml_file': lambda self, file=file, root=root: self.assertEqual(
                        subprocess.run(['puccini-tosca', 'parse', os.path.join(root, file)], capture_output=True).returncode,
                        0,
                        f"puccini failed for {file}"
                    )
                })

    return test_classes

globals().update(generate_test_classes())

if __name__ == '__main__':
    unittest.main()