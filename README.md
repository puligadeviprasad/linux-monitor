# Linux System Monitoring Dashboard

A production-grade Linux server monitoring tool built with Python, Bash, Prometheus and Grafana deployed on AWS EC2.

## Features
- Real-time CPU, memory, disk and network monitoring every 5 seconds
- Automated email alerts when metrics cross thresholds
- Grafana alerting with professional alert rules
- SQLite database storing complete metric history
- Log anomaly parser reducing review time by 70%
- Prometheus and Grafana industry standard stack
- Fully Dockerized for portable deployment
- Deployed on AWS EC2 with custom VPC and security groups
- Bash scripts with cron scheduling

## Tech Stack
- Python 3.12, Bash, psutil, SQLite
- Prometheus, Grafana, node_exporter
- Docker, AWS EC2, AWS VPC

## Project Structure
- monitor.py        - Main metrics collector
- alerts.py         - Email alert system
- database.py       - SQLite database logging
- log_parser.py     - Log anomaly scanner
- config.py         - Configuration settings
- Dockerfile        - Docker container setup
- requirements.txt  - Python dependencies
- scripts/check_disk.sh  - Disk usage checker
- scripts/check_net.sh   - Network tracker

## Installation

1. Clone the repository
git clone https://github.com/puligadeviprasad/linux-monitor.git
cd linux-monitor

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure email alerts in alerts.py
EMAIL_SENDER   = your@gmail.com
EMAIL_PASSWORD = your_app_password
EMAIL_RECEIVER = your@gmail.com

5. Run the monitor
python3 monitor.py

## Prometheus and Grafana Setup

1. Start node_exporter
node_exporter &

2. Start Prometheus
prometheus --config.file=/etc/prometheus/prometheus.yml &

3. Start Grafana
sudo /usr/sbin/grafana-server --config=/etc/grafana/grafana.ini --homepath=/usr/share/grafana &

4. Open Grafana at http://localhost:3000
Username: admin
Password: admin

5. Import dashboard ID 1860

## Docker Deployment
docker build -t linux-monitor .
docker run -d --name monitor-app linux-monitor
docker logs -f monitor-app

## AWS EC2 Deployment

1. Launch t2.micro Ubuntu instance
2. Open ports 22, 3000, 9090, 9100
3. Copy project to EC2
scp -i monitor-key.pem -r ~/linux-monitor ubuntu@EC2_IP:~/

4. SSH into EC2
ssh -i monitor-key.pem ubuntu@EC2_IP

5. Access Grafana at http://EC2_IP:3000

## Alert Thresholds
- CPU    greater than 80 percent - Email alert sent
- Memory greater than 75 percent - Email alert sent
- Disk   greater than 85 percent - Email alert sent

## Log Anomaly Detection
Automatically scans for:
- Authentication failures
- Out of memory errors
- Disk I/O errors
- System crashes and segfaults

Run with: sudo python3 log_parser.py

## Quick Start
bash ~/start-monitor.sh

## Daily Workflow
Start  - bash ~/start-monitor.sh
Open   - http://localhost:3000
Stop   - bash ~/stop-monitor.sh

## Author
Devi Prasad Puliga
GitHub: https://github.com/puligadeviprasad
Email: puligadeviprasad@gmail.com

## License
MIT License - feel free to use this project!

If you find this project useful please give it a star on GitHub!
