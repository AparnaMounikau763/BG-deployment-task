EC2 one-time setup:

sudo apt update
sudo apt install docker.io nginx -y
sudo systemctl enable docker nginx
sudo systemctl start docker nginx
sudo usermod -aG docker ubuntu

sudo mkdir -p /opt/deploy
echo blue | sudo tee /opt/deploy/active_env

Copy nginx.conf to:
  /etc/nginx/sites-available/default

sudo nginx -t
sudo systemctl reload nginx

GitHub Secrets:
DOCKER_USERNAME
DOCKER_PASSWORD
EC2_HOST
EC2_USERNAME
EC2_SSH_KEY
