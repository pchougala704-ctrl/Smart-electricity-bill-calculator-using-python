# Smart Electricity Bill Calculator

A beginner-friendly Python console program that calculates electricity bills based on slab-wise unit rates. No external libraries, databases, files, or APIs — just pure Python.

---

## How to Run

```bash
python electricity_bill_calculator.py
```

Requires Python 3.x. No additional packages needed.

---

## Program Flow

```
START
  │
  ▼
main()
  │
  ├──► get_customer_details()
  │       │  Ask for Customer Name        (string input)
  │       │  Ask for Customer ID          (string input)
  │       │  Ask for Units Consumed       (float input)
  │       │  Validate: units must be ≥ 0  (loop until valid)
  │       └─ Return: name, customer_id, units
  │
  ├──► calculate_bill(units)
  │       │  Apply slab-wise energy rates (if/elif/else)
  │       │  Add fixed service charge     (Rs. 100)
  │       └─ Return: energy_charge, service_charge, total_bill
  │
  ├──► display_bill(name, customer_id, units,
  │                 energy_charge, service_charge, total_bill)
  │       │  Print formatted receipt to console
  │       └─ Shows: customer info, units, charges, total
  │
  └──► Ask user: "Calculate another bill? (yes/no)"
          │
          ├── yes → loop back to get_customer_details()
          └── no  → print goodbye and EXIT
```

---

## Slab Rate Structure

| Slab | Units Consumed  | Rate per Unit |
|------|-----------------|---------------|
| 1    | 0 – 100 units   | Rs. 2         |
| 2    | 101 – 200 units | Rs. 4         |
| 3    | 201 – 500 units | Rs. 6         |
| 4    | Above 500 units | Rs. 8         |

**Fixed Service Charge:** Rs. 100 (added to every bill)

Slabs are cumulative — each slab rate applies only to the units that fall within that slab's range.

**Example — 250 units:**
```
First 100 units  × Rs.2 = Rs. 200
Next  100 units  × Rs.4 = Rs. 400
Last   50 units  × Rs.6 = Rs. 300
                           -------
Energy Charge            = Rs. 900
Service Charge           = Rs. 100
                           -------
Total Bill               = Rs.1000
```

---

## Functions

| Function | Parameters | Returns | Purpose |
|---|---|---|---|
| `get_customer_details()` | none | `name, customer_id, units` | Collects and validates user input |
| `calculate_bill(units)` | `units` (float) | `energy_charge, service_charge, total_bill` | Applies slab rates and adds service charge |
| `display_bill(...)` | all bill details | nothing | Prints formatted receipt |
| `main()` | none | nothing | Orchestrates the program loop |

---

## Python Concepts Used

- **Variables** — storing name, ID, units, charges
- **Strings** — customer name, ID, formatted output
- **Integers & Floats** — units consumed, rates, charges
- **Functions** — `get_customer_details`, `calculate_bill`, `display_bill`, `main`
- **Parameters & Return values** — passing data between functions
- **Input & Type conversion** — `input()`, `float()`, `str.strip()`
- **Comparison operators** — `<=`, `<`, `==`, `!=`
- **if / elif / else** — slab selection and input validation
- **while loop** — re-prompting on invalid input, repeat billing
- **Formatted output** — f-strings with alignment (`:>8.2f`)
- **Constants** — slab limits and rates defined at the top

---

## Sample Output

```
==================================================
   SMART ELECTRICITY BILL CALCULATOR
==================================================
Please enter your details below.

Enter Customer Name     : John Doe
Enter Customer ID       : CUST-2024
Enter Units Consumed    : 250


==================================================
        ELECTRICITY BILL RECEIPT
==================================================
  Customer Name   : John Doe
  Customer ID     : CUST-2024
--------------------------------------------------
  Units Consumed  : 250.00 kWh
  Rate Applied    : Slab 1+2+3  (up to 500 units)
--------------------------------------------------
  Energy Charge   : Rs.   900.00
  Service Charge  : Rs.   100.00
--------------------------------------------------
  TOTAL AMOUNT    : Rs.  1000.00
==================================================
  Thank you for using Smart Bill Calculator!
==================================================
```

---

## File Structure

```
Smart-electricity-bill-calculator-using-python/
│
├── electricity_bill_calculator.py   ← main program
└── README.md                        ← this file
```
