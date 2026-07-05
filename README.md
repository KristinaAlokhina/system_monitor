# System Resource Monitor

A lightweight Python script to monitor system disk usage and display platform information. It automatically detects the operating system and checks the main drive (`C:\` on Windows, `/` on Linux/macOS).

---

## English

### Features
* **Cross-platform**: Works seamlessly on Windows, Linux, and macOS.
* **Disk Analysis**: Displays total space, free space, and free percentage.
* **Alert System**: Issues a `[WARNING]` if free space drops below 10%.
* **Safe Execution**: Wrapped in error handling to prevent crashes.

### Requirements
* Python 3.x (No external dependencies required).

### Usage
Run the script using your terminal or command prompt:
```bash
python monitor.py
```

---

## Deutsch

### Funktionen
* **Plattformübergreifend**: Funktioniert unter Windows, Linux und macOS.
* **Speicheranalyse**: Zeigt den Gesamtspeicher, den freien Speicher und den Prozentsatz des freien Speichers an.
* **Warnsystem**: Gibt eine `[WARNUNG]` aus, wenn der freie Speicherplatz unter 10 % fällt.
* **Sichere Ausführung**: Fehlerbehandlung verhindert unerwartete Abstürze.

### Voraussetzungen
* Python 3.x (Keine externen Abhängigkeiten erforderlich).

### Verwendung
Führen Sie das Skript über das Terminal oder die Eingabeaufforderung aus:
```bash
python monitor.py
```
