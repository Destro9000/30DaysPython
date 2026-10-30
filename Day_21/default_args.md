
# Understanding Default Arguments in Python

## 🔍 The Core Rule
In Python, **default argument values are evaluated exactly once**, at the time the function is **defined** — not each time the function is called.

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

When Python executes that `def`, it creates `items=[]` **once**, and reuses that same list object for every call that doesn't pass an `items` argument.

---

## 🧪 Example: What Happens with Mutable Defaults

```python
def add_item(item, items=[]):
    items.append(item)
    return items

a = add_item("apple")
b = add_item("banana")
print(a)  # ['apple', 'banana']
print(b)  # ['apple', 'banana']
print(a is b)  # True
```

**Why?**  
`a` and `b` both point to the **same list object**. You didn't create two separate lists; you just called the same function twice, and the second call appended to the list that was already mutated by the first call.

---

## ✅ The Standard Fix
Use a **immutable** default value like `None`, then create the mutable object inside the function:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

a = add_item("apple")
b = add_item("banana")
print(a)  # ['apple']
print(b)  # ['banana']
print(a is b)  # False
```

Now every call without an explicit `items` argument gets a **fresh list**.

---

## 🔁 Why This Matters for Your `PersonAccount`

### ❌ Bad: Mutable Default Arguments
```python
def __init__(self, firstname, lastname, incomes = set(), expenses = set()):
    self.incomes = incomes
    self.expenses = expenses
```

If you create two accounts:
```python
p1 = PersonAccount("Alice", "Smith")
p2 = PersonAccount("Bob", "Doe")
p1.incomes.add(100)
print(p2.incomes)  # {100} ← BUG! p2 accidentally has Alice's income
```

### ✅ Good: `None` + Fresh Object Inside
```python
def __init__(self, firstname, lastname, incomes=None, expenses=None):
    self.firstname = firstname
    self.lastname = lastname
    self.incomes = incomes if incomes is not None else set()
    self.expenses = expenses if expenses is not None else set()
```
Now `p1` and `p2` each get their own independent sets.

---

## ⚠️ When You *Actually* Want a Mutable Default
Sometimes defaults are intentionally mutable, but you must be deliberate:

```python
# Shared cache across all calls (valid, but rare)
def cache_result(key, cache={}):
    if key not in cache:
        cache[key] = compute_expensive_value(key)
    return cache[key]
```

This works because you **want** the same dictionary to be reused. Just document it clearly so future readers don't think it's a bug.

---

## 📌 Quick Mental Model

| Default Value         | Evaluated When? | Shared Across Calls? |
|-----------------------|-----------------|----------------------|
| `int`, `str`, `tuple`, `None` | Once at definition | No (immutable) |
| `list`, `dict`, `set` | Once at definition | **Yes** (mutable) |
| `None` (your fix)      | Once at definition | No (you create a new one inside) |

---

## 💡 Alternative Syntax (Python 3.8+)
If you're using `dataclasses`, `field(default_factory=...)` makes this pattern cleaner and more explicit:

```python
from dataclasses import dataclass, field

@dataclass
class PersonAccount:
    firstname: str
    lastname: str
    incomes: set = field(default_factory=set)
    expenses: set = field(default_factory=set)
```

Under the hood, `default_factory` does exactly what you manually wrote: creates a fresh set per instance.

---

## ✅ Bottom Line
- Mutable defaults (`list`, `dict`, `set`) are evaluated **once** and **shared** across all calls.
- Use `None` (immutable) as the default, then initialize the mutable object **inside** the function.
- If you intentionally want a shared object, make it obvious and comment it.

---

## 📊 Summary of this Conversation

| Topic | What We Learned |
|-------|-----------------|
| Optional input | `input().strip()` + `if not raw:` lets users skip input by pressing Enter |
| Class instance in a function | Fully supported; used for factories, caching, and encapsulation |
| `while True` vs single run | `while True` + `break` on option 6 keeps the menu open; remove the loop for one-shot execution |
| Mutable defaults | `set()` as a default shares state across instances; use `None` + `set()` inside `__init__` |
| Input validation | Wrap `int(input(...))` in `try/except ValueError` to avoid crashes |
| Cleaner menu | Turn `handle_op` into an instance method (`self`) for better OOP design |

---