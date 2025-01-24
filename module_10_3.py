import threading
import time
import random

class Bank:
    def __init__(self):
        self.balance = 0 # баланс банка
        self.lock = threading.Lock()  # для блокировки потоков

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            dep = random.randint(50, 500)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            tak = random.randint(50, 500)
            print(f'Запрос на {tak}')
            if tak <= self.balance:
                self.balance -= tak
                print(f'Снятие: {tak}. Баланс: {self.balance}')
            elif tak > self.balance:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')