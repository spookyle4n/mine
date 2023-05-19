import bitcoin_miner

def mine_bitcoin():
    while True:
        transaction = bitcoin_miner.generate_transaction()
        transaction_hash = bitcoin_miner.calculate_hash(transaction)
        
        if transaction_hash.startswith("0000"):  # Check if the hash meets the mining criteria
            return transaction_hash

mine_bitcoin()
