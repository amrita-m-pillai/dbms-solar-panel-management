
import mysql.connector

# -----------------------------------
# DATABASE CONNECTION
# -----------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amrita2006@",
    database="solar_plant_db"
)

cursor = connection.cursor()

print("Connected to MySQL successfully!")


# -----------------------------------
# 1. VIEW SOLAR PLANTS
# -----------------------------------

def view_plants():

    cursor.execute("SELECT * FROM Solar_Plants")
    plants = cursor.fetchall()

    print("\n--- SOLAR PLANTS ---")

    for plant in plants:
        print("Plant ID:", plant[0])
        print("Plant Name:", plant[1])
        print("Location:", plant[2])
        print("Capacity:", plant[3], "MW")
        print("Commission Date:", plant[4])
        print()


# -----------------------------------
# 2. VIEW PLANT PERFORMANCE
# -----------------------------------

def view_performance():

    cursor.execute("SELECT * FROM Plant_Performance")
    performance = cursor.fetchall()

    print("\n--- PLANT PERFORMANCE ---")

    for row in performance:
        print("Plant ID:", row[0])
        print("Plant Name:", row[1])
        print("Total Energy:", row[2], "kWh")
        print("Average Efficiency:", row[3], "%")
        print()


# -----------------------------------
# 3. VIEW WEATHER DATA
# -----------------------------------

def view_weather():

    cursor.execute("""
        SELECT
            Solar_Plants.Plant_Name,
            Weather_Data.Weather_Date,
            Weather_Data.Temperature,
            Weather_Data.Irradiance,
            Weather_Data.Humidity
        FROM Weather_Data
        JOIN Solar_Plants
        ON Weather_Data.Plant_ID = Solar_Plants.Plant_ID
    """)

    weather = cursor.fetchall()

    print("\n--- WEATHER DATA ---")

    for row in weather:
        print("Plant:", row[0])
        print("Date:", row[1])
        print("Temperature:", row[2], "°C")
        print("Irradiance:", row[3])
        print("Humidity:", row[4], "%")
        print()


# -----------------------------------
# 4. VIEW POWER GENERATION
# -----------------------------------

def view_generation():

    cursor.execute("""
        SELECT
            Solar_Plants.Plant_Name,
            Power_Generation.Gen_Date,
            Power_Generation.Energy_kWh,
            Power_Generation.Peak_MW,
            Power_Generation.Efficiency
        FROM Power_Generation
        JOIN Solar_Plants
        ON Power_Generation.Plant_ID = Solar_Plants.Plant_ID
    """)

    generation = cursor.fetchall()

    print("\n--- POWER GENERATION ---")

    for row in generation:
        print("Plant:", row[0])
        print("Date:", row[1])
        print("Energy:", row[2], "kWh")
        print("Peak Power:", row[3], "MW")
        print("Efficiency:", row[4], "%")
        print()


# -----------------------------------
# 5. VIEW MAINTENANCE
# -----------------------------------

def view_maintenance():

    cursor.execute("""
        SELECT
            Employees.First_Name,
            Employees.Last_Name,
            Maintenance.Equip_Type,
            Maintenance.Equip_ID,
            Maintenance.Maint_Date,
            Maintenance.Remarks
        FROM Maintenance
        JOIN Employees
        ON Maintenance.Emp_ID = Employees.Emp_ID
    """)

    maintenance = cursor.fetchall()

    print("\n--- MAINTENANCE RECORDS ---")

    for row in maintenance:
        print("Employee:", row[0], row[1])
        print("Equipment:", row[2])
        print("Equipment ID:", row[3])
        print("Date:", row[4])
        print("Remarks:", row[5])
        print()


# -----------------------------------
# 6. VIEW FAULT LOGS
# -----------------------------------

def view_faults():

    cursor.execute("SELECT * FROM Fault_Logs")
    faults = cursor.fetchall()

    print("\n--- FAULT LOGS ---")

    for fault in faults:
        print("Fault ID:", fault[0])
        print("Equipment:", fault[1])
        print("Equipment ID:", fault[2])
        print("Fault:", fault[3])
        print("Severity:", fault[4])
        print("Date:", fault[5])
        print("Status:", fault[6])
        print()


