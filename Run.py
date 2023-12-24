#!/usr/bin/env python3
import platform, subprocess

if __name__ == '__main__':
    try:
        if platform.machine() == "aarch64":
            subprocess.call(["chmod", "+x", "aarch64"])
            subprocess.call(["./aarch64"])
        else:
            print(f"Perangkat {platform.machine()} bit, tidak dapat menjalankan aarch64!")
            exit()
    except (KeyboardInterrupt):
        exit()
    except (Exception) as e:
        print(f"[Error] {str(e).capitalize()}!")
        exit()
