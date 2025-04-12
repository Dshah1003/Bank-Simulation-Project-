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
