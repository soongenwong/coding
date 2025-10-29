from banking_system import BankingSystem

class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts = {}
        self.outgoing = {}
        self.payments = {}  # payment_id: dict
        self.scheduled_at = {}  # timestamp: [payment_id list]
        self.counter = 1
        self.last_processed_time = 0
        # For Level 4
        self.balance_history = {}  # account_id: {timestamp: balance}
        self.account_exists_at = {}  # account_id: creation_timestamp
        self.account_merged_at = {}  # account_id: merge_timestamp (when it was merged away)
        self.merged_into = {}  # old_account: new_account (for tracking merges)

    def _record_balance(self, account_id, timestamp):
        """Record the current balance at this timestamp"""
        if account_id not in self.balance_history:
            self.balance_history[account_id] = {}
        self.balance_history[account_id][timestamp] = self.accounts.get(account_id, 0)

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
                        # Record balance after payment
                        self._record_balance(acc, ts)
            del self.scheduled_at[ts]
        
        self.last_processed_time = timestamp

    def create_account(self, timestamp, account_id):
        self._process_scheduled(timestamp)
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        self.outgoing[account_id] = 0
        self.account_exists_at[account_id] = timestamp
        # Clear merge tracking if this account name was previously merged
        if account_id in self.account_merged_at:
            del self.account_merged_at[account_id]
        if account_id in self.merged_into:
            del self.merged_into[account_id]
        self._record_balance(account_id, timestamp)
        return True

    def deposit(self, timestamp, account_id, amount):
        self._process_scheduled(timestamp)
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        self._record_balance(account_id, timestamp)
        return self.accounts[account_id]

    def transfer(self, timestamp, src, tgt, amount):
        self._process_scheduled(timestamp)
        if src not in self.accounts or tgt not in self.accounts or src == tgt or self.accounts[src] < amount:
            return None
        self.accounts[src] -= amount
        self.accounts[tgt] += amount
        self.outgoing[src] += amount
        self._record_balance(src, timestamp)
        self._record_balance(tgt, timestamp)
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

    def merge_accounts(self, timestamp, account_id_1, account_id_2):
        self._process_scheduled(timestamp)
        
        # Validation checks
        if account_id_1 == account_id_2:
            return False
        if account_id_1 not in self.accounts or account_id_2 not in self.accounts:
            return False
        
        # Merge balance
        self.accounts[account_id_1] += self.accounts[account_id_2]
        
        # Merge outgoing transactions
        self.outgoing[account_id_1] += self.outgoing[account_id_2]
        
        # Transfer all scheduled payments from account_id_2 to account_id_1
        for pid, payment in self.payments.items():
            if payment["account"] == account_id_2 and not payment["performed"] and not payment["canceled"]:
                payment["account"] = account_id_1
        
        # Merge balance history from account_id_2 into account_id_1
        # The target account (account_id_1) inherits all of account_id_2's history
        if account_id_2 in self.balance_history:
            if account_id_1 not in self.balance_history:
                self.balance_history[account_id_1] = {}
            
            # Copy account_id_2's balance history to account_id_1
            # These balances represent what account_id_2 had before the merge
            for ts, balance in self.balance_history[account_id_2].items():
                # Store account_id_2's historical balance under account_id_1
                # But we need to keep them separate somehow...
                # Actually, we should keep account_id_2's history as is for queries about account_id_2 before merge
                pass
        
        # Record that account_id_2 was merged into account_id_1 at this timestamp
        self.merged_into[account_id_2] = account_id_1
        self.account_merged_at[account_id_2] = timestamp
        
        # Record balance after merge for account_id_1
        self._record_balance(account_id_1, timestamp)
        
        # Remove account_id_2 from current state
        del self.accounts[account_id_2]
        del self.outgoing[account_id_2]
        
        return True

    def get_balance(self, timestamp, account_id, time_at):
        self._process_scheduled(timestamp)
        
        # If account was merged, check if the merge happened before or after time_at
        if account_id in self.account_merged_at:
            merge_time = self.account_merged_at[account_id]
            if time_at >= merge_time:
                # Account was already merged at time_at, so it doesn't exist
                return None
            # Otherwise, account still existed at time_at, get its balance from history
        
        # Check if the account ever existed
        if account_id not in self.account_exists_at:
            return None
        
        # Check if the account existed at time_at
        if self.account_exists_at[account_id] > time_at:
            return None
        
        # Find the balance at time_at from the account's own history
        if account_id in self.balance_history:
            history = self.balance_history[account_id]
            
            # If we have exact timestamp, return it
            if time_at in history:
                return history[time_at]
            
            # Otherwise, find the most recent balance at or before time_at
            relevant_times = sorted([ts for ts in history.keys() if ts <= time_at])
            if relevant_times:
                return history[relevant_times[-1]]
        
        # If no history found but account existed, return 0
        return 0