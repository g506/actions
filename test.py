import subprocess
import shlex
import pytest
import unittest

class SimpleTest(unittest.TestCase):
    def test_sh(self):
        sh_output = subprocess.call(shlex.split('./entrypoint.sh World'))
        print(sh_output)
        or_output = 0
        message = "Test Failed"
        self.assertEqual(sh_output, or_output, message)

if __name__ == '__main__':
    unittest.main()
