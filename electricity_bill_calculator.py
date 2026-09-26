# ============================================================
#   Smart Electricity Bill Calculator
#   A beginner-friendly Python console program
# ============================================================

# ---------- Constants ----------
SERVICE_CHARGE = 100.0      # Fixed service charge in Rupees

# Slab rate boundaries
SLAB_1_LIMIT = 100          # 0 – 100  units  → Rs.2 per unit
SLAB_2_LIMIT = 200          # 101 – 200 units → Rs.4 per unit
SLAB_3_LIMIT = 500          # 201 – 500 units → Rs.6 per unit
                             # Above 500 units → Rs.8 per unit

RATE_SLAB_1 = 2.0
RATE_SLAB_2 = 4.0
RATE_SLAB_3 = 6.0
RATE_SLAB_4 = 8.0


# ============================================================
# FUNCTION 1 — Collect and validate customer details
# ============================================================
def get_customer_details():
    """
    Ask the user for their name, customer ID, and units consumed.
    Validates that units consumed is a non-negative number.
    Returns a tuple: (name, customer_id, units)
    """

    print("\n" + "=" * 50)
    print("   SMART ELECTRICITY BILL CALCULATOR")
    print("=" * 50)
    print("Please enter your details below.\n")

    # --- Customer Name ---
    name = input("Enter Customer Name     : ").strip()
    while name == "":
        print("  [!] Name cannot be empty. Please try again.")
        name = input("Enter Customer Name     : ").strip()

    # --- Customer ID ---
    customer_id = input("Enter Customer ID       : ").strip()
    while customer_id == "":
        print("  [!] Customer ID cannot be empty. Please try again.")
        customer_id = input("Enter Customer ID       : ").strip()

    # --- Units Consumed (with validation) ---
    units = -1.0
    while units < 0:
        units_input = input("Enter Units Consumed    : ").strip()

        # Try converting the input to a float
        try:
            units = float(units_input)   # type conversion: string → float
        except ValueError:
            print("  [!] Invalid input. Please enter a numeric value.")
            units = -1.0   # reset so the loop continues
            continue

        if units < 0:
            print("  [!] Units cannot be negative. Please enter a valid value.")

    return name, customer_id, units   # return values


# ============================================================
# FUNCTION 2 — Calculate the electricity bill
# ============================================================
def calculate_bill(units):
    """
    Calculate the energy charge based on slab rates and
    add the fixed service charge.

    Slab structure:
        0  – 100  units : Rs.2 per unit
        101 – 200 units : Rs.4 per unit
        201 – 500 units : Rs.6 per unit
        Above 500 units : Rs.8 per unit

    Fixed service charge: Rs.100

    Parameters : units (float) — units consumed
    Returns    : (energy_charge, service_charge, total_bill) — all floats
    """

    energy_charge = 0.0   # will accumulate the slab-wise charge

    # ---- Slab 1 : 0 to 100 units ----
    if units <= SLAB_1_LIMIT:
        energy_charge = units * RATE_SLAB_1

    # ---- Slab 2 : 101 to 200 units ----
    elif units <= SLAB_2_LIMIT:
        energy_charge = (SLAB_1_LIMIT * RATE_SLAB_1) + \
                        ((units - SLAB_1_LIMIT) * RATE_SLAB_2)

    # ---- Slab 3 : 201 to 500 units ----
    elif units <= SLAB_3_LIMIT:
        energy_charge = (SLAB_1_LIMIT * RATE_SLAB_1) + \
                        ((SLAB_2_LIMIT - SLAB_1_LIMIT) * RATE_SLAB_2) + \
                        ((units - SLAB_2_LIMIT) * RATE_SLAB_3)

    # ---- Slab 4 : above 500 units ----
    else:
        energy_charge = (SLAB_1_LIMIT * RATE_SLAB_1) + \
                        ((SLAB_2_LIMIT - SLAB_1_LIMIT) * RATE_SLAB_2) + \
                        ((SLAB_3_LIMIT - SLAB_2_LIMIT) * RATE_SLAB_3) + \
                        ((units - SLAB_3_LIMIT) * RATE_SLAB_4)

    total_bill = energy_charge + SERVICE_CHARGE   # final amount

    return energy_charge, SERVICE_CHARGE, total_bill


# ============================================================
# FUNCTION 3 — Display a clean formatted bill
# ============================================================
def display_bill(name, customer_id, units, energy_charge, service_charge, total_bill):
    """
    Print a neatly formatted electricity bill to the console.

    Parameters:
        name           (str)   — customer name
        customer_id    (str)   — customer ID
        units          (float) — units consumed
        energy_charge  (float) — calculated energy charge
        service_charge (float) — fixed service charge
        total_bill     (float) — total amount payable
    """

    # Determine which slab was applied (for display)
    if units <= SLAB_1_LIMIT:
        slab_info = "Slab 1  (0 – 100 units @ Rs.2/unit)"
    elif units <= SLAB_2_LIMIT:
        slab_info = "Slab 1+2  (up to 200 units)"
    elif units <= SLAB_3_LIMIT:
        slab_info = "Slab 1+2+3  (up to 500 units)"
    else:
        slab_info = "Slab 1+2+3+4  (above 500 units)"

    print("\n")
    print("=" * 50)
    print("        ELECTRICITY BILL RECEIPT")
    print("=" * 50)

    # Customer details
    print(f"  Customer Name   : {name}")
    print(f"  Customer ID     : {customer_id}")
    print("-" * 50)

    # Usage details
    print(f"  Units Consumed  : {units:.2f} kWh")
    print(f"  Rate Applied    : {slab_info}")
    print("-" * 50)

    # Charges breakdown
    print(f"  Energy Charge   : Rs. {energy_charge:>8.2f}")
    print(f"  Service Charge  : Rs. {service_charge:>8.2f}")
    print("-" * 50)

    # Total
    print(f"  TOTAL AMOUNT    : Rs. {total_bill:>8.2f}")
    print("=" * 50)
    print("  Thank you for using Smart Bill Calculator!")
    print("=" * 50)


# ============================================================
# MAIN — Program entry point
# ============================================================
def main():
    """
    Orchestrates the program flow:
      1. Get customer details
      2. Calculate the bill
      3. Display the bill
      4. Ask if the user wants to calculate another bill
    """

    while True:
        # Step 1 — collect inputs
        name, customer_id, units = get_customer_details()

        # Step 2 — calculate charges
        energy_charge, service_charge, total_bill = calculate_bill(units)

        # Step 3 — show the bill
        display_bill(name, customer_id, units,
                     energy_charge, service_charge, total_bill)

        # Step 4 — ask to continue
        print()
        again = input("Calculate another bill? (yes / no) : ").strip().lower()
        if again != "yes" and again != "y":
            print("\nGoodbye! Have a nice day.\n")
            break


# Run the program
if __name__ == "__main__":
    main()
