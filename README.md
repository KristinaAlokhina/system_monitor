<p align="center">
  <ins><b><kbd>&nbsp;DESKTOP APPLICATION&nbsp;</kbd></b></ins>
</p>

<h1 align="center" style="font-size: 2.5rem; font-weight: 900; color: #1a1a1a; margin-top: 10px; margin-bottom: 10px; border-bottom: none;">
  📊 ADVANCED SYSTEM MONITOR (v1.0)
</h1>

<p align="center">
  <strong>Ein moderner Multi-Laufwerk- und CPU-Ressourcenmonitor mit nativer grafischer Benutzeroberfläche.</strong>
  <br />
  <i>Entwickelt mit Python, Tkinter und Psutil für präzise Hardware-Überwachung in Echtzeit.</i>
</p>

<p align="center">
  <a href="#-deutsch">🇩🇪 Deutsch</a> • 
  <a href="#-english">🇺🇸 English</a> • 
  <a href="#-русский">🇷🇺 Русский</a> • 
  <a href="#-українська">🇺🇦 Українська</a>
</p>

---

## 🇩🇪 Deutsch

Die Anwendung bietet ein kompaktes, hochfunktionales Dashboard zur Echtzeitüberwachung von Systemspeicher und Prozessorauslastung. Perfekt optimiert für Administratoren zur schnellen Diagnose von Speicherengpässen.

### 🚀 Funktionen
* **Multi-Sprachunterstützung (4 Sprachen) 🌍**: Vollständige Lokalisierung für Deutsch, Englisch, Russisch und Ukrainisch. Die Sprache kann mitten im Betrieb per Knopfdruck gewechselt werden und wird für den nächsten Start in `config.json` gespeichert.
* **Erweiterte Farbcodierung 🎨**: Prozentsätze ändern dynamisch ihre Farbe (Grün ➔ Gelb ➔ Orange ➔ Rot) basierend auf der aktuellen Hardware-Last.
* **Dynamische Laufwerkserkennung 💾**: Erkennt automatisch alle aktiven Partitionen und Mount-Punkte auf Windows- und Unix-Systemen, berechnet freien/belegten Speicherplatz und passt die Fensterhöhe flexibel an.
* **Theme-Umschalter (Dark/Light) 🌓**: Schneller Wechsel zwischen augenschonendem Dunkelmodus und klarem Hellmodus.
* **Erzwungener Admin-Modus 🛡️**: Startet sich automatisch mit erhöhten Rechten neu, falls erforderlich, um blockierungsfreien Zugriff auf Systemmetriken zu gewährleisten.

### 🛠️ Technologien
* **Framework**: Python Tkinter (mit erweitertem `ttk`-Flachstyling)
* **Metriken**: `psutil` (Prozessordaten), `shutil` (Speicheranalysen)
* **Daten-Persistenz**: Native `json`-Konfiguration zur persistenten Speicherung der Benutzersprache.

### 📦 Installation & Ausführung

#### Option A: Standalone Ausführung (.exe)
Laden Sie die kompilierte Datei `system_monitor.exe` aus den Releases herunter und führen Sie sie direkt aus.

#### Option B: Ausführung aus dem Quellcode
Es werden Python 3.x und die `psutil`-Bibliothek benötigt.

1. Repository klonen:
   ```bash
   git clone https://github.com
   ```
2. In den Projektordner wechseln:
   ```bash
   cd system-monitor
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install psutil
   ```
4. Die Anwendung starten:
   ```bash
   python system_monitor.py
   ```

---

## 🇺🇸 English

A high-performance system metrics dashboard designed to aggregate and view hardware workloads, including individual storage drives and real-time thread utilization.

