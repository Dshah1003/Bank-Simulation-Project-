# Devlog – Bank Simulation Project (CS4348 Project 2)

## April 12, 2025 – 5:00 PM

### Thoughts So Far
The project simulates a bank using threads for tellers and customers. The bank has 3 tellers and 50 customers, and there are constraints around how they interact. For example:
- Only 2 customers can enter the bank at a time.
- Only 2 tellers can be in the safe at once.
- Only 1 teller can interact with the manager at a time.
This requires synchronization using semaphores.

### Plan for Today
- Set up Git repo and initial project folder
- Write this devlog entry and commit it
- Review and outline thread classes and shared semaphores in a design diagram (next step)

## April 12, 2025 – 6:00 PM

### Thoughts So Far
Broke down the shared resources and how customers/tellers communicate.
Started implementing the core simulation logic using threads and semaphores in Python.

### Plan for Next Session
- Add more print/logging statements for output formatting
- Refine manager/safe interaction logic
- Make sure output matches assignment format exactly
## April 12, 2025 – 6:40 PM

### Thoughts So Far
Successfully implemented full teller-customer interaction including:
- Transaction passing
- Safe and manager access
- Semaphore-based synchronization
- Correct log format

Tested with 5 customers to verify correctness.

### What I Did This Session
- Finalized customer and teller logic
- Connected threads using shared transaction buffer
- Ensured proper entry/exit logging and sleep delays
- Debugged interactions with smaller test case

### Plan for Next Session
- Scale up to 50 customers
- Add README and test logs
- Prepare for final packaging

## April 12, 2025 – 7:30 PM

### Thoughts So Far
The customer and teller thread logic is now fully implemented and synchronized. I used semaphores to control access to shared resources like the manager's office and the safe, and also to ensure proper communication between threads.

### What I Did This Session
- Completed the full `Customer.run()` method:
  - Customers wait at the door using a semaphore (max 2 inside).
  - Each customer chooses a teller by acquiring a lock.
  - Passes the transaction type (Deposit or Withdraw) to the teller using a shared list.
  - Waits for transaction to complete, then leaves.
- Finalized the `Teller.run()` method:
  - Waits for a customer signal.
  - Reads the transaction type.
  - For Withdrawals: interacts with the manager (mutex with semaphore).
  - Uses the safe (limited to 2 tellers).
  - Notifies customer that transaction is complete.
- Ensured log formatting is clean: `THREAD_TYPE ID [THREAD_TYPE ID]: message`.
- Validated this logic with a small test run using 5 customers.

### Plan for Next Session
- Run a full test with all 50 customer threads.
- Verify all logs print correctly and no deadlocks occur.
- Create README and prep project for submission.


## April 12, 2025 – 7:45 PM

### Thoughts So Far
Ran the simulation with 50 customers and everything executed successfully. All customers were served by one of the 3 tellers. There were no deadlocks or synchronization issues. The logs followed the required format and showed proper sequencing of events (entry, teller selection, manager/safe access, transaction, and exit).

### What I Did This Session
- Tested the full run of the program using 50 customer threads.
- Validated:
  - Max 2 customers inside the bank at a time.
  - Only 2 tellers using the safe concurrently.
  - Only 1 teller with the manager at any time.
- Observed randomized transaction types (Withdraw/Deposit).
- Verified that all customer–teller interactions completed.
- Checked the final summary message: `All customers have been served. Bank is closing.`
- Confirmed no issues even with heavy concurrency.

### Final Thoughts
Happy with how the project turned out! This helped me understand thread synchronization using semaphores in real-world scenarios. I now feel more confident handling concurrency in operating systems and system-level design.

### Plan for Next Session
- Final commit and ZIP creation.
- Submit the project on eLearning.