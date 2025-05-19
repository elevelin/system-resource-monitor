import datetime
import os
import psutil
import shutil 

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.used / (1024**3), mem.total / (1024**3), mem.percent

def get_disk_usage():
    disk = shutil.disk_usage("/")
    percent = (disk.used / disk.total) * 100
    return disk.used / (1024**3), disk.total / (1024**3), percent

def get_top_processes(n=5):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            info = proc.info
            if info['cpu_percent'] is not None:
                processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    top = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:n]
    return top

def log_output(output):
    os.makedirs("logs", exist_ok=True)
    filename = f"logs/monitor-{datetime.date.today()}.log"
    with open(filename, "a") as f:
        f.write(output + "\n")

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = get_cpu_usage()
    mem_used, mem_total, mem_pct = get_memory_usage()
    disk_used, disk_total, disk_pct = get_disk_usage()
    top_procs = get_top_processes()

    output = (
        f"📅 {now}\n"
        f"🧠 CPU Usage: {cpu}%\n"
        f"💾 Memory Usage: {mem_used:.2f} GB / {mem_total:.2f} GB ({mem_pct}%)\n"
        f"🗃️ Disk Usage: {disk_used:.2f} GB / {disk_total:.2f} GB ({disk_pct}%)\n"
        f"🔥 Top {len(top_procs)} CPU Processes:\n"
    )
    for proc in top_procs:
        output += f"  PID {proc['pid']:>5} | {proc['name'][:20]:<20} | {proc['cpu_percent']:>5}% CPU\n"

    print(output)
    log_output(output)


if __name__ == "__main__":
    main()

