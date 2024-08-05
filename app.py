from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import threading
import time
import requests
from pythonping import ping

app = Flask(__name__)
socketio = SocketIO(app)

hosts = []

def ping_host(host):
    try:
        response = ping(host, count=5, timeout=2)  # Sending 5 packets
        packets_sent = 5  # Total packets sent
        packets_received = sum(1 for r in response if r.success)  # Total packets received

        if packets_received > 0:
            packet_loss = ((packets_sent - packets_received) / packets_sent) * 100  # Calculate packet loss percentage
            avg_rtt = sum(r.time_elapsed_ms for r in response if r.success) / packets_received  # Calculate average RTT
            return 'up', avg_rtt, packet_loss
        else:
            return 'down', None, 100  # 100% packet loss if ping fails
    except Exception as e:
        print(f"Error pinging host {host}: {e}")
        return 'down', None, 100

def monitor_hosts():
    while True:
        for host in hosts:
            status, rtt, packet_loss = ping_host(host['address'])
            host['status'] = status
            host['rtt'] = rtt
            host['packet_loss'] = packet_loss
            socketio.emit('update_host', host)
        time.sleep(5)  # Ping every 5 seconds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_host', methods=['POST'])
def add_host():
    address = request.form['address']
    host = {'address': address, 'status': 'unknown', 'rtt': None, 'packet_loss': None}
    hosts.append(host)
    return jsonify(host)

@app.route('/remove_host', methods=['POST'])
def remove_host():
    address = request.form['address']
    global hosts
    hosts = [host for host in hosts if host['address'] != address]
    return jsonify({'status': 'success'})

@app.route('/get_ip_info')
def get_ip_info():
    ip_info = requests.get("https://ipinfo.io/json?token=YOUR_TOKEN_HERE").json()
    return jsonify(ip_info)

@app.route('/get_ipv6_info')
def get_ipv6_info():
    ipv6_info = requests.get("https://api64.ipify.org?format=json").json()
    return jsonify(ipv6_info)

if __name__ == '__main__':
    threading.Thread(target=monitor_hosts).start()
    socketio.run(app, debug=True)
