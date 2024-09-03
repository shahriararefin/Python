#!/bin/python3

import os
import sys


class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def total(self) -> int:
        return sum(item.price for item in self.items)

    def __len__(self):
        return len(self.items)


if __name__ == "__main__":
    fptr = open(os.environ.get('OUTPUT_PATH', 'output.txt'), 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next((item for item in items if item.name == name), None)
            if item is not None:
                cart.add(item)
            else:
                fptr.write(f"Item {name} not found\n")
        else:
            fptr.write(f"Unknown command {command}\n")
            
    fptr.close()