# -----------------------------------
# 7. VIEW ALERTS
# -----------------------------------

def view_alerts():

    cursor.execute("""
        SELECT
            Solar_Plants.Plant_Name,
            Alerts.Alert_Type,
            Alerts.Message,
            Alerts.Alert_Date,
            Alerts.Status
        FROM Alerts
        JOIN Solar_Plants
        ON Alerts.Plant_ID = Solar_Plants.Plant_ID
    """)

    alerts = cursor.fetchall()

    print("\n--- ALERTS ---")

    for alert in alerts:
        print("Plant:", alert[0])
        print("Type:", alert[1])
        print("Message:", alert[2])
        print("Date:", alert[3])
        print("Status:", alert[4])
        print()


# -----------------------------------
# 8. VIEW INVENTORY
# -----------------------------------

def view_inventory():

    cursor.execute("SELECT * FROM Inventory")
    inventory = cursor.fetchall()

    print("\n--- INVENTORY ---")

    for item in inventory:
        print("Item ID:", item[0])
        print("Item:", item[1])
        print("Quantity:", item[2])
        print("Supplier:", item[3])
        print("Unit Cost:", item[4])
        print()


# -----------------------------------
# 9. VIEW EMPLOYEES
# -----------------------------------

def view_employees():

    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()

    print("\n--- EMPLOYEES ---")

    for employee in employees:
        print("Employee ID:", employee[0])
        print("Name:", employee[1], employee[2])
        print("Designation:", employee[3])
        print("Phone:", employee[4])
        print("Email:", employee[5])
        print("Skills:", employee[6])
        print()

# -----------------------------------
# 10. VIEW SOLAR PANELS
# -----------------------------------

def view_panels():

    cursor.execute("""
        SELECT
            Solar_Plants.Plant_Name,
            Solar_Panels.Panel_Number,
            Solar_Panels.Manufacturer,
            Solar_Panels.Model,
            Solar_Panels.Power_Rating,
            Solar_Panels.Status
        FROM Solar_Panels
        JOIN Solar_Plants
        ON Solar_Panels.Plant_ID = Solar_Plants.Plant_ID
    """)

    panels = cursor.fetchall()

    print("\n--- SOLAR PANELS ---")

    for panel in panels:
        print("Plant:", panel[0])
        print("Panel Number:", panel[1])
        print("Manufacturer:", panel[2])
        print("Model:", panel[3])
        print("Power Rating:", panel[4])
        print("Status:", panel[5])
        print()


# -----------------------------------
# 11. VIEW INVERTERS
# -----------------------------------

def view_inverters():

    cursor.execute("""
        SELECT
            Solar_Plants.Plant_Name,
            Inverters.Inverter_No,
            Inverters.Capacity_KW,
            Inverters.Efficiency,
            Inverters.Status
        FROM Inverters
        JOIN Solar_Plants
        ON Inverters.Plant_ID = Solar_Plants.Plant_ID
    """)

    inverters = cursor.fetchall()

    print("\n--- INVERTERS ---")

    for inverter in inverters:
        print("Plant:", inverter[0])
        print("Inverter Number:", inverter[1])
        print("Capacity:", inverter[2], "kW")
        print("Efficiency:", inverter[3], "%")
        print("Status:", inverter[4])
        print()

    # ==========================================
# ADD SOLAR PLANT
# ==========================================

