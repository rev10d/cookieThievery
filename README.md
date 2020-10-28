# cookieThievery

## Quick and dirty cookie stealer

## Pre-Req's:
### ubuntu / python3 supporting box / whatever

apt install python3-pip <br / >
python3 -m pip install flask <br />

## I like to use httrack to clone a website.
apt install httrack <br />

## Usage 

mkdir webclone <br /> 
cd webclone <br /> <br />

httrack https://defensiveorigins.com/login <br /><br />

python3 -m http.server 8088 <br /><br />

