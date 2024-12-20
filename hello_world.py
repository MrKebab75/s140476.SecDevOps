print("hello world")

# Kwetsbare code
SECRET_KEY = "12345"  # Hardcoded secret
import subprocess
subprocess.run("rm -rf /", shell=True)  # Onveilig gebruik van subprocess
