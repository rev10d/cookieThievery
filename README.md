# cookieThievery

# Quick and dirty cookie stealer

# Pre-Req's:
# ubuntu / python3 supporting box / whatever

apt install python3-pip
python3 -m pip install flask

# I like to use httrack to clone a website.
apt install httrack

# Usage 

mkdir webclone
cd webclone

httrack https://defensiveorigins.com/login 

python3 -m http.server 8088

