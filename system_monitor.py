import os
import shutil
import sys
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random
import string

def get_existing_drives():
    """Findet automatisch alle aktiven Festplatten/Partitionen im System."""
    drives = []
    if os.name == 'nt':  # Für Windows
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                try:
                    shutil.disk_usage(drive)
                    drives.append(drive)
                except Exception:
                    continue
    else:  # Für Linux / macOS
        drives = ['/']
        for mnt in ['/media', '/mnt']:
            if os.path.exists(mnt):
                for folder in os.listdir(mnt):
                    path = os.path.join(mnt, folder)
                    if os.path.islink(path) or os.path.ismount(path) or os.path.exists(path):
                        drives.append(path)
    return drives

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Multi-Disk & CPU Monitor")
        self.root.configure(bg="#f5f5f5")
        
        # Titel
        lbl_title = tk.Label(root, text="System-Ressourcen-Monitor", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333333")
        lbl_title.pack(pady=10)

        # Zeitstempel
        self.lbl_time = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5", fg="#666666")
        self.lbl_time.pack(pady=2)

        # Scrollbarer Bereich
        self.canvas = tk.Canvas(root, bg="#f5f5f5", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scroll_frame = ttk.Frame(self.canvas)

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=10)
        self.scrollbar.pack(side="right", fill="y")

        # CPU Box erstellen
        self.create_cpu_box()

        # Alle aktiven Laufwerke ermitteln und Boxen erstellen
        self.active_drives = get_existing_drives()
        self.disk_elements = {}

        for drive in self.active_drives:
            self.create_disk_box(drive)

        # Fenstergröße dynamisch anpassen
        window_height = 180 + (len(self.active_drives) * 90)
        window_height = min(window_height, 600)  # Maximale Höhe begrenzen
        self.root.geometry(f"480x{window_height}")

        # Start der Echtzeit-Schleife
        self.update_resources()

    def create_cpu_box(self):
        frame = tk.LabelFrame(self.scroll_frame, text="Prozessorauslastung (CPU-Sim)", font=("Arial", 11, "bold"), padx=15, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        lbl_status = tk.Label(frame, text="Lade Daten...", font=("Arial", 11))
        lbl_status.pack(anchor="w")

        progress = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
        progress.pack(pady=5, fill="x")

        self.lbl_cpu = lbl_status
        self.progress_cpu = progress

    def create_disk_box(self, drive_path):
        display_name = f"Laufwerk {drive_path}" if os.name == 'nt' else f"Verzeichnis {drive_path}"
        frame = tk.LabelFrame(self.scroll_frame, text=display_name, font=("Arial", 11, "bold"), padx=15, pady=10)
        frame.pack(fill="x", padx=10, pady=5)

        lbl_status = tk.Label(frame, text="Analysiere...", font=("Arial", 11))
        lbl_status.pack(anchor="w")

        progress = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
        progress.pack(pady=5, fill="x")

        self.disk_elements[drive_path] = {
            "label": lbl_status,
            "progress": progress
        }

    def get_color_code(self, percentage):
        if percentage < 50:
            return "#2ecc71"  # Grün
        elif percentage < 70:
            return "#f1c40f"  # Gelb
        elif percentage < 85:
            return "#e67e22"  # Orange
        else:
            return "#e74c3c"  # Rot

    def update_resources(self):
        # 1. Zeit aktualisieren
        self.lbl_time.config(text=f"Letzte Aktualisierung: {datetime.now().strftime('%H:%M:%S')}")

        # 2. Alle Festplatten aktualisieren
        for drive_path, elements in self.disk_elements.items():
            try:
                total, used, free = shutil.disk_usage(drive_path)
                used_percent = (used / total) * 100
                free_gb = free / (2**30)
                total_gb = total / (2**30)

                elements["label"].config(
                    text=f"Genutzt: {used_percent:.1f}% ({free_gb:.1f} GB von {total_gb:.1f} GB frei)"
                )
                elements["progress"]['value'] = used_percent
                elements["label"].config(fg=self.get_color_code(used_percent))
            except Exception:
                elements["label"].config(text="Fehler bei der Analyse", fg="red")

        # 3. CPU-Simulation aktualisieren
        cpu_percent = random.randint(15, 95)
        self.lbl_cpu.config(text=f"Aktuelle Auslastung: {cpu_percent}%")
        self.progress_cpu['value'] = cpu_percent
        self.lbl_cpu.config(fg=self.get_color_code(cpu_percent))

        # Wiederholung alle 2 Sekunden
        self.root.after(2000, self.update_resources)

if __name__ == "__main__":
    window = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    app = SystemMonitorApp(window)
    window.mainloop()
