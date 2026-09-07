import os
import sys
import shutil
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import string
import ctypes

# Versuchen, psutil zu importieren (notwendig für echte CPU-Daten)
try:
    import psutil
except ImportError:
    # Automatische Installation, falls psutil fehlt
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

def is_admin():
    """Überprüft, ob das Skript mit Administratorrechten ausgeführt wird."""
    try:
        if os.name == 'nt':
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
            return os.getuid() == 0
    except Exception:
        return False

def run_as_admin():
    """Startet das Skript automatisch mit Administratorrechten neu."""
    if os.name == 'nt':
        # Windows: UAC-Anforderungsdialog anzeigen
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        # Linux/macOS: Mit sudo neu starten
        os.execvp('sudo', ['sudo', sys.executable] + sys.argv)
    sys.exit()

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
                        if path not in drives:
                            drives.append(path)
    return drives

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Multi-Disk & CPU Monitor (Admin Mode)")
        
        # Theme-Status (True = Dark, False = Light)
        self.is_dark_theme = True
        
        # Farbpaletten für beide Themes definieren
        self.themes = {
            "dark": {"bg": "#1e1e1e", "card": "#2d2d2d", "fg": "#ffffff", "muted": "#aaaaaa", "btn": "#4a4a4a", "btn_fg": "#ffffff"},
            "light": {"bg": "#f5f5f5", "card": "#ffffff", "fg": "#333333", "muted": "#666666", "btn": "#e0e0e0", "btn_fg": "#333333"}
        }
        
        # Listen für Widgets zur dynamischen Farbänderung
        self.labels = []
        self.frames = []
        
        # Hauptfenster konfigurieren
        self.root.configure(bg=self.themes["dark"]["bg"])
        
        # Header-Bereich für Titel und Theme-Button
        self.header_frame = tk.Frame(root, bg=self.themes["dark"]["bg"])
        self.header_frame.pack(fill="x", padx=10, pady=5)
        
        # Titelzeile / Titel
        self.lbl_title = tk.Label(self.header_frame, text="System-Monitor", font=("Arial", 16, "bold"), bg=self.themes["dark"]["bg"], fg=self.themes["dark"]["fg"])
        self.lbl_title.pack(side="left", padx=5)
        self.labels.append((self.lbl_title, "fg", "bg"))
        
        # Button zum Wechseln des Themes
        self.btn_theme = tk.Button(self.header_frame, text="Theme wechseln", command=self.toggle_theme, font=("Arial", 9), relief="flat")
        self.btn_theme.pack(side="right", padx=5)
        
        # Zeitstempel der letzten Aktualisierung / Zeitstempel
        self.lbl_time = tk.Label(root, text="", font=("Arial", 10), bg=self.themes["dark"]["bg"], fg=self.themes["dark"]["muted"])
        self.lbl_time.pack(pady=2)
        self.labels.append((self.lbl_time, "muted", "bg"))
        
        # Scrollbarer Bereich Setup
        self.canvas = tk.Canvas(root, bg=self.themes["dark"]["bg"], highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        
        self.scroll_frame = tk.Frame(self.canvas, bg=self.themes["dark"]["bg"])
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Packen von Canvas und Scrollbar
        self.canvas.pack(side="left", fill="both", expand=True, padx=10, pady=5)
        self.scrollbar.pack(side="right", fill="y")
        
        # CPU Box erstellen
        self.create_cpu_box()
        
        # Alle aktiven Laufwerke ermitteln und Boxen erstellen
        self.active_drives = get_existing_drives()
        self.disk_elements = {}
        for drive in self.active_drives:
            self.create_disk_box(drive)
            
        # Fenstergröße dynamisch anpassen
        window_height = 200 + (len(self.active_drives) * 95)
        window_height = min(window_height, 600)  # Maximale Höhe begrenzen
        self.root.geometry(f"480x{window_height}")
        
        # Initiales Theme-Styling anwenden
        self.apply_theme_styles()
        
        # Start der Echtzeit-Schleife
        self.update_resources()

    def create_cpu_box(self):
        """Erstellt die Box für die echte CPU-Auslastung"""
        t = self.themes["dark"]
        frame = tk.LabelFrame(self.scroll_frame, text="Prozessorauslastung (Echte CPU)", font=("Arial", 11, "bold"), 
                             bg=t["card"], fg=t["fg"], padx=15, pady=10, bd=1, relief="solid")
        frame.pack(fill="x", padx=10, pady=5, expand=True)
        self.frames.append(frame)
        
        # Textueller Ladestatus
        self.lbl_cpu = tk.Label(frame, text="Echte CPU-Daten werden geladen...", font=("Arial", 11), bg=t["card"], fg=t["fg"])
        self.lbl_cpu.pack(anchor="w")
        self.labels.append((self.lbl_cpu, "fg", "card"))
        
        # Fortschrittsbalken
        self.progress_cpu = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate", style="Custom.Horizontal.TProgressbar")
        self.progress_cpu.pack(pady=5, fill="x")

    def create_disk_box(self, drive_path):
        """Erstellt eine Box für ein spezifisches Laufwerk"""
        t = self.themes["dark"]
        display_name = f"Laufwerk {drive_path}" if os.name == 'nt' else f"Verzeichnis {drive_path}"
        frame = tk.LabelFrame(self.scroll_frame, text=display_name, font=("Arial", 11, "bold"), 
                             bg=t["card"], fg=t["fg"], padx=15, pady=10, bd=1, relief="solid")
        frame.pack(fill="x", padx=10, pady=5, expand=True)
        self.frames.append(frame)
        
        lbl_status = tk.Label(frame, text="Analysiere...", font=("Arial", 11), bg=t["card"], fg=t["fg"])
        lbl_status.pack(anchor="w")
        self.labels.append((lbl_status, "custom_color", "card"))
        
        # Fortschrittsbalken (Progress Bar)
        progress = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate", style="Custom.Horizontal.TProgressbar")
        progress.pack(pady=5, fill="x")
        
        self.disk_elements[drive_path] = {
            "label": lbl_status,
            "progress": progress
        }

    def toggle_theme(self):
        """Schaltet zwischen hellem und dunklem Theme um"""
        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme_styles()

    def apply_theme_styles(self):
        """Wendet die Farben des aktuellen Themes auf alle Widgets an"""
        theme_key = "dark" if self.is_dark_theme else "light"
        t = self.themes[theme_key]
        
        # Hauptkomponenten färben
        self.root.configure(bg=t["bg"])
        self.header_frame.configure(bg=t["bg"])
        self.canvas.configure(bg=t["bg"])
        self.scroll_frame.configure(bg=t["bg"])
        
        # Button stylen
        self.btn_theme.configure(bg=t["btn"], fg=t["btn_fg"], activebackground=t["muted"])
        
        # Alle registrierten Labels aktualisieren
        for lbl, fg_type, bg_type in self.labels:
            bg_color = t[bg_type]
            fg_color = t[fg_type] if fg_type != "custom_color" else lbl.cget("fg")
            lbl.configure(bg=bg_color, fg=fg_color)
            
        # Alle Registrierten Frames aktualisieren
        for frame in self.frames:
            frame.configure(bg=t["card"], fg=t["fg"])
            
        # TTK Progressbar & Scrollbar Style anpassen
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Custom.Horizontal.TProgressbar", 
                        troughcolor=t["bg"], 
                        background="#4a4a4a" if self.is_dark_theme else "#0078d7", 
                        bordercolor=t["card"], 
                        lightcolor="#4a4a4a" if self.is_dark_theme else "#0078d7", 
                        darkcolor="#4a4a4a" if self.is_dark_theme else "#0078d7")
        
        style.configure("Vertical.TScrollbar", 
                        troughcolor=t["bg"], 
                        background=t["btn"], 
                        bordercolor=t["card"], 
                        arrowcolor=t["fg"])

    def get_color_code(self, percentage):
        """Gibt den Farbcode basierend auf dem Auslastungsprozentsatz zurück"""
        if percentage < 50:
            return "#2ecc71"  # Grün
        elif percentage < 70:
            return "#f1c40f"  # Gelb
        elif percentage < 85:
            return "#e67e22"  # Orange
        else:
            return "#e74c3c"  # Rot

    def update_resources(self):
        """Hauptmethode zur Aktualisierung der Daten auf dem Bildschirm"""
        theme_key = "dark" if self.is_dark_theme else "light"
        t = self.themes[theme_key]
        
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
                    text=f"Genutzt: {used_percent:.1f}% ({free_gb:.1f} GB von {total_gb:.1f} GB frei)",
                    bg=t["card"]
                )
                elements["progress"]['value'] = used_percent
                elements["label"].config(fg=self.get_color_code(used_percent))
            except Exception:
                elements["label"].config(text="Fehler bei der Analyse", fg="#e74c3c", bg=t["card"])
                
        # 3. Echte CPU-Auslastung aktualisieren
        cpu_percent = psutil.cpu_percent(interval=None)
        self.lbl_cpu.config(text=f"Aktuelle Auslastung: {cpu_percent}%", bg=t["card"])
        self.progress_cpu['value'] = cpu_percent
        self.lbl_cpu.config(fg=self.get_color_code(cpu_percent))
        
        # Wiederholung alle 1 Sekunde (1000 Millisekunden)
        self.root.after(1000, self.update_resources)

if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
        
    window = tk.Tk()
    app = SystemMonitorApp(window)
