import sys
import subprocess

print("Platform is:", sys.platform)
print("Python version is:", sys.version_info)


cp = subprocess.run(['ls','-l'],
                            capture_output=True,
                            universal_newlines=True)
print(cp.stdout)

