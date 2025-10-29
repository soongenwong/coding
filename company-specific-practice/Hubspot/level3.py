from banking_system import BankingSystem

class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts = {}
        self.outgoing = {}
        self.payments = {}  # payment_id: dict
        self.scheduled_at = {}  # timestamp: [payment_id list]
        self.counter = 1
        self.last_processed_time = 0

    def _process_scheduled(self, timestamp):
        # Process all scheduled payments up to and including the current timestamp
        # that haven't been processed yet
        timestamps_to_process = sorted([ts for ts in self.scheduled_at.keys() 
                                        if self.last_processed_time < ts <= timestamp])
        
        for ts in timestamps_to_process:
            # Sort by payment ID (numeric order of creation)
            for pid in sorted(self.scheduled_at[ts], key=lambda x: int(x[7:])):
                p = self.payments[pid]
                if not p["canceled"] and not p["performed"]:
                    acc, amt = p["account"], p["amount"]
                    # Mark as performed regardless of whether it succeeds or is skipped
                    p["performed"] = True
                    # Only execute if sufficient funds
                    if acc in self.accounts and self.accounts[acc] >= amt:
                        self.accounts[acc] -= amt
                        if acc not in self.outgoing:
                            self.outgoing[acc] = 0
                        self.outgoing[acc] += amt
            del self.scheduled_at[ts]
        
        self.last_processed_time = timestamp

    def create_account(self, timestamp, account_id):
        self._process_scheduled(timestamp)
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        self.outgoing[account_id] = 0
        return True

    def deposit(self, timestamp, account_id, amount):
        self._process_scheduled(timestamp)
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def transfer(self, timestamp, src, tgt, amount):
        self._process_scheduled(timestamp)
        if src not in self.accounts or tgt not in self.accounts or src == tgt or self.accounts[src] < amount:
            return None
        self.accounts[src] -= amount
        self.accounts[tgt] += amount
        self.outgoing[src] += amount
        return self.accounts[src]

    def top_spenders(self, timestamp, n):
        self._process_scheduled(timestamp)
        res = sorted(self.outgoing.items(), key=lambda x: (-x[1], x[0]))
        return [f"{k}({v})" for k, v in res[:n]]

    def schedule_payment(self, timestamp, account_id, amount, delay):
        self._process_scheduled(timestamp)
        if account_id not in self.accounts:
            return None
        pid = f"payment{self.counter}"
        self.counter += 1
        p = {"account": account_id, "amount": amount,
             "scheduled_time": timestamp + delay,
             "canceled": False, "performed": False}
        self.payments[pid] = p
        self.scheduled_at.setdefault(timestamp + delay, []).append(pid)
        return pid

    def cancel_payment(self, timestamp, account_id, payment_id):
        self._process_scheduled(timestamp)
        p = self.payments.get(payment_id)
        if not p or p["canceled"] or p["performed"] or p["account"] != account_id:
            return False
        p["canceled"] = True
        return True