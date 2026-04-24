# 🔐 Password Generator

A command-line password generating tool written in Python. Quickly generate strong, customizable passwords with clipboard support.

---

## Features

- Set a custom password length (minimum 8 characters)
- Choose from 3 password strength modes:
  - **Strong** — uppercase, lowercase, numbers & symbols
  - **Medium** — uppercase, lowercase & numbers
  - **Simple** — letters only
- Generate multiple passwords in a single run
- Automatically copies the first generated password to your clipboard

---

## Requirements

- Python 3.x
- [`pyperclip`](https://pypi.org/project/pyperclip/) — for clipboard support

Install the dependency with:

```bash
pip install pyperclip
```

> **Note for Linux users:** `pyperclip` may require `xclip` or `xsel`:
> ```bash
> sudo apt install xclip
> ```

---

## Installation

```bash
git clone https://github.com/jacebate/generatorPassword.git
cd generatorPassword
pip install pyperclip
```

---

## Usage

Run the script from your terminal:

```bash
python password_generator.py
```

You will be prompted to:

1. Enter a password length (8 or more)
2. Select a password strength mode (1, 2, or 3)
3. Specify how many passwords to generate

### Example session

```
=== Advanced Password Generator ===

Enter password length (minimum 8): 12

Choose password type:
1. Strong (Upper, lower, numbers, symbols)
2. Medium (upper, lower, numbers)
3. Simple (letters only)

Enter your choice (1/2/3): 1
Mode: Strong
How many passwords do you want to generate? 3

Generating 3 password(s)...

Password 1: aB3@kR7!mNpQ
Password 2: Tz9#wLc4$Yj6
Password 3: hG5^nXb8&vEr

First password has been copied to clipboard!
```

---

## Password Modes

| Mode | Characters Included | Best For |
|------|---------------------|----------|
| **1 - Strong** | A-Z, a-z, 0-9, symbols | High-security accounts |
| **2 - Medium** | A-Z, a-z, 0-9 | General use |
| **3 - Simple** | A-Z, a-z only | Low-security / easy to type |

---

## Project Structure

```
generatorPassword/
└── password_generator.py   # Main script
```

---

## Contributing

Contributions, bug reports, and feature suggestions are welcome! Feel free to open an issue or submit a pull request.

---

## License

This project is open source. See [GitHub](https://github.com/jacebate/generatorPassword) for more details.
