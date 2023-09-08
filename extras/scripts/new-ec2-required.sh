# Update package lists
sudo apt update

# Install Python3, Pip3
sudo apt install python3 python3-pip

# Install Git
sudo apt install git

# Install Gunicorn
pip3 install gunicorn

# Install Tmux
sudo apt install tmux

# Install Fuser, required for github actions (and that's about all I know)
sudo apt install psmisc

# pip mysql connector will fail without this:
sudo apt install libmysqlclient-dev