### 🚀 Features
* **On-the-Fly Multi-Language 🌍**: Native interface tracking for English, German, Russian, and Ukrainian. Prompted during first boot and completely adjustable at runtime via interactive header toggles.
* **Dynamic Loading Visualizers 🎨**: Text readouts actively shift color gamuts (Green ➔ Yellow ➔ Orange ➔ Red) to reflect performance thresholds instantly.
* **Cross-Platform Drive Scanner 💾**: Traverses native volumes (`C:\`, `D:\`) or Unix mounts (`/`, `/media`), fetching accurate disk bounds and setting fluid window constraints.
* **Dual Palette Theme Swapper 🌓**: Seamlessly redraws all canvas frames between customized high-contrast Dark and Light aesthetic models.
* **Self-Elevating Admin Protocol 🛡️**: Built-in safeguards check user execution context, automatically prompting for UAC permissions to extract secure hardware streams.

### 🛠️ Technologies
* **Framework**: Python Tkinter (stylized with precise structural flat `ttk` parameters)
* **Metrics Engine**: `psutil` (CPU thread states), `shutil` (high-level storage tracking)
* **Data Layer**: Clean `json` flat-file pipeline handling long-term translation preferences.

### 📦 Installation & Setup

#### Option A: Standalone Execution (.exe)
Grab the standalone `system_monitor.exe` from the GitHub releases pipeline. Completely portable with zero runtime hooks needed.

#### Option B: Source Code Setup
Requires a standard Python 3.x package configuration environment.

1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to project root:
   ```bash
   cd system-monitor
   ```
3. Install required library:
   ```bash
   pip install psutil
   ```
4. Initialize the monitor:
   ```bash
   python system_monitor.py
   ```

---

## 🇷🇺 Русский

Компактная утилита мониторинга ресурсов, которая собирает данные о загруженности процессора и всех доступных в системе жестких дисков. Идеальный инструмент для быстрого контроля за состоянием железа в реальном времени.

### 🚀 Возможности
* **Мультиязычность на лету (4 языка) 🌍**: Полная поддержка русского, английского, немецкого и украинского языков. Локализация переключается кнопкой в интерфейсе и сохраняется в файл `config.json`.
* **Умная цветовая индикация 🎨**: Текст с процентами динамически меняет свой цвет в зависимости от тяжести нагрузки (Зеленый ➔ Желтый ➔ Оранжевый ➔ Красный).
* **Автоопределение накопителей 💾**: Сканирует активные разделы Windows или точки монтирования Unix, рассчитывает объемы накопителей и автоматически подстраивает высоту окна под количество дисков.
* **Смена тем оформления 🌓**: Полноценная поддержка адаптивного ночного (Dark) и дневного (Light) графических режимов.
* **Автоматический запуск с правами админа 🛡️**: Скрипт самостоятельно запрашивает повышенные привилегии (UAC) при старте, чтобы иметь беспрепятственный доступ к низкоуровневым метрикам ОС.

### 🛠️ Технологии
* **Графика**: Python Tkinter (с применением кастомных стилей `ttk`)
* **Сбор данных**: `psutil` (метрики CPU), `shutil` (анализ дискового пространства)
* **Конфигурация**: Модуль `json` для хранения языковых предпочтений пользователя между перезапусками.

### 📦 Установка и запуск

#### Вариант А: Готовый исполняемый файл (.exe)
Скачайте скомпилированный файл `system_monitor.exe` из раздела релизов и запустите его. Установка Python и зависимостей не требуется.

#### Вариант Б: Запуск из исходного кода
Требуется интерпретатор Python 3.x и библиотека `psutil`.

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com
   ```
2. Перейдите в папку проекта:
   ```bash
   cd system-monitor
   ```
3. Установите модуль `psutil`:
   ```bash
   pip install psutil
   ```
4. Запустите монитор:
   ```bash
   python system_monitor.py
   ```

---

## 🇺🇦 Українська

Компактна утиліта моніторингу ресурсів, що збирає дані про завантаженість процесора та всіх доступних у системі жорстких дисків. Ідеальний інструмент для швидкого контролю стану заліза в реальному часі.

### 🚀 Можливості
* **Мультиязычність на льоту (4 мови) 🌍**: Повна підтримка української, англійської, німецької та російської мов. Локалізація перемикається однією кнопкою в інтерфейсі та зберігається у файл `config.json`.
* **Розумна колірна індикація 🎨**: Текст із відсотками динамічно змінює свій колір залежно від рівня навантаження (Зелений ➔ Жовтий ➔ Помаранчевий ➔ Червоний).
* **Автовизначення накопичувачів 💾**: Сканує активні розділи Windows або точки монтування Unix, розраховує обсяги накопичувачів та автоматично підлаштовує висоту вікна під кількість дисків.
* **Зміна тем оформлення 🌓**: Повноцінна підтримка адаптивного нічного (Dark) та денного (Light) графічних режимів.
* **Автоматичний запуск із правами адміна 🛡️**: Скрипт самостійно запитує підвищені привілеї (UAC) під час старту, щоб мати безперешкодний доступ до низькорівневих метрик ОС.

### 🛠️ Технології
* **Графіка**: Python Tkinter (із застосуванням кастомних стилів `ttk`)
* **Збір даних**: `psutil` (метрики CPU), `shutil` (аналіз дискового простору)
* **Конфігурація**: Модуль `json` для збереження мовних уподобань користувача між перезапусками.

### 📦 Встановлення та запуск

#### Вариант А: Готовий виконуваний файл (.exe)
Завантажте скомпільований файл `system_monitor.exe` із розділу релізів та запустіть його. Встановлення Python та залежностей не потрібне.

#### Вариант Б: Запуск із вихідного коду
Необхідно мати встановлений інтерпретатор Python 3.x та бібліотеку `psutil`.

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com
   ```
2. Перейдіть до папки проєкту:
   ```bash
   cd system-monitor
   ```
3. Встановіть модуль `psutil`:
   ```bash
   pip install psutil
   ```
4. Запустіть монітор:
   ```bash
   python system_monitor.py
   ```
