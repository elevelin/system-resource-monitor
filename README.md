# 🖥️ System Resource Monitor (Python)

A lightweight Python tool to monitor CPU, memory, disk usage, and high-usage processes. Logs output to timestamped files and prints a clean snapshot of your system health.

---

## 🚀 Features

- 📊 Live stats: CPU %, memory, and disk usage
- 🔍 Top 5 CPU-consuming processes
- 📝 Logs output to `logs/` directory (rotated daily)
- ✅ Designed for macOS and Linux

---

## 📦 Setup

### 1. Clone the repo
```bash
git clone https://github.com/elevelin/system-resource-monitor.git
cd system-resource-monitor
```
2. Install required dependencies
```bash
pip3 install psutil
```
3. Run the monitor
```bash

python3 monitor.py
```
📁 Output Example

📅 2025-05-19 13:00:00

🧠 CPU Usage: 23.4%

💾 Memory Usage: 5.12 GB / 16.00 GB (32.0%)

🗃️ Disk Usage: 74.32 GB / 256.00 GB (29.0%)

🔥 Top 5 CPU Processes:

  PID  18432 | Chrome              | 15.2% CPU
  
  PID  15312 | Docker              | 12.7% CPU
...
🧠 Why Use This?


This tool is useful for:

System resource visibility

Lightweight local monitoring

Building automation scripts or cron jobs

Demonstrating Python + Linux CLI experience
