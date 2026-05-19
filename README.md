# StayAwake

Tiny mouse-jiggler. Prevents screen lock during long downloads, demos, remote sessions.

Cross-platform Python (macOS + Windows + Linux). No packaging.

## Install

```bash
git clone https://github.com/pradhanashutosh/stayawake.git
cd stayawake
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py            # jiggle every 30s (default)
python main.py 60         # jiggle every 60s
```

Stop: `Ctrl+C` or move mouse to top-left corner (pyautogui failsafe).

## macOS permissions

First run prompts for **Accessibility** access. Grant to your terminal:

System Settings → Privacy & Security → Accessibility → enable Terminal/iTerm.

Without it, mouse moves are blocked silently.

Alternative on macOS: built-in `caffeinate -d` prevents display sleep without moving mouse — use it if you don't need to fake activity to a remote session.

## Optional icon

```bash
python icon.py    # generates icon.png + icon.ico
```

Only needed if you later package to .app/.exe.

## Use legitimately

Prevent timeout during your own work. Don't fake presence to dodge monitoring.
