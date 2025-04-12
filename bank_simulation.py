import threading
import time
import random

# Shared semaphores
door_semaphore = threading.Semaphore(2)
safe_semaphore = threading.Semaphore(2)
manager_semaphore = threading.Semaphore(1)

# Other global structures (you’ll expand later)
teller_ready = [threading.Semaphore(0) for _ in range(3)]
teller_locks = [threading.Lock() for _ in range(3)]
customer_queue = []
queue_lock = threading.Lock()

# Signals for communication between teller and customer
customer_ready = [threading.Semaphore(0) for _ in range(3)]
transaction_ready = [threading.Semaphore(0) for _ in range(3)]
transaction_done = [threading.Semaphore(0) for _ in range(3)]
customer_left = [threading.Semaphore(0) for _ in range(3)]

class Teller(threading.Thread):
    def __init__(self, teller_id):
        super().__init__()
        self.teller_id = teller_id

    def run(self):
        print(f"Teller {self.teller_id} [Teller {self.teller_id}]: ready to serve")

        while True:
            # Wait for customer
            customer_ready[self.teller_id].acquire()
            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: asks for transaction")

            # Wait for transaction
            transaction_ready[self.teller_id].acquire()

            # Simulate withdraw needing manager approval
            # Will update this part once customer logic is added

            # Access the safe
            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: waiting for safe")
            safe_semaphore.acquire()
            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: using safe")
            time.sleep(random.uniform(0.01, 0.05))
            print(f"Teller {self.teller_id} [Teller {self.teller_id}]: done with safe")
            safe_semaphore.release()

            # Notify transaction complete
            transaction_done[self.teller_id].release()

            # Wait for customer to leave
            customer_left[self.teller_id].acquire()

class Customer(threading.Thread):
    def __init__(self, customer_id):
        super().__init__()
        self.customer_id = customer_id
        self.transaction_type = random.choice(['Deposit', 'Withdraw'])

    def run(self):
        time.sleep(random.uniform(0, 0.1))  # Wait 0-100ms before entering

        print(f"Customer {self.customer_id} [Customer {self.customer_id}]: waiting to enter bank")
        door_semaphore.acquire()
        print(f"Customer {self.customer_id} [Customer {self.customer_id}]: enters bank")

        # Pick the first available teller
        for i in range(3):
            if teller_locks[i].acquire(blocking=False):
                print(f"Customer {self.customer_id} [Teller {i}]: selects teller")
                customer_ready[i].release()
                print(f"Customer {self.customer_id} [Teller {i}]: gives transaction ({self.transaction_type})")
                transaction_ready[i].release()

                # Simulate manager interaction for withdrawal
                if self.transaction_type == 'Withdraw':
                    print(f"Teller {i} [Teller {i}]: going to manager")
                    manager_semaphore.acquire()
                    print(f"Teller {i} [Teller {i}]: using manager")
                    time.sleep(random.uniform(0.005, 0.03))
                    print(f"Teller {i} [Teller {i}]: done with manager")
                    manager_semaphore.release()

                transaction_done[i].acquire()

                print(f"Customer {self.customer_id} [Teller {i}]: transaction done, leaving")
                customer_left[i].release()
                teller_locks[i].release()
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
