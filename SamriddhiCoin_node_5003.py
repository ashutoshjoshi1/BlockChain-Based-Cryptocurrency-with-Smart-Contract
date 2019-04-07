
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4	
from urllib.parse import urlparse

# Making a Blockchain
class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.createblock(proof = 1, previoushash = '0')
        self.nodes = set()
    
    def createblock(self, proof, previoushash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previoushash': previoushash,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block

    def getpreviousblock(self):
        return self.chain[-1]

    def proofofwork(self, previousblockproof):
        newproof = 1
        checkproof = False
        while checkproof is False:
            hash_operation = hashlib.sha256(str(newproof**2 - previousblockproof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                checkproof = True
            else:
                newproof += 1
        return newproof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def ischainvalid(self, chain):
        previousblock = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previoushash'] != self.hash(previousblock):
                return False
            previousblockproof = previousblock['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previousblockproof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previousblock = block
            block_index += 1
        return True
    
    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})
        previousblock = self.getpreviousblock()
        return previousblock['index'] + 1
    
    def add_node(self, address):	#address: address of node
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
# Very Quickly it replaces to the Genuine blockchain (longest)  
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.ischainvalid(chain):
                    max_length = length
                    longest_chain = chain
        # Converting Fake/Non-updated Chain to Longest Chain            
        if longest_chain:
            self.chain = longest_chain
            return True
        return False



# Mining our Blockchain-----------------------!!

# Creating a Web App
app = Flask(__name__)

# generating an address for the node on Port 5000 or 01-03...
#uuid provides unique id with - in b/w
node_address = str(uuid4()).replace('-', '')

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previousblock = blockchain.getpreviousblock()
    previousblockproof = previousblock['proof']
    proof = blockchain.proofofwork(previousblockproof)
    previoushash = blockchain.hash(previousblock)
    blockchain.add_transaction(sender = node_address, receiver = 'Aditya', amount = 1)
    block = blockchain.createblock(proof, previoushash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previoushash': block['previoushash'],
                'transactions': block['transactions']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.ischainvalid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'We have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200

#Putting data to JSON file
#Taking data from JSON file

# Adding a new transaction to the Blockchain
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
    json = request.get_json()   #Getting a json file
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing', 400
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message': f'This transaction will be added to Block {index}'}
    return jsonify(response), 201



# Decentralizing our Blockchain-----------------------!!

# Connecting new nodes
@app.route('/connect_node', methods = ['POST'])
def connect_node():
    json = request.get_json() #json file contains all the nodes of decentralized connections including the one we are connecting now
    nodes = json.get('nodes')
    if nodes is None:
        return "No node", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'All the nodes are now connected. The Samriddhi Coin Blockchain now contains the following nodes:',
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

# Replacing the chain by the longest chain if needed
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The nodes had different chains so the chain was replaced by the longest one.',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'All good. The chain is the largest one.',
                    'actual_chain': blockchain.chain}
    return jsonify(response), 200

# Finally Running the app
app.run(host = '0.0.0.0', port = 5003)

#200,201: Good Response
#400,401: BAD Response
