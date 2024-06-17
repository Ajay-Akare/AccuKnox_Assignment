import logging
import time
import psutil


def log_message(message):
    # Configure logging
    logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')
    logging.info(message)


def print_alert(message):
    print(f"ALERT: {message}")


def display_usage(cpu_usage, mem_usage, disk_usage, bars=10):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    if cpu_usage > 50.00:
        message = f"High cpu usage detected: {cpu_usage}%"
        log_message(message)
        print_alert(message)

    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    if mem_usage > 50.00:
        message = f"High Memory usage detected: {mem_usage}%"
        log_message(message)
        print_alert(message)

    disk_usage = (disk_usage / 100.0)
    disk_bar = '█' * int(disk_usage * bars) + '-' * (bars - int(disk_usage * bars))
    if disk_usage > 50.00:
        message = f"High Disk usage detected: {disk_usage}%"
        log_message(message)
        print_alert(message)

    print(f" CPU Usage: | |{cpu_bar}| {cpu_usage:.2f}%", end="\n")
    print(f" Mem Usage: | |{mem_bar}| {mem_usage:.2f}%", end="\n")
    print(f" disk Usage: | |{disk_bar}| {disk_usage:.2f}%", end="\n")


while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage('/').percent)
    time.sleep(10)
