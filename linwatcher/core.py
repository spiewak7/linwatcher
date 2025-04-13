import platform
import psutil
import socket
import shutil

def get_system_info():
    return {
        "OS": f"{platform.system()} {platform.release()}",
        "Kernel": platform.uname().release,
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "CPU": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "Disk": f"{shutil.disk_usage('/').total // (1024 ** 3)} GB"
    }
