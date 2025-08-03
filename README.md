🧙‍♂️ ASCIIQuest: Terminal Rogue Game

**ASCIIQuest** is a retro-style terminal-based rogue-like adventure game built entirely in Python using the `curses` module. Featuring dynamic maps, procedural item placement, enemy encounters, and real-time combat — this game delivers an old-school experience in a clean, modular codebase.

---

## 🎯 Features

- 🔁 **Infinite Replayability** – Randomly generated rooms, enemies, and item drops.
- ⚔️ **Combat System** – Battle goblins and monsters with turn-based logic.
- 💡 **Fog of War** – Visibility depends on player's proximity.
- 🚪 **Doors, Keys & Treasures** – Collect keys to unlock doors and loot rare treasures.
- ✨ **Powerups** – Health potions, weapon boosts, and more.
- 🎮 **Keyboard Controls** for full gameplay:
  - `W A S D` — Movement
  - `Q` — Quit the game

---

## 🛠️ Tech Stack

- Python 3.x
- curses (standard terminal GUI)
- Modular design with MVC-like structure

---

## 🚀 How to Run

> **Make sure you are using a terminal that supports `curses` (Linux/macOS or Windows via WSL/PowerShell + Windows Terminal).**

### 1. Clone the Repository
git clone https://github.com/M-ar-SHAL/RogueGame.git
cd RogueGame


### 2. Install Requirements
No external packages required! Just make sure Python 3 is installed.

### 3. Run the Game
python main.py


---

## 📁 Project Structure

RogueGame/
│
├── main.py              # Game entry point
├── game/
│   ├── engine.py        # Main game loop and logic
│   ├── player.py        # Player logic and stats
│   ├── enemies.py       # Enemy AI
│   ├── map.py           # Map generation
│   ├── items.py         # Items and pickups
│   └── ui.py            # Terminal rendering with curses
├── README.md
└── assets/
    └── screenshot.png   # Sample gameplay screenshot


---

## 💼 Why This Project Stands Out

> Built to impress recruiters with:

* Clean modular architecture
* Advanced terminal handling
* Procedural generation logic
* Real-time combat and enemy AI
* Unique, non-boilerplate project idea

---

## 📜 License

MIT License — free to use and modify.

---

## 🙋‍♂️ Author

Built with ❤️ by [Anshuman Mishra](https://github.com/M-ar-SHAL)


