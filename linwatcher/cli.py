from linwatcher.core import get_system_info

def display_system_info():
    info = get_system_info()
    print("=" * 40)
    print("🖥️  LinWatcher — System Overview")
    print("=" * 40)
    for key, value in info.items():
        print(f"{key:15}: {value}")
    print("=" * 40)
