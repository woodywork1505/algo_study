import os
import psutil

def get_drive_info(drive_path='C:\\'):
    usage = psutil.disk_usage(drive_path)
    
    info = {
        "Drive": drive_path,
        "Total Space (GB)": usage.total / (1024**3),
        "Used Space (GB)": usage.used / (1024**3),
        "Free Space (GB)": usage.free / (1024**3),
        "Usage Percentage": usage.percent
    }
    
    return info

def get_system_info():
    virtual_memory = psutil.virtual_memory()
    
    info = {
        "CPU Cores (logical)": psutil.cpu_count(logical=True),
        "CPU Cores (physical)": psutil.cpu_count(logical=False),
        "Total RAM (GB)": virtual_memory.total / (1024**3),
        "Used RAM (GB)": virtual_memory.used / (1024**3),
        "Free RAM (GB)": virtual_memory.available / (1024**3),
        "RAM Usage Percentage": virtual_memory.percent
    }
    
    return info

def print_info(title, info_dict):
    print(title)
    for key, value in info_dict.items():
        if isinstance(value, (int, float)):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    drive_info = get_drive_info()
    system_info = get_system_info()

    print_info("Drive Information:", drive_info)
    print("\n")
    print_info("System Information:", system_info) 