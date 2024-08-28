#!/usr/bin/env python3
import ipdb

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, age=9):
        self.age = age
        print(f"Age: {self.age}")

person = Person()
print(person.age)

ipdb.set_trace()