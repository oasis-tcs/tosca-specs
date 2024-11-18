import os
import subprocess
import unittest

class TestYAMLFiles(unittest.TestCase):

    def test_yaml_files(self):
        # # Directory to search for .yaml files
        directory = 'tosca_2_0/examples'

        # # Find all .yaml files in the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.yaml'):
                    # Run puccini command on each .yaml file and check the result is zero
                    print(f"Running puccini on {file} at {root}")
                    print
                    result = subprocess.run(['puccini-tosca', 'parse', os.path.join(root,file) ], capture_output=True)
                    print(result.stderr,"\n")
                    self.assertEqual(result.returncode, 0, f"puccini failed for {file}")

if __name__ == '__main__':
    unittest.main()
