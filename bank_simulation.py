import threading
import time
import random

# Shared resources
door_semaphore = threading.Semaphore(2)        # Only 2 customers can enter bank at a time
safe_semaphore = threading.Semaphore(2)        # Only 2 tellers in the safe at a time
manager_semaphore = threading.Semaphore(1)     # Only 1 teller with manager at a time

# Teller communication structures
teller_ready = [threading.Semaphore(0) for _ in range(3)]
customer_ready = [threading.Semaphore(0) for _ in range(3)]
transaction_ready = [threading.Semaphore(0) for _ in range(3)]
transaction_done = [threading.Semaphore(0) for _ in range(3)]
customer_left = [threading.Semaphore(0) for _ in range(3)]

teller_locks = [threading.Lock() for _ in range(3)]  # To lock teller while in use
shared_transactions = [None] * 3                     # Teller-wise transaction type buffer


class Teller(threading.Thread):
    def __init__(self, teller_id):
        super().__init__()
        self.teller_id = teller_id

    def run(self):
        print(f"Teller {self.teller_id} [Teller {self.teller_id}]: ready to serve")

        while True:
            customer_ready[self.teller_id].acquire()
            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: asks for transaction")

            transaction_ready[self.teller_id].acquire()

            transaction_type = shared_transactions[self.teller_id]

            if transaction_type == 'Withdraw':
                print(f"Teller {self.teller_id} [Teller {self.teller_id}]: going to manager")
                manager_semaphore.acquire()
                print(f"Teller {self.teller_id} [Teller {self.teller_id}]: using manager")
                time.sleep(random.uniform(0.005, 0.03))
                print(f"Teller {self.teller_id} [Teller {self.teller_id}]: done with manager")
                manager_semaphore.release()

            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: waiting for safe")
            safe_semaphore.acquire()
            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: using safe")
            time.sleep(random.uniform(0.01, 0.05))
            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: done with safe")
            safe_semaphore.release()

            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: transaction complete")
            transaction_done[self.teller_id].release()

            customer_left[self.teller_id].acquire()


class Customer(threading.Thread):
    def __init__(self, customer_id):
        super().__init__()
        self.customer_id = customer_id
        self.transaction_type = random.choice(['Deposit', 'Withdraw'])

    def run(self):
        time.sleep(random.uniform(0, 0.1))  # Step 2: wait 0–100 ms

        print(f"Customer {self.customer_id} [Customer {self.customer_id}]: waiting to enter bank")
        door_semaphore.acquire()
        print(f"Customer {self.customer_id} [Customer {self.customer_id}]: enters bank")

        assigned = False
        while not assigned:
            for i in range(3):
                if teller_locks[i].acquire(blocking=False):
                    print(f"Customer {self.customer_id} [Teller {i}]: selects teller")
                    print(f"Customer {self.customer_id} [Teller {i}]: gives transaction ({self.transaction_type})")

                    shared_transactions[i] = self.transaction_type

                    customer_ready[i].release()
                    transaction_ready[i].release()

                    transaction_done[i].acquire()
                    print(f"Customer {self.customer_id} [Teller {i}]: transaction complete, leaving")

                    customer_left[i].release()
                    teller_locks[i].release()
                    assigned = True
                    break

        print(f"Customer {self.customer_id} [Customer {self.customer_id}]: leaves bank")
        door_semaphore.release()


def main():
    tellers = [Teller(i) for i in range(3)]
    for t in tellers:
        t.start()

    customers = [Customer(i) for i in range(50)]
    for c in customers:
        c.start()

    for c in customers:
        c.join()

    print("All customers have been served. Bank is closing.")


if __name__ == "__main__":
    main()
customers = [Customer(i) for i in range(5)]