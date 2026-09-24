import os
import sys
import json
import psutil
import shutil
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import string
import ctypes
import subprocess

# --- KONFIGURATION UND LOGIK FÜR DIE SPRACHUNTERSTÜTZUNG ---

# Name der Konfigurationsdatei zur Speicherung der Spracheinstellungen
CONFIG_FILE = "config.json"

# Lokalisierungswörterbuch für alle unterstützten Sprachen
TRANSLATIONS = {
    "ru": {
        "title": "Системный монитор (Режим Админа)",
        "header": "Системный Монитор",
        "btn_theme": "Сменить тему",
        "btn_lang": "Сменить язык",
        "cpu_title": "Загрузка процессора",
        "cpu_loading": "Загрузка данных CPU...",
        "drive_name": "Диск",
        "folder_name": "Каталог",
        "analyzing": "Анализ...",
        "select_title": "Выбор языка",
        "select_label": "Выберите язык интерфейса:",
        "btn_confirm": "Подтвердить",
        "last_update": "Последнее обновление",
        "disk_text": "Использовано: {percent:.1f}% ({free:.1f} GB из {total:.1f} GB свободно)",
        "disk_error": "Ошибка анализа",
        "cpu_text": "Текущая загрузка: {percent}%"
    },
    "en": {
        "title": "System Monitor (Admin Mode)",
        "header": "System Monitor",
        "btn_theme": "Toggle Theme",
        "btn_lang": "Change Language",
        "cpu_title": "Processor Usage",
        "cpu_loading": "Loading CPU data...",
        "drive_name": "Drive",
        "folder_name": "Directory",
        "analyzing": "Analyzing...",
        "select_title": "Language Selection",
        "select_label": "Choose your language:",
        "btn_confirm": "Confirm",
        "last_update": "Last Update",
        "disk_text": "Used: {percent:.1f}% ({free:.1f} GB of {total:.1f} GB free)",
        "disk_error": "Analysis Error",
        "cpu_text": "Current Load: {percent}%"
    },
    "de": {
        "title": "System-Monitor (Admin-Modus)",
        "header": "System-Monitor",
        "btn_theme": "Theme wechseln",
        "btn_lang": "Sprache ändern",
        "cpu_title": "Prozessorauslastung",
        "cpu_loading": "Echte CPU-Daten werden geladen...",
        "drive_name": "Laufwerk",
        "folder_name": "Verzeichnis",
        "analyzing": "Analysiere...",
        "select_title": "Sprachauswahl",
        "select_label": "Wählen Sie eine Sprache:",
        "btn_confirm": "Bestätigen",
        "last_update": "Letzte Aktualisierung",
        "disk_text": "Genutzt: {percent:.1f}% ({free:.1f} GB von {total:.1f} GB frei)",
        "disk_error": "Fehler bei der Analyse",
        "cpu_text": "Aktuelle Auslastung: {percent}%"
    },
    "uk": {
        "title": "Системний монітор (Режим Адміна)",
        "header": "Системний Монітор",
        "btn_theme": "Змінити тему",
        "btn_lang": "Змінити мову",
        "cpu_title": "Завантаження процесора",
        "cpu_loading": "Завантаження даних CPU...",
        "drive_name": "Диск",
        "folder_name": "Каталог",
        "analyzing": "Аналіз...",
        "select_title": "Вибір мови",
        "select_label": "Оберіть мову інтерфейсу:",
        "btn_confirm": "Підтвердити",
        "last_update": "Останнє оновлення",
        "disk_text": "Використано: {percent:.1f}% ({free:.1f} GB з {total:.1f} GB вільно)",
        "disk_error": "Помилка аналізу",
        "cpu_text": "Поточне завантаження: {percent}%"
    }
}

def load_language():
    """
    Lädt die gespeicherte Sprache aus der Konfigurationsdatei.
    Gibt None zurück, wenn keine Datei existiert oder ein Fehler auftritt.
    """
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
                lang = config.get("language")
                if lang in TRANSLATIONS:
                    return lang
        except Exception:
            pass
    return None

