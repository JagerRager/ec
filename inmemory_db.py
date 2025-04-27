class TransactionError(Exception):
    pass

class InMemoryDB:
    def __init__(self):
        self.database = {}
        self.transaction = None

    def get(self, key):
        if self.transaction is not None and key in self.transaction:
            return self.transaction[key]
        return self.database.get(key)

    def put(self, key, value):
        if self.transaction is None:
            raise TransactionError("No active transaction. Begin a transaction first.")
        self.transaction[key] = value

    def begin_transaction(self):
        if self.transaction is not None:
            raise TransactionError("A transaction is already active.")
        self.transaction = {}

    def commit(self):
        if self.transaction is None:
            raise TransactionError("No active transaction to commit.")
        for key, value in self.transaction.items():
            self.database[key] = value
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            raise TransactionError("No active transaction to rollback.")
        self.transaction = None

if __name__ == "__main__":
    db = InMemoryDB()

    # Test 1: .get() when key doesn't exist
    print('\nTest 1: Get key that does not exist')
    print('\tExpected: None')
    print(f'\tActual: {db.get('A')}\n')

    # Test 2: .put() without a transaction (should raise error)
    print('Test 2: Put without an active transaction')
    try:
        db.put('A', 1)
    except TransactionError as e:
        print(f'\tExpected Error: {e}\n')

    # Test 3: .begin_transaction()
    print('Test 3: Begin transaction')
    db.begin_transaction()
    print('\tTransaction started successfully.\n')

    # Test 4: .put() inside transaction
    print('Test 4: Put A = 1 inside transaction')
    db.put('A', 1)
    print('\tPut successful (inside transaction).\n')

    # Test 5: .get() inside transaction (should see uncommitted change)
    print('Test 5: Get key A inside transaction (should see A = 1)')
    print('\tExpected: 1')
    print(f'\tActual: {db.get('A')}\n')

    # Test 6: update key A = 12 inside transaction
    print("Test 6: Update key A to 12 inside transaction")
    db.put('A', 12)
    print('\tUpdate successful (A = 12 now inside transaction).\n')

    # Test 7: .commit()
    print("Test 7: Commit transaction")
    db.commit()
    print('\tTransaction committed successfully.')

    # Test 8: .get() after commit
    print('Test 8: Get key A after commit')
    print('\tExpected: 12')
    print(f'\tActual: {db.get('A')}\n')

    # Test 9: .commit() without transaction (should raise error)
    print('Test 9: Commit with no active transaction')
    try:
        db.commit()
    except TransactionError as e:
        print(f'\tExpected Error: {e}\n')

    # Test 10: .rollback() without transaction (should raise error)
    print('Test 10: Rollback with no active transaction')
    try:
        db.rollback()
    except TransactionError as e:
        print(f'\tExpected Error: {e}\n')

    # Test 11: .begin_transaction() and .rollback()
    print('Test 11: Begin transaction, put B = 2, then rollback')
    db.begin_transaction()
    db.put('B', 2)
    print(f'\tCheck current value of B before rollback with .get() => {db.get('B')}')
    db.rollback()
    print('\tRolled back completed.')
    print('\tExpected: None')
    print(f'\tActual: {db.get('B')}\n')


    # Big Test: Full workflow
    print('Big Test: Complex Transaction Workflow')
    db.begin_transaction()
    db.put('X', 100)
    db.put('Y', 200)
    print(f'\tInside Transaction: X = {db.get('X')}, Y = {db.get('Y')}')

    db.commit()
    print(f'\tAfter commit: X = {db.get('X')}, Y = {db.get('Y')}')


    db.begin_transaction()
    db.put('X', 300)
    db.put('Z', 400)
    print(f'\tInside New Transaction: X = {db.get('X')}, Z = {db.get('Z')}')

    db.rollback()
    print(f'\tAfter rollback: X = {db.get('X')}, Z = {db.get('Z')}')

    print('\tExpected: X = 100, Z = None')
    print(f'\tActual: X = {db.get('X')}, Z = {db.get('Z')}\n')
