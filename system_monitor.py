import os
import shutil
import sys
from datetime import datetime

def check_disk_usage(disk_path="/"):
    # Festplattendaten (Gesamt, Belegt, Frei) in Bytes abrufen.
    try:
        total, used, free = shutil.disk_usage(disk_path)
        # Zur besseren Lesbarkeit rechnen wir in Gigabyte um.
        total_gb = total / (2**30)
        free_gb = free / (2**30)
        percent_free = (free / total) * 100
        
        print(f"Festplatte ({disk_path}):")
        print(f"  Gesamtspeicher: {total_gb:.2f} GB")
        print(f"  Freier Speicher: {free_gb:.2f} GB ({percent_free:.1f}% frei)")
        
        # Kritische Warnung bei geringem Speicherplatz
        if percent_free < 10.0:
            print("[WARNUNG] Der freie Festplattenspeicher liegt unter 10%!")
        else:
            print("[INFO] Festplattenspeicher ist im grünen Bereich.")
            
    except Exception as e:
        print(f"[FEHLER] Speicheranalyse fehlgeschlagen: {e}")

def check_system_info():
    print(f"=== System-Ressourcen-Monitor ===")
    print(f"Zeitpunkt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Betriebssystem-Plattform: {sys.platform}")
    print("-" * 35)
    
    # Wir überprüfen das Hauptlaufwerk (unter Windows ist es „C:“, unter Linux/Mac „/“).
    root_path = "C:\\" if os.name == 'nt' else '/'
    check_disk_usage(root_path)
    print("=" * 35)

if __name__ == "__main__":
    check_system_info()