def save_language(lang):
    """
    Speichert die ausgewählte Sprache in die Konfigurationsdatei.
    """
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"language": lang}, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def show_language_selection_dialog():
    """
    Zeigt ein grafisches Fenster zur Sprachauswahl beim ersten Start an.
    """
    selected_lang = {"code": "en"}
    
    dialog = tk.Tk()
    dialog.title("Language / Sprache")
    dialog.geometry("300x180")
    dialog.resizable(False, False)
    
    lbl = tk.Label(dialog, text="Select Language / Язык / Мову:", font=("Arial", 11, "bold"))
    lbl.pack(pady=10)
    
    lang_options = {
        "Русский": "ru",
        "English": "en",
        "Deutsch": "de",
        "Українська": "uk"
    }
    
    combo = ttk.Combobox(dialog, values=list(lang_options.keys()), state="readonly", font=("Arial", 10))
    combo.set("English")
    combo.pack(pady=10)
    
    def on_confirm():
        selected_lang["code"] = lang_options[combo.get()]
        dialog.destroy()
        
    btn = tk.Button(dialog, text="OK", command=on_confirm, width=10, font=("Arial", 10))
    btn.pack(pady=10)
    
    dialog.mainloop()
    return selected_lang["code"]

# --- UTILS UND SYSTEMLOGIK ---

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
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        os.execvp('sudo', ['sudo', sys.executable] + sys.argv)
    sys.exit()

def get_existing_drives():
    """Findet automatisch alle aktiven Festplatten/Partitionen im System."""
    drives = []
    if os.name == 'nt':
        for letter in string.ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                try:
                    shutil.disk_usage(drive)
                    drives.append(drive)
                except Exception:
                    continue
    else:
        drives = ['/']
        for mnt in ['/media', '/mnt']:
            if os.path.exists(mnt):
                for folder in os.listdir(mnt):
                    path = os.path.join(mnt, folder)
                    if os.path.islink(path) or os.path.ismount(path) or os.path.exists(path):
                        if path not in drives:
                            drives.append(path)
    return drives

# --- HAUPTANWENDUNG ---

