# Password Generator Project 🔒

A professional-grade CLI Password Generator built with Python.
Part of the **120 Days of Code Challenge** - Day 1.

## Features
- **Customizable**: Choose length, uppercase, numbers, symbols.
- **Ambiguity Filter**: Option to remove confusing characters like `l`, `1`, `O`, `0`.
- **Strength Meter**: Estimates password strength (Weak to Very Strong).
- **Clipboard Integration**: One-click copy (requires `pyperclip`).
- **History Log**: Keeps a local record of generated passwords in `history.txt`.

## Usage
### CLI Version
```bash
python main.py
```
Follow the interactive prompts.

### Web App Version 🚀
```bash
pip install -r requirements.txt
streamlit run app.py
```
This will open the generator in your web browser.

## Project Structure
- `main.py`: Entry point and user interface.
- `generator.py`: Core logic for password generation.
- `utils.py`: Helper functions for clipboard, history, and analytics.
- `requirements.txt`: Project dependencies.
