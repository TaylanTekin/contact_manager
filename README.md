# 📇 Contact Manager

A simple console-based contact manager built with Python.  
It lets you add, view, and clear contacts — each contact includes a name, phone number, and email address.

---

## 🚀 Features

- Add new contacts with name, phone, and email
- View all saved contacts from `contacts.txt`
- Clear all saved contacts
- Input validation (e.g. phone number must be numeric)
- File-based storage (`contacts.txt`)

---

## 🛠 How It Works

- Contacts are stored as dictionaries in a list.
- New contacts are appended to the file `contacts.txt`.
- The file is read line by line and split by commas to display saved info.
- You can clear all contacts by choosing option 3 in the main menu.

---

## 📦 Requirements

Just Python 3 — no external libraries needed.

---

## 💡 How to Run

1. Save the script as `contact_manager.py`
2. Open a terminal or command prompt
3. Run the program:

```bash
python contact_manager.py