class SystemMonitorApp:
    def __init__(self, root, current_lang):
        self.root = root
        self.current_lang = current_lang
        
        self.is_dark_theme = True
        self.themes = {
            "dark": {"bg": "#1e1e1e", "card": "#2d2d2d", "fg": "#ffffff", "muted": "#aaaaaa", "btn": "#4a4a4a", "btn_fg": "#ffffff"},
            "light": {"bg": "#f5f5f5", "card": "#ffffff", "fg": "#333333", "muted": "#666666", "btn": "#e0e0e0", "btn_fg": "#333333"}
        }
        
        self.labels = []
        self.frames = []
        
        self.root.configure(bg=self.themes["dark"]["bg"])
        
        # Header-Bereich erstellen
        self.header_frame = tk.Frame(root, bg=self.themes["dark"]["bg"])
        self.header_frame.pack(fill="x", padx=10, pady=5)
        
        self.lbl_title = tk.Label(self.header_frame, text="", font=("Arial", 16, "bold"), bg=self.themes["dark"]["bg"], fg=self.themes["dark"]["fg"])
        self.lbl_title.pack(side="left", padx=5)
        self.labels.append((self.lbl_title, "fg", "bg"))
        
        # Funktionstasten im Header platzieren
        self.btn_lang = tk.Button(self.header_frame, text="", command=self.change_language_runtime, font=("Arial", 9), relief="flat")
        self.btn_lang.pack(side="right", padx=5)
        
        self.btn_theme = tk.Button(self.header_frame, text="", command=self.toggle_theme, font=("Arial", 9), relief="flat")
        self.btn_theme.pack(side="right", padx=5)
        
        self.lbl_time = tk.Label(root, text="", font=("Arial", 10), bg=self.themes["dark"]["bg"], fg=self.themes["dark"]["muted"])
        self.lbl_time.pack(pady=2)
        self.labels.append((self.lbl_time, "muted", "bg"))
        
        # Scrollbares Canvas-System initialisieren
        self.canvas = tk.Canvas(root, bg=self.themes["dark"]["bg"], highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        
        self.scroll_frame = tk.Frame(self.canvas, bg=self.themes["dark"]["bg"])
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=10, pady=5)
        self.scrollbar.pack(side="right", fill="y")
        
        # CPU-Box generieren
        self.create_cpu_box()
        
        # Laufwerk-Boxen generieren
        self.active_drives = get_existing_drives()
        self.disk_elements = {}
        for drive in self.active_drives:
            self.create_disk_box(drive)
            
        # Dynamische Fenstergröße berechnen
        window_height = 200 + (len(self.active_drives) * 95)
        window_height = min(window_height, 600)
        self.root.geometry(f"520x{window_height}")
        
        # UI-Texte, Styles und Ressourcen-Updates initialisieren
        self.update_ui_texts()
        self.apply_theme_styles()
        self.update_resources()

        def create_cpu_box(self):
        """Erstellt die UI-Komponenten für die CPU-Überwachung."""
        t = self.themes["dark"]
        self.cpu_frame = tk.LabelFrame(self.scroll_frame, text="", font=("Arial", 11, "bold"), 
                                      bg=t["card"], fg=t["fg"], padx=15, pady=10, bd=1, relief="solid")
        self.cpu_frame.pack(fill="x", padx=10, pady=5, expand=True)
        self.frames.append(self.cpu_frame)
        
        self.lbl_cpu = tk.Label(self.cpu_frame, text="", font=("Arial", 11), bg=t["card"], fg=t["fg"])
        self.lbl_cpu.pack(anchor="w")
        self.labels.append((self.lbl_cpu, "custom_color", "card"))
        
        self.progress_cpu = ttk.Progressbar(self.cpu_frame, orient="horizontal", length=400, mode="determinate", style="Custom.Horizontal.TProgressbar")
        self.progress_cpu.pack(pady=5, fill="x")

    def create_disk_box(self, drive_path):
        """Erstellt ein separates LabelFrame für jedes erkannte Laufwerk."""
        t = self.themes["dark"]
        frame = tk.LabelFrame(self.scroll_frame, text="", font=("Arial", 11, "bold"), 
                             bg=t["card"], fg=t["fg"], padx=15, pady=10, bd=1, relief="solid")
        frame.pack(fill="x", padx=10, pady=5, expand=True)
        self.frames.append(frame)
        
        lbl_status = tk.Label(frame, text="", font=("Arial", 11), bg=t["card"], fg=t["fg"])
        lbl_status.pack(anchor="w")
        self.labels.append((lbl_status, "custom_color", "card"))
        
        progress = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate", style="Custom.Horizontal.TProgressbar")
        progress.pack(pady=5, fill="x")
        
        self.disk_elements[drive_path] = {
            "frame": frame,
            "label": lbl_status,
            "progress": progress
        }

    def update_ui_texts(self):
        """Aktualisiert alle statischen Texte in der Benutzeroberfläche bei Sprachwechsel."""
        lang_data = TRANSLATIONS[self.current_lang]
        
        self.root.title(lang_data["title"])
        self.lbl_title.configure(text=lang_data["header"])
        self.btn_theme.configure(text=lang_data["btn_theme"])
        self.btn_lang.configure(text=lang_data["btn_lang"])
        self.cpu_frame.configure(text=lang_data["cpu_title"])
        
        for drive_path, elements in self.disk_elements.items():
            prefix = lang_data["drive_name"] if os.name == 'nt' else lang_data["folder_name"]
            elements["frame"].configure(text=f"{prefix} {drive_path}")

    def change_language_runtime(self):
        """Erlaubt den Wechsel der Sprache während der Laufzeit per Knopfdruck."""
        lang_codes = list(TRANSLATIONS.keys())
        current_idx = lang_codes.index(self.current_lang)
        next_idx = (current_idx + 1) % len(lang_codes)
        
        self.current_lang = lang_codes[next_idx]
        save_language(self.current_lang)
        
        self.update_ui_texts()
        self.apply_theme_styles()

    def toggle_theme(self):
        """Schaltet zwischen hellem und dunklem Design um."""
        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme_styles()

    def apply_theme_styles(self):
        """Wendet die Farbthemen (Dark/Light) auf alle GUI-Elemente an."""
        theme_key = "dark" if self.is_dark_theme else "light"
        t = self.themes[theme_key]
        
        self.root.configure(bg=t["bg"])
        self.header_frame.configure(bg=t["bg"])
        self.canvas.configure(bg=t["bg"])
        self.scroll_frame.configure(bg=t["bg"])
        
        self.btn_theme.configure(bg=t["btn"], fg=t["btn_fg"], activebackground=t["muted"])
        self.btn_lang.configure(bg=t["btn"], fg=t["btn_fg"], activebackground=t["muted"])
        
        for lbl, fg_type, bg_type in self.labels:
            bg_color = t[bg_type]
            fg_color = t[fg_type] if fg_type != "custom_color" else lbl.cget("fg")
            lbl.configure(bg=bg_color, fg=fg_color)
            
        for frame in self.frames:
            frame.configure(bg=t["card"], fg=t["fg"])
            
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
        """Gibt je nach Auslastungsprozentsatz einen entsprechenden Farbcode zurück."""
        if percentage < 50:
            return "#2ecc71"  # Grün
        elif percentage < 70:
            return "#f1c40f"  # Gelb
        elif percentage < 85:
            return "#e67e22"  # Orange
        else:
            return "#e74c3c"  # Rot

    def update_resources(self):
        """Aktualisiert periodisch alle Systemressourcen und wendet Farbcodierung an."""
        theme_key = "dark" if self.is_dark_theme else "light"
        t = self.themes[theme_key]
        lang_data = TRANSLATIONS[self.current_lang]
        
        # Zeitanzeige aktualisieren
        time_str = datetime.now().strftime('%H:%M:%S')
        self.lbl_time.config(text=f"{lang_data['last_update']}: {time_str}")
        
        # Festplatten-Status aktualisieren
        for drive_path, elements in self.disk_elements.items():
            try:
                total, used, free = shutil.disk_usage(drive_path)
                used_percent = (used / total) * 100
                free_gb = free / (2**30)
                total_gb = total / (2**30)
                
                formatted_text = lang_data["disk_text"].format(
                    percent=used_percent, free=free_gb, total=total_gb
                )
                
                elements["label"].config(text=formatted_text, bg=t["card"])
                elements["progress"]['value'] = used_percent
                elements["label"].config(fg=self.get_color_code(used_percent))
            except Exception:
                elements["label"].config(text=lang_data["disk_error"], fg="#e74c3c", bg=t["card"])
                
        # CPU-Status aktualisieren (über psutil)
        cpu_percent = psutil.cpu_percent(interval=None)
        cpu_text_formatted = lang_data["cpu_text"].format(percent=cpu_percent)
        
        self.lbl_cpu.config(text=cpu_text_formatted, bg=t["card"])
        self.progress_cpu['value'] = cpu_percent
        self.lbl_cpu.config(fg=self.get_color_code(cpu_percent))
        
        # Endlosschleife für periodisches Update (alle 2 Sekunden)
        self.root.after(2000, self.update_resources)

# --- PROGRAMMSTART ---

if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
    else:
        # Sprache ermitteln oder GUI-Dialog beim ersten Start anzeigen
        lang = load_language()
        if not lang:
            lang = show_language_selection_dialog()
            save_language(lang)
            
        window = tk.Tk()
        app = SystemMonitorApp(window, lang)
        window.mainloop()
