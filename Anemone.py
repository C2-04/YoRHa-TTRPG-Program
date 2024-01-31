import pickle
import math
import random

def materialShop():
    with open('shop/materialList.shop', 'rb') as infile:
        items = pickle.load(infile)
        infile.close()
    itemList = items.keys()
    for element in itemList:
        print(element + ': ' + str(items[element]) + ' G')
    selectedItem = None
    while selectedItem != 'quit':
        selectedItem = input('Enter the item you wish to buy: ')
        if selectedItem == 'quit':
            break
        with open('inventory.data', 'rb') as infile:
            inventory = pickle.load(infile)
            infile.close()
        howMany = int(input('How many? '))
        if inventory['Gold'] >= (items[selectedItem]*howMany):
            inventory['Gold'] = inventory['Gold'] - (items[selectedItem]*howMany)
            try:
                inventory[selectedItem] = inventory[selectedItem] + howMany
            except KeyError:
                inventory[selectedItem] = howMany
            print('Operation complete. You have', inventory['Gold'], 'gold remaining.')
        else:
            print('Not enough gold!')
        with open('inventory.data', 'wb') as outfile:
            pickle.dump(inventory, outfile)
            outfile.close()

def giveGold():
    toGive = int(input('Enter the amount of gold you wish to give: '))
    with open('inventory.data', 'rb') as infile:
        items = pickle.load(infile)
        infile.close()
    items['Gold'] = items['Gold'] + toGive
    print('Gold:', items['Gold'])
    with open('inventory.data', 'wb') as outfile:
        pickle.dump(items, outfile)
        outfile.close()

def takeInventory():
    with open('inventory.data', 'rb') as infile:
        items = pickle.load(infile)
        infile.close()
    itemList = items.keys()
    for element in itemList:
        print(element + ': ' + str(items[element]))
def main():
    mode = None
    while mode != 'quit':
        mode = input('What do you need? shop, stock, give, quit: ')
        if mode == 'shop':
            materialShop()
        if mode == 'stock':
            takeInventory()
        if mode == 'give':
            giveGold()
main()