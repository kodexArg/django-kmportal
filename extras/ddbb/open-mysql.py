#!/usr/bin/env python3

import os
import subprocess
from dotenv import load_dotenv
import time


# Load environment variables from .env file
load_dotenv('.env')

# Start the km1151 Docker Compose stack
subprocess.run(["docker", "compose", "-f", "extras/docker-compose.yaml", "up", "-d"], check=True)

time.sleep(1)

# Get the IP address of the km1151 container
result = subprocess.run(["docker", "inspect", "-f", "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}", "extras-km1151-1"], capture_output=True, text=True, check=True)
ip_address = result.stdout.strip()

# Connect to the MySQL server using the MySQL command-line client
mysql_command = f"mysql -h {ip_address} -u {os.environ['MYSQL_USER']} -p{os.environ['MYSQL_PASS']}"
subprocess.run(mysql_command, shell=True, check=True)

