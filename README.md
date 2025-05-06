# Thoughtful Automation

This is a solution to the **FDE Technical Screen** challenge for Thoughtful.

![Challenge](https://thoughtfulautomation.notion.site/FDE-Technical-Screen-12af43a78fa480af8d97c2fc9478cb18)

## 🚀 Objective

Write a function for a robotic arm to sort packages according to their **volume** and **mass** into the correct stack.

## 📦 Sorting Rules

- A package is **bulky** if:
  - Volume (Width × Height × Length) ≥ 1,000,000 cm³  
  **or**
  - Any dimension ≥ 150 cm

- A package is **heavy** if:
  - Mass ≥ 20 kg

### Dispatch Stacks

| Condition               | Stack      |
|-------------------------|------------|
| Not bulky and not heavy | STANDARD   |
| Bulky **or** heavy      | SPECIAL    |
| Bulky **and** heavy     | REJECTED   |

## 🧠 Implementation

The core function is:

```python
def sort(width, height, length, mass) -> str:
    ...
