import pprint

import psutil
import platform


OS = platform.system()  # Display ex: Linux, Windows
RELEASE = platform.release()  # Display ex: 11
ARCH = platform.architecture()[0]  # Display ex: x64 or x86
PROCESSOR_NAME = platform.processor()  # Display ex: Intel64 Family 6 Model 183 Stepping 1
PYTHON_VERSION = platform.python_version()  # Display ex: 3.11.2

CORE_CPU = psutil.cpu_count(logical=False)  # Display only cpu core physical
CORE_THREADS = psutil.cpu_count(logical=True)  # Display with thread logical
CPU_FREQUENCY = psutil.cpu_freq()[0]  # Display CPU Frequency clock
CPU_USAGE = f'{psutil.cpu_percent()}%'  # Display CPU usage in %
DISK_USAGE = psutil.disk_usage('C:/' or '/')  # Display Free space in bytes, Usage space in byte and Free space in %
USER = psutil.users()[0][0]  # Display root user where application run
MEMORY_USAGE = f'{psutil.virtual_memory()[2]}%'  # Display Free Memory in %

print(CPU_USAGE)