def add_plant():

    print("\n--- ADD SOLAR PLANT ---")

    plant_name = input("Enter Plant Name: ")
    location = input("Enter Location: ")
    capacity = float(input("Enter Capacity (MW): "))
    commission_date = input("Enter Commission Date (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO Solar_Plants
        (Plant_Name, Location, Capacity_MW, Commission_Date)
        VALUES (%s, %s, %s, %s)
    """, (
        plant_name,
        location,
        capacity,
        commission_date
    ))

    connection.commit()

    print("Solar plant added successfully!")


# ==========================================
# ADD MAINTENANCE RECORD
# ==========================================

def add_maintenance():

    print("\n--- ADD MAINTENANCE RECORD ---")

    emp_id = int(input("Enter Employee ID: "))
    equip_type = input("Enter Equipment Type: ")
    equip_id = int(input("Enter Equipment ID: "))
    maint_date = input("Enter Maintenance Date (YYYY-MM-DD): ")
    remarks = input("Enter Remarks: ")

    cursor.execute("""
        INSERT INTO Maintenance
        (Emp_ID, Equip_Type, Equip_ID, Maint_Date, Remarks)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        emp_id,
        equip_type,
        equip_id,
        maint_date,
        remarks
    ))

    connection.commit()

    print("Maintenance record added successfully!")


# ==========================================
# ADD FAULT LOG
# ==========================================

def add_fault():

    print("\n--- ADD FAULT LOG ---")

    equip_type = input("Enter Equipment Type: ")
    equip_id = int(input("Enter Equipment ID: "))
    fault = input("Enter Fault Description: ")
    severity = input("Enter Severity (Low/Medium/High): ")
    fault_date = input("Enter Fault Date (YYYY-MM-DD): ")
    status = input("Enter Status (Pending/Resolved): ")

    cursor.execute("""
        INSERT INTO Fault_Logs
        (Equip_Type, Equip_ID, Fault, Severity, Fault_Date, Status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        equip_type,
        equip_id,
        fault,
        severity,
        fault_date,
        status
    ))

    connection.commit()

    print("Fault log added successfully!")


# ==========================================
# ADD INVENTORY ITEM
# ==========================================

def add_inventory():

    print("\n--- ADD INVENTORY ITEM ---")

    item = input("Enter Item Name: ")
    qty = int(input("Enter Quantity: "))
    supplier = input("Enter Supplier: ")
    unit_cost = float(input("Enter Unit Cost: "))

    cursor.execute("""
        INSERT INTO Inventory
        (Item, Qty, Supplier, Unit_Cost)
        VALUES (%s, %s, %s, %s)
    """, (
        item,
        qty,
        supplier,
        unit_cost
    ))

    connection.commit()

    print("Inventory item added successfully!")
# -----------------------------------
# MAIN MENU
# -----------------------------------

while True:

    print("\n====================================")
    print("     SOLAR PLANT MANAGEMENT SYSTEM")
    print("====================================")

    print("1. View Solar Plants")
    print("2. View Solar Panels")
    print("3. View Inverters")
    print("4. View Plant Performance")
    print("5. View Weather Data")
    print("6. View Power Generation")
    print("7. View Maintenance Records")
    print("8. View Fault Logs")
    print("9. View Alerts")
    print("10. View Inventory")
    print("11. View Employees")
    print("12. Add Solar Plant")
    print("13. Add Maintenance Record")
    print("14. Add Fault Log")
    print("15. Add Inventory Item")
    print("16. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_plants()

    elif choice == "2":
        view_panels()

    elif choice == "3":
        view_inverters()

    elif choice == "4":
        view_performance()

    elif choice == "5":
        view_weather()

    elif choice == "6":
        view_generation()

    elif choice == "7":
        view_maintenance()

    elif choice == "8":
        view_faults()

    elif choice == "9":
        view_alerts()

    elif choice == "10":
        view_inventory()

    elif choice == "11":
        view_employees()

    elif choice == "12":
        add_plant()

    elif choice == "13":
        add_maintenance()

    elif choice == "14":
        add_fault()

    elif choice == "15":
        add_inventory()

    elif choice == "16":
        break

    elif choice == "17":
        print("\nExiting Solar Plant Management System...")
        break

    else:
        print("\nInvalid choice. Please try again.")


# -----------------------------------
# CLOSE CONNECTION
# -----------------------------------

cursor.close()
connection.close()

print("Database connection closed.")

