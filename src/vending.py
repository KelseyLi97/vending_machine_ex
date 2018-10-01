#!/usr/bin/env python

import json
from pathlib import Path
import sys

inventory_json = open(sys.argv[1]).read()
transactions_json = open(sys.argv[2]).read()
#inventory_json = '{"Cool Ranch Doritos": {"quantity": 2,"price": 1.3}}'
#transactions_json = '[{"name": "Cool Ranch Doritos","funds": [25,5,100]}, {"name": "Cool Ranch Doritos","funds": [25,25,100]}]'

#load json
inventory = json.loads(inventory_json);
transactions = json.loads(transactions_json);

result = {
    "product_delivered": [],
    "change": []
}
rlist = []

#get inventory info
for inv in inventory:
    print("Inventory：" + inv)
    quantity = inventory[inv]["quantity"]
    price = inventory[inv]["price"]

#get transactions info
for trans in transactions:
    print("Transactions:" + str(trans))
    #Calculate the sum of coins
    trans_sum = sum(x for x in trans["funds"])/100
    #Product can be delivered if sum of coins > price and there is stock
    if trans_sum >= price and quantity > 0:
        output = True
        quantity -= 1
        diff = trans_sum - price
        change = []
        while diff > 0:
            #in case 5 cent is needed
            if diff < 0.09:
                change.append(5)
                break
            #change is divided into 10 cents
            change.append(10)
            diff -= 0.1
    #If not delivered the funds will be returned
    else:
        output = False
        change = trans["funds"]
    result["product_delivered"] = output
    result["change"] = change
    rlist.append(result.copy())

print("Output:" + str(rlist))
#save to json file
with open("output.json","w+") as outfile:
    json.dump(rlist, outfile)
