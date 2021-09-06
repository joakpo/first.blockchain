import hashlib

class JCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        

        self.block_data = "-".join(transaction_list)+"- \n"+previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "1 tranfers 10JCoins to 3"
t2 = "8 tranfers 59JCoins to 5"
t3 = "1 tranfers 2JCoins to 8"
t4 = "5 tranfers 107JCoins to 4"
t5 = "4 tranfers 3.1JCoins to 1"
t6 = "3 tranfers 10JCoins to 1"


initial_block = JCoinBlock("Initializing ", [t1 , t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = JCoinBlock(initial_block.block_hash, [t3 , t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = JCoinBlock(second_block.block_hash, [t5 , t6])

print(third_block.block_data)
print(third_block.block_hash)

