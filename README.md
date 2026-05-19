<div align="center">

# StayAwake

**Tiny cross-platform mouse jiggler. Keeps your screen alive: no lock, no logout.**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey.svg)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

---

## Why

Screen locks during long downloads, demos, remote sessions, or while reading?
StayAwake nudges the cursor by 1px every few seconds. Enough to register as
activity, invisible to you.

## Quick start

```bash
git clone https://github.com/pradhanashutosh/stayawake.git
cd stayawake
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

That's it. Cursor jiggles every 30 seconds until you stop it.

## Usage

| Command              | What it does                          |
| -------------------- | ------------------------------------- |
| `python main.py`     | Jiggle every 30 seconds (default)     |
| `python main.py 10`  | Jiggle every 10 seconds               |
| `python main.py 120` | Jiggle every 2 minutes                |

**Stop it:** `Ctrl+C`, or move the cursor to the top-left corner of the
screen (PyAutoGUI's built-in failsafe).

## How it works

- Reads current cursor position
- Moves it +1px on the x-axis, sleeps 0.2s, moves it back
- Sleeps for the chosen interval, repeats
- Runs in a daemon thread, so `Ctrl+C` exits cleanly

## macOS first-run setup

PyAutoGUI needs **Accessibility** permission to move the cursor.

1. Run `python main.py` once. macOS prompts you.
2. Or manually: **System Settings → Privacy & Security → Accessibility → +**,
   then add your terminal app (or the `Python.app` inside your venv).
3. Toggle it **on**.

Without this permission, the script appears to run but the cursor never moves.

> **macOS alternative:** `caffeinate -d` is built in and prevents display
> sleep without any cursor movement. Use StayAwake when you specifically need
> fake input activity (remote sessions, presence detection).

## Auto-start on login (macOS)

Save as `~/Library/LaunchAgents/com.user.stayawake.plist` (edit the two
absolute paths):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key><string>com.user.stayawake</string>
    <key>ProgramArguments</key>
    <array>
        <string>/absolute/path/to/stayawake/.venv/bin/python</string>
        <string>/absolute/path/to/stayawake/main.py</string>
        <string>30</string>
    </array>
    <key>RunAtLoad</key><true/>
    <key>KeepAlive</key><true/>
</dict>
</plist>
```

Then load it:

```bash
launchctl load -w ~/Library/LaunchAgents/com.user.stayawake.plist
```

To stop and remove:

```bash
launchctl unload -w ~/Library/LaunchAgents/com.user.stayawake.plist
```

## Use responsibly

StayAwake is for **your own machine, on your own time**: long-running tasks,
demos, presentations, reading. Don't use it to fake presence on systems you
don't own or to dodge legitimate activity tracking by your employer.

## License

[MIT](LICENSE)
