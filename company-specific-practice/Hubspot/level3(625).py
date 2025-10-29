from banking_system import BankingSystem

class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts = {}
        self.outgoing = {}
        self.payments = {}  # payment_id: payment_info
        self.scheduled = {} # timestamp: list of payment_ids
        self.payment_counter = 1

    def _process_payments(self, timestamp):
        # Helper: process due payments before any operation at timestamp
        if timestamp in self.scheduled:
            due_payments = self.scheduled[timestamp]
            due_payments.sort()  # paymentX comes before paymentY if X < Y
            for pid in due_payments:
                info = self.payments.get(pid)
                if info and not info['canceled']:
                    acc = info['account_id']
                    amount = info['amount']
                    if self.accounts.get(acc, 0) >= amount:
                        self.accounts[acc] -= amount
                        self.outgoing[acc] += amount
                        info['performed'] = True
            del self.scheduled[timestamp]

    def create_account(self, timestamp: int, account_id: str) -> bool:
        self._process_payments(timestamp)
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        self.outgoing[account_id] = 0
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        self._process_payments(timestamp)
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None:
        self._process_payments(timestamp)
        if (source_account_id not in self.accounts or
            target_account_id not in self.accounts or
            source_account_id == target_account_id or
            self.accounts[source_account_id] < amount):
            return None
        self.accounts[source_account_id] -= amount
        self.accounts[target_account_id] += amount
        self.outgoing[source_account_id] += amount
        return self.accounts[source_account_id]

    def top_spenders(self, timestamp: int, n: int) -> list[str]:
        self._process_payments(timestamp)
        sorted_accounts = sorted(
            self.outgoing.items(),
            key=lambda x: (-x[1], x[0])
        )
        return [f"{acc}({amt})" for acc, amt in sorted_accounts[:n]]

    def schedule_payment(self, timestamp: int, account_id: str, amount: int, delay: int) -> str | None:
        self._process_payments(timestamp)
        if account_id not in self.accounts:
            return None
        pid = f"payment{self.payment_counter}"
        info = {
            'account_id': account_id,
            'amount': amount,
            'scheduled_time': timestamp + delay,
            'canceled': False,
            'performed': False
        }
        self.payments[pid] = info
        self.scheduled.setdefault(timestamp + delay, []).append(pid)
        self.payment_counter += 1
        return pid

    def cancel_payment(self, timestamp: int, account_id: str, payment_id: str) -> bool:
        self._process_payments(timestamp)
        info = self.payments.get(payment_id)
        if not info or info['canceled'] or info['account_id'] != account_id or info['performed']:
            return False
        info['canceled'] = True
        return True
