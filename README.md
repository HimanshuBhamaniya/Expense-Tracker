# 💰 Expense Tracker CLI

A simple **Command Line Interface (CLI) Expense Tracker** built in Python.  
This project is inspired by the [roadmap.sh Expense Tracker project](https://roadmap.sh/projects/expense-tracker) and is designed to help practice clean software architecture, JSON storage, and CLI application development in Python.

---

## 📖 Overview
The Expense Tracker lets you:
- Add new expenses with descriptions and amounts
- List all recorded expenses with formatting
- Update expense details by ID
- Delete expenses by ID
- View total spending summary (overall or by specific month)

All expenses are stored locally in a `storage.json` file using atomic write operations for data integrity.

---

## ⚙️ Features
- **Add expenses** with descriptions and amounts
- **List expenses** in a clean tabular view with dates and auto-formatted currency
- **Update expenses** by ID (change description or amount)
- **Delete expenses** by ID
- **Summary calculation** for total overall expenses or filtered by month
- **Persistent & Safe storage** using JSON with atomic writes

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/HimanshuBhamaniya/Expense-Tracker.git]
cd Expense-Tracker
