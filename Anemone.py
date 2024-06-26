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
        with open('savedata/inventory.data', 'rb') as infile:
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
        with open('savedata/inventory.data', 'wb') as outfile:
            pickle.dump(inventory, outfile)
            outfile.close()
def addItem(item):
    with open('savedata/inventory.data', 'rb') as infile:
        inventory = pickle.load(infile)
        infile.close()
    howMany = 1
    try:
        inventory[item] = inventory[item] + howMany
    except KeyError:
        inventory[item] = howMany
    with open('savedata/inventory.data', 'wb') as outfile:
        pickle.dump(inventory, outfile)
        outfile.close()
def eraseItem(item):
    with open('savedata/inventory.data', 'rb') as infile:
        inventory = pickle.load(infile)
        infile.close()
    inventory[item] = 0
    with open('savedata/inventory.data', 'wb') as outfile:
        pickle.dump(inventory, outfile)
        outfile.close()
def giveGold(toGive):
    with open('savedata/inventory.data', 'rb') as infile:
        items = pickle.load(infile)
        infile.close()
    items['Gold'] = items['Gold'] + toGive
    print('Gold:', items['Gold'])
    with open('savedata/inventory.data', 'wb') as outfile:
        pickle.dump(items, outfile)
        outfile.close()
def takeInventory():
    with open('savedata/inventory.data', 'rb') as infile:
        items = pickle.load(infile)
        infile.close()
    itemList = items.keys()
    for element in itemList:
        print(element + ': ' + str(items[element]))
def main():
    mode = None
    while mode != 'quit':
        mode = input('What do you need? shop, stock, give, trash, quit: ')
        if mode == 'shop':
            materialShop()
        if mode == 'stock':
            takeInventory()
        if mode == 'give':
            giveGold(int(input('Enter the amount of gold you wish to give: ')))
        if mode == 'trash':
            eraseItem(input('Enter the item stack you wish to trash: '))
if __name__ == "__main__":
    main()