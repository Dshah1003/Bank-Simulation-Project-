# CS4348 – Project 2: Bank Simulation

##  Author
Drashti Shah  


---

## Files Included
- `bank_simulation.py` – Main Python program simulating the multithreaded bank
- `devlog.md` – Development log with time-stamped progress entries
- `README.md` – This file, containing instructions and documentation

---

## Project Description
This project simulates a bank environment using threads and semaphores:

- **3 Tellers (threads)** ready to serve customers
- **50 Customers (threads)** each randomly performing either a Deposit or Withdrawal
- Controlled access to:
  - **Bank door** (only 2 customers allowed at a time)
  - **Manager** (only 1 teller at a time for Withdrawals)
  - **Safe** (only 2 tellers allowed inside at a time)
- Uses **Python’s `threading` module and semaphores** for synchronization

---

## 🛠️ How to Run the Program

###  Requirements
- Python 3.x installed

###  To Run the Simulation
Open terminal or command prompt, then run:
```bash
python bank_simulation.py
