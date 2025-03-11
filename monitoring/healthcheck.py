import psutil
from prometheus_client import start_http_server, Gauge

class SystemMonitor:
    def __init__(self):
        self.cpu_usage = Gauge('cpu_usage', 'CPU utilization')
        self.memory_usage = Gauge('memory_usage', 'RAM usage')
        
    def run(self):
        while True:
            self.cpu_usage.set(psutil.cpu_percent())
            self.memory_usage.set(psutil.virtual_memory().percent)
