# System-Ressourcen-Monitor

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>

---

## 🇩🇪 Deutsch

Ein leichtgewichtiger, plattformunabhängiger System-Monitor mit grafischer Benutzeroberfläche zur Echtzeit-Überwachung von Speicherplatz und CPU-Auslastung.

### 🌟 Hauptmerkmale
* **Automatisierte Laufwerkserkennung**: Identifiziert selbstständig das zugrundeliegende Betriebssystem und ermittelt den freien sowie belegten Speicherplatz (in GB und Prozent).
* **Interaktive Prozessor-Simulation**: Veranschaulicht kontinuierliche UI-Aktualisierungen durch eine dynamische, zeitgesteuerte Simulation der CPU-Last.
* **Visuelles Warnsystem**: Intelligente Farbcodierung (Grün, Gelb, Orange, Rot), die sich dem aktuellen Auslastungs- und Kritikalitätsstatus der Ressourcen anpasst.
* **Live-Aktualisierung**: Vollautomatische Daten-Resynchronisation im festen Intervall von 2000 Millisekunden (2 Sekunden).
* **Plattformübergreifendes Design**: Nutzung des integrierten `clam`-Themes von Tkinter für eine saubere und konsistente Darstellung von Fortschrittsbalken auf allen OS-Systemen.

### 🛠️ Technologien & Bibliotheken
* **Laufzeitumgebung**: Python 3.x
* **Standard-Module**: `os`, `shutil`, `sys`, `datetime`, `random`, `string`
* **GUI-Framework**: `tkinter` (keine externen Abhängigkeiten erforderlich)

### 📂 Aufbau der Benutzeroberfläche
Die Anwendung ist modular in drei wesentliche Segmente unterteilt:
1. **Kopfzeile & Zeitstempel**: Zeigt den Status sowie die exakte Uhrzeit der letzten Datenabfrage an.
2. **Speicherplatz-Panel**: Visualisiert den Status aller aktiven Partitionen (`C:\`, `D:\` für Windows oder `/` für Unix/Linux) via Progress-Bar.
3. **Prozessor-Panel**: Zeigt die simulierte CPU-Auslastung in Echtzeit an.

### 📦 Schnellstart-Anleitung
Führen Sie die folgenden Befehle in Ihrem Terminal aus, um das Projekt zu starten:

```bash
# 1. Repository herunterladen
git clone https://github.com/KristinaAlokhina/system_monitor

# 2. In das Projektverzeichnis wechseln
cd system_monitor

# 3. Anwendung starten
python system_monitor.py
```

---

## 🇺🇸 English

A lightweight, cross-platform system monitor featuring a graphical user interface for real-time tracking of disk space and CPU usage.

### 🚀 Key Features
* **Automated Drive Detection**: Automatically identifies the host OS and calculates available vs. used storage in both Gigabytes and percentages.
* **Dynamic CPU Simulation**: Demonstrates seamless UI updates using a time-based random variance model for processor load simulation.
* **Smart Alert System**: Adaptive color coding (Green, Yellow, Orange, Red) that shifts dynamically based on resource critical levels.
* **Instant Refresh**: Automatic data polling and interface synchronization every 2000 milliseconds (2 seconds).
* **Cross-Platform UI**: Built on Tkinter's native `clam` theme to ensure clean, consistent progress bar rendering across different operating systems.

### 🛠️ Tech Stack
* **Runtime**: Python 3.x
* **Built-in Modules**: `os`, `shutil`, `sys`, `datetime`, `random`, `string`
* **GUI Library**: `tkinter` (included in standard Python installations)

### 📂 Layout Structure
The dashboard is split into three main functional zones:
1. **Header & Timestamp**: Displays the application status and the precise time of the most recent data refresh.
2. **Storage Allocation Box**: Renders progress bars and text metrics for all active partitions (`C:\`, `D:\` on Windows or `/` on Unix/Linux).
3. **Processor Load Box**: Monitors and visualizes the simulated real-time CPU capacity.

### 📦 Installation & Setup
Run the following commands in your terminal to deploy and launch the script:

```bash
# 1. Clone the repository
git clone https://github.com/KristinaAlokhina/system_monitor

# 2. Navigate to the project directory
cd system_monitor

# 3. Run the application
python system_monitor.py
```

   cd system_monitor
   ```
3. Run the script:
   ```bash
   python system_monitor.py
   ```
