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

## 📃 Commands  
1. ADD EXPENSES
python main.py add --description "Lunch" --amount 20
Expense added successfully (ID: 1)

python main.py add --description "Petrol" --amount 200
Expense added successfully (ID: 2)

python main.py add --description "Take-out" --amount 120
Expense added successfully (ID: 3)



2. LIST ALL EXPENSES
python main.py list
ID   Date         Description          Amount    
------------------------------------------------
1    2026-07-31   Lunch                ₹20.00    
2    2026-07-31   Petrol               ₹200.00   
3    2026-07-31   Take-out             ₹120.00   

3. GET EXPENSE SUMMARIES

Total expense across all time
python main.py summary
Total expenses: ₹340.00

Expense summary for a specific month (e.g., July = 7)
python main.py summary --month 7
Total expenses for July: ₹340.00

4. UPDATE AN EXPENSE
Update description or amount by ID
python main.py update --id 1 --amount 25.50
Expense updated successfully

5. DELETE AN EXPENSE
Delete expense by ID
python main.py delete --id 2
Expense deleted successfully

6. VERIFY AFTER UPDATE & DELETE
python main.py list
ID   Date         Description          Amount    
------------------------------------------------
1    2026-07-31   Lunch                ₹25.50    
3    2026-07-31   Take-out             ₹120.00   

python main.py summary
Total expenses: ₹145.50

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/HimanshuBhamaniya/Expense-Tracker.git]
cd Expense-Tracker
