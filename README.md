# System-Ressourcen-Monitor

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>

---

## 🇩🇪 Deutsch

Ein leichtgewichtiger, plattformunabhängiger System-Monitor mit grafischer Benutzeroberfläche zur Echtzeit-Überwachung von Speicherplatz und realer CPU-Auslastung.

### 🌟 Hauptmerkmale
* **Echte CPU-Überwachung**: Nutzt die `psutil`-Bibliothek zur präzisen Erfassung der tatsächlichen Prozessorlast in Echtzeit (keine Simulation).
* **Automatisierter Admin-Modus**: Prüft beim Start die Benutzerrechte und fordert unter Windows (UAC) oder Linux/macOS (Sudo) automatisch Administratorrechte an.
* **Dynamischer Theme-Wechsel**: Ermöglicht das Umschalten zwischen einem modernen Dark-Mode und einem klassischen Light-Mode per Knopfdruck zur Laufzeit.
* **Automatisierte Laufwerkserkennung**: Identifiziert selbstständig das Betriebssystem und ermittelt den freien sowie belegten Speicherplatz aller aktiven Partitionen (in GB und Prozent).
* **Visuelles Warnsystem**: Intelligente Farbcodierung (Grün, Gelb, Orange, Rot), die sich dem aktuellen Auslastungs- und Kritikalitätsstatus der Ressourcen anpasst.
* **Live-Aktualisierung**: Vollautomatische Daten-Resynchronisation im festen Intervall von 1000 Millisekunden (1 Sekunde) für präzise CPU-Werte.

### 🛠️ Technologien & Bibliotheken
* **Laufzeitumgebung**: Python 3.x
* **Standard-Module**: `os`, `shutil`, `sys`, `datetime`, `string`, `ctypes`
* **Externe Abhängigkeiten**: `psutil` (wird bei Fehlen automatisch im globalen Kontext installiert)
* **GUI-Framework**: `tkinter` & `ttk`

### 📂 Aufbau der Benutzeroberfläche
Die Anwendung ist modular in drei wesentliche Segmente unterteilt:
1. **Kopfzeile & Steuerung**: Enthält den Titel, den Button zum Wechseln des Themes sowie die exakte Uhrzeit der letzten Datenabfrage.
2. **Prozessor-Panel**: Visualisiert die reale CPU-Auslastung mittels eines farbcodierten Fortschrittsbalkens.
3. **Speicherplatz-Panel**: Zeigt den Status aller aktiven Partitionen (`C:\`, `D:\` etc. für Windows oder `/` für Unix/Linux) über scrollbare Fortschrittsbalken an.

### 📦 Schnellstart-Anleitung
Führen Sie die folgenden Befehle in Ihrem Terminal aus, um das Projekt zu starten:

```bash
# 1. Repository herunterladen
git clone https://github.com/KristinaAlokhina/system_monitor

# 2. In das Projektverzeichnis wechseln
cd system_monitor

# 3. Anwendung starten (fordert Admin-Rechte an)
python system_monitor.py
```

---

## 🇺🇸 English

A lightweight, cross-platform system monitor featuring a graphical user interface for real-time tracking of real CPU load and disk space allocation.

### 🚀 Key Features
* **Real CPU Monitoring**: Utilizes the `psutil` library to accurately capture and display actual hardware processor capacity (no more simulation).
* **Automated Admin Elevation**: Automatically detects user privileges and requests UAC elevation (Windows) or Sudo access (Linux/macOS) upon startup.
* **On-the-Fly Theme Toggle**: Seamlessly switches between a sleek Dark Theme and a clean Light Theme instantly at the click of a button.
* **Automated Drive Detection**: Automatically maps host storage partitions, calculating available vs. used space in Gigabytes and percentages.
* **Smart Alert System**: Adaptive color coding (Green, Yellow, Orange, Red) that shifts dynamically based on current resource critical levels.
* **Instant Refresh**: High-frequency data polling and interface synchronization every 1000 milliseconds (1 second) for precise metric trailing.

### 🛠️ Tech Stack
* **Runtime**: Python 3.x
* **Built-in Modules**: `os`, `shutil`, `sys`, `datetime`, `string`, `ctypes`
* **External Dependencies**: `psutil` (automatically installed globally if missing)
* **GUI Library**: `tkinter` & `ttk`

### 📂 Layout Structure
The interface layout consists of three primary functional zones:
1. **Header & Theme Controller**: Hosts the application title, the theme toggle button, and the exact timestamp of the last data polling event.
2. **Processor Load Box**: Monitors and visualizes the active, real-time processor utilization.
3. **Storage Allocation Box**: Renders vertical, scrollable progress bars and text metrics for all active mounted system drives (`C:\`, `D:\` on Windows or `/` on Unix/Linux).

### 📦 Installation & Setup
Run the following commands in your terminal to deploy and launch the script:

```bash
# 1. Clone the repository
git clone https://github.com/KristinaAlokhina/system_monitor

# 2. Navigate to the project directory
cd system_monitor

# 3. Run the application (triggers admin UAC prompt)
python system_monitor.py
```
