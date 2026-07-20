# System-Ressourcen-Monitor

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>


---

## 🇩🇪 Deutsch


### 🚀 Funktionen
* **Echtzeit-Festplattenanalyse**: Erkennt automatisch das Betriebssystem и berechnet den belegten sowie freien Speicherplatz in Prozent und Gigabyte.
* **Dynamische CPU-Simulation**: Simuliert kontinuierliche Änderungen der Prozessorauslastung mithilfe von zeitbasierten Zufallswerten zur Demonstration von UI-Updates.
* **Intelligente Farbcodierung**: Ändert die Textfarbe der Widgets щелчком мыши (Grün, Gelb, Orange, Rot) basierend auf der Kritikalität der Ressourcenauslastung.
* **Automatische Aktualisierung**: Die Benutzeroberfläche liest und aktualisiert die Systemdaten vollautomatisch alle 2000 Millisekunden (2 Sekunden).
* **Modernes GUI-Design**: Nutzt das `clam`-Theme von Tkinter für eine konsistente und plattformübergreifende Darstellung der Fortschrittsbalken.

### 🛠️ Technologien
* Python 3.x
* Integrierte Module: `os`, `shutil`, `sys`, `datetime`, `random`
* GUI-Bibliothek: `tkinter` (Standardmäßig in Python enthalten)

### 📂 Struktur der Benutzeroberfläche
Das Fenster ist in folgende Bereiche unterteilt:
* **Uhrzeit & Status**: Zeigt den Anwendungsnamen und die exakte Uhrzeit der letzten Datenaktualisierung.
* **Festplatten-Anzeige**: Fortschrittsbalken und Statusmeldung für den Hauptspeicher (`C:\` unter Windows, `/` unter Unix/Linux).
* **Prozessor-Anzeige**: Fortschrittsbalken und Prozentanzeige für die simulierte Prozessorauslastung.

### 📦 Installation & Start
1. Repository klonen:
   ```bash
   git clone https://github.com/KristinaAlokhina/system_monitor
   ```
2. Skript ausführen:
   ```bash
   system_monitor.py
   ```

---

## 🇺🇸 English


### 🚀 Features
* **Real-time Disk Tracking**: Automatically detects your OS and calculates used and free storage space in percentages and Gigabytes.
* **Dynamic CPU Simulation**: Simulates continuous processor load changes using time-based random variance to demonstrate UI state updates.
* **Smart Color Coding**: UI text labels dynamically change colors (Green, Yellow, Orange, Red) based on resource critical levels.
* **Automated Refresh**: The interface automatically pulls and updates system data every 2000 milliseconds (2 seconds).
* **Modern UI Styling**: Uses Tkinter's `clam` theme for clean and consistent cross-platform progress bar rendering.

### 🛠️ Technologies
* Python 3.x
* Built-in modules: `os`, `shutil`, `sys`, `datetime`, `random`
* GUI Library: `tkinter` (Bundled with standard Python installations)

### 📂 User Interface Structure
The layout is divided into the following sections:
* **Header & Timestamp**: Displays the app title and the exact time of the latest data refresh.
* **Disk Space Box**: Status label and progress bar for the primary drive (`C:\` on Windows, `/` on Unix/Linux).
* **CPU Load Box**: Status label and progress bar showing the simulated processor load.

### 📦 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/KristinaAlokhina/system_monitor
   ```
2. Run the script:
   ```bash
   system_monitor.py
   ```
