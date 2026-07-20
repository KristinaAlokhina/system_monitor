import os
import shutil
import sys
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System-Ressourcen-Monitor")
        self.root.geometry("450x400")
        self.root.configure(bg="#f5f5f5")
        
        # Titelzeile
        lbl_title = tk.Label(root, text="System-Ressourcen-Monitor", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333333")
        lbl_title.pack(pady=10)

        # Zeitstempel der letzten Aktualisierung
        self.lbl_time = tk.Label(root, text="", font=("Arial", 10), bg="#f5f5f5", fg="#666666")
        self.lbl_time.pack(pady=2)

        # Container für den Festplattenspeicher
        self.create_resource_box("Festplattenspeicher (HDD/SSD)", "disk")

        # Container für die CPU-Simulation
        self.create_resource_box("Prozessorauslastung (CPU-Sim)", "cpu")

        # Start der kontinuierlichen Aktualisierung (alle 2000 ms / 2 Sekunden)
        self.update_resources()

    def create_resource_box(self, title, ref):
        """Erstellt eine Box zur Anzeige einer Ressource (Text + Fortschrittsbalken)"""
        frame = tk.LabelFrame(self.root, text=title, font=("Arial", 11, "bold"), bg="#f5f5f5", padx=15, pady=10)
        frame.pack(fill="x", padx=20, pady=10)

        # Textueller Ladestatus
        lbl_status = tk.Label(frame, text="Daten werden geladen...", font=("Arial", 11), bg="#f5f5f5")
        lbl_status.pack(anchor="w")

        # Fortschrittsbalken (Progress Bar)
        progress = ttk.Progressbar(frame, orient="horizontal", length=350, mode="determinate")
        progress.pack(pady=5, fill="x")

        # Speichern der Referenzen für die dynamische Aktualisierung
        if ref == "disk":
            self.lbl_disk = lbl_status
            self.progress_disk = progress
        elif ref == "cpu":
            self.lbl_cpu = lbl_status
            self.progress_cpu = progress

    def get_color_code(self, percentage):
        """Gibt den Farbcode basierend auf dem Auslastungsprozentsatz zurück"""
        if percentage < 50:
            return "#2ecc71"  # Grün: Alles OK
        elif percentage < 70:
            return "#f1c40f"  # Gelb: Leicht ausgelastet
        elif percentage < 85:
            return "#e67e22"  # Orange: Hohe Auslastung
        else:
            return "#e74c3c"  # Rot: Kritischer Bereich

    def update_resources(self):
        """Hauptmethode zur Aktualisierung der Daten auf dem Bildschirm"""
        # 1. Aktualisierung der Uhrzeit
        self.lbl_time.config(text=f"Letzte Aktualisierung: {datetime.now().strftime('%H:%M:%S')}")

        # 2. Berechnung der Festplattendaten
        root_path = "C:\\" if os.name == 'nt' else '/'
        try:
            total, used, free = shutil.disk_usage(root_path)
            used_percent = (used / total) * 100
            free_gb = free / (2**30)
            total_gb = total / (2**30)

            self.lbl_disk.config(
                text=f"Belegt: {used_percent:.1f}% ({free_gb:.1f} GB von {total_gb:.1f} GB frei)"
            )
            self.progress_disk['value'] = used_percent

            # Textfarbe basierend auf der Kritikalität der Festplattenbelegung ändern
            self.lbl_disk.config(fg=self.get_color_code(used_percent))
        except Exception:
            self.lbl_disk.config(text="Fehler bei der Festplattenanalyse", fg="red")

        # 3. Simulation der CPU-Dynamik (Zufallszahlen von 15% bis 95%)
        cpu_percent = random.randint(15, 95)

        self.lbl_cpu.config(text=f"Aktuelle Auslastung: {cpu_percent}%")
        self.progress_cpu['value'] = cpu_percent
        self.lbl_cpu.config(fg=self.get_color_code(cpu_percent))

        # Endlosschleife zur Aktualisierung alle 2 Sekunden (2000 Millisekunden)
        self.root.after(2000, self.update_resources)

if __name__ == "__main__":
    window = tk.Tk()
    
    # Stileinstellungen für die Fortschrittsbalken
    style = ttk.Style()
    style.theme_use('clam')
    
    app = SystemMonitorApp(window)
    window.mainloop()
