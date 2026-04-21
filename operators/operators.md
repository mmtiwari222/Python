# Python Operators 🐍

## What are Operators?

**Operators** in Python are special symbols or keywords that perform operations on values and variables. Think of them as the building blocks for any logic or calculation in your code.

---

## 🔢 Arithmetic Operators

These are used for mathematical operations.

| Operator | Name | Example |
| :---: | :---: | :---: |
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulus | `a % b` |
| `**` | Exponentiation | `a ** b` |
| `//` | Floor Division | `a // b` |

---

## ⚖️ Comparison Operators

These operators compare two values and return a `Boolean` result (`True` or `False`).

| Operator | Name | Example |
| :---: | :---: | :---: |
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

---

## 🎯 Assignment Operators

Used to assign values to variables.

| Operator | Example | Equivalent to |
| :---: | :---: | :---: |
| `=` | `x = 5` | - |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 5` | `x = x ** 5` |
| `//=` | `x //= 5` | `x = x // 5` |

---

## 🧠 Logical Operators

These combine conditional statements.

| Operator | Description | Example |
| :---: | :--- | :--- |
| `and` | Returns `True` if both statements are `True`. | `x > 5 and x < 10` |
| `or` | Returns `True` if one of the statements is `True`. | `x > 5 or x < 4` |
| `not` | Reverses the result. | `not(x > 5 and x < 10)` |

---

## 🔍 Identity Operators

Used to check if two variables refer to the **same object in memory**.

| Operator | Description | Example |
| :---: | :--- | :--- |
| `is` | Returns `True` if both variables are the same object. | `x is y` |
| `is not` | Returns `True` if both variables are not the same object. | `x is not y` |

---

## 🙋 Membership Operators

Used to test if a value is present in a sequence (like a string, list, or tuple).

| Operator | Description | Example |
| :---: | :--- | :--- |
| `in` | Returns `True` if a value is found in the sequence. | `'a' in 'apple'` |
| `not in` | Returns `True` if a value is not found in the sequence. | `'b' not in 'apple'` |

---

## ⚙️ Bitwise Operators

These operators perform operations on integer operands at the binary level.

| Operator | Name | Description |
| :---: | :--- | :--- |
| `&` | AND | Sets each bit to 1 if both bits are 1. |
| `\|` | OR | Sets each bit to 1 if at least one of the bits is 1. |
| `^` | XOR | Sets each bit to 1 if only one of the bits is 1. |
| `~` | NOT | Inverts all the bits. |
| `<<` | Left shift | Shifts bits to the left. |
| `>>` | Right shift | Shifts bits to the right. |