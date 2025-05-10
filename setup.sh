apt install -y python3-dev
apt install -y python3-picamera2 --no-install-recommends
apt install -y python3-picamera2 --no-install-recommends

python3 -m venv .venv
source .venv/bin/activate

pip3 install --upgrade pip
pip3 install --no-cache-dir -r requirements.txt
