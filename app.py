from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amrita2006@",
        database="solar_plant_db"
    )


# ==========================================
# HOME / DASHBOARD
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# SOLAR PLANTS
# ==========================================

@app.route("/plants")
def plants():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            Plant_ID,
            Plant_Name,
            Location,
            Capacity_MW,
            Commission_Date
        FROM Solar_Plants
    """)

    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "plants.html",
        plants=plants
    )


# ==========================================
# SOLAR PANELS
# ==========================================

@app.route("/panels")
def panels():

    connection = get_connection()
    cursor = connection.cursor()

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

    cursor.close()
    connection.close()

    return render_template(
        "panels.html",
        panels=panels
    )


# ==========================================
# INVERTERS
# ==========================================

@app.route("/inverters")
def inverters():

    connection = get_connection()
    cursor = connection.cursor()

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

    cursor.close()
    connection.close()

    return render_template(
        "inverters.html",
        inverters=inverters
    )


# ==========================================
# PLANT PERFORMANCE
# ==========================================

@app.route("/performance")
def performance():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            Plant_ID,
            Plant_Name,
            Total_Energy_kWh,
            Average_Efficiency
        FROM Plant_Performance
    """)

    performance = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "performance.html",
        performance=performance
    )


# ==========================================
# WEATHER DATA
# ==========================================

@app.route("/weather")
def weather():

    connection = get_connection()
    cursor = connection.cursor()

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
        ORDER BY Weather_Data.Weather_Date DESC
    """)

    weather = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "weather.html",
        weather=weather
    )


# ==========================================
# POWER GENERATION
# ==========================================

@app.route("/generation")
def generation():

    connection = get_connection()
    cursor = connection.cursor()

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
        ORDER BY Power_Generation.Gen_Date DESC
    """)

    generation = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "generation.html",
        generation=generation
    )


# ==========================================
# MAINTENANCE
# ==========================================

@app.route("/maintenance")
def maintenance():

    connection = get_connection()
    cursor = connection.cursor()

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
        ORDER BY Maintenance.Maint_Date DESC
    """)

    maintenance = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "maintenance.html",
        maintenance=maintenance
    )


# ==========================================
# FAULT LOGS
# ==========================================

@app.route("/faults")
def faults():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            Fault_ID,
            Equip_Type,
            Equip_ID,
            Fault,
            Severity,
            Fault_Date,
            Status
        FROM Fault_Logs
        ORDER BY Fault_Date DESC
    """)

    faults = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "faults.html",
        faults=faults
    )


# ==========================================
# ALERTS
# ==========================================

@app.route("/alerts")
def alerts():

    connection = get_connection()
    cursor = connection.cursor()

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
        ORDER BY Alerts.Alert_Date DESC
    """)

    alerts = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "alerts.html",
        alerts=alerts
    )


# ==========================================
# INVENTORY
# ==========================================

@app.route("/inventory")
def inventory():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            Item_ID,
            Item,
            Qty,
            Supplier,
            Unit_Cost
        FROM Inventory
    """)

    inventory = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "inventory.html",
        inventory=inventory
    )


# ==========================================
# EMPLOYEES
# ==========================================

@app.route("/employees")
def employees():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            Emp_ID,
            First_Name,
            Last_Name,
            Designation,
            Phone,
            Email,
            Skills
        FROM Employees
    """)

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "employees.html",
        employees=employees
    )


# ==========================================
# ADD SOLAR PLANT
# ==========================================

@app.route("/add-plant", methods=["GET", "POST"])
def add_plant():

    if request.method == "POST":

        plant_name = request.form["plant_name"]
        location = request.form["location"]
        capacity = request.form["capacity"]
        commission_date = request.form["commission_date"]

        connection = get_connection()
        cursor = connection.cursor()

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

        cursor.close()
        connection.close()

        return redirect(url_for("plants"))

    return render_template("add_plant.html")

# ==========================================
# ADD MAINTENANCE RECORD
# ==========================================

@app.route("/add-maintenance", methods=["GET", "POST"])
def add_maintenance():

    if request.method == "POST":

        emp_id = request.form["emp_id"]
        equip_type = request.form["equip_type"]
        equip_id = request.form["equip_id"]
        maint_date = request.form["maint_date"]
        remarks = request.form["remarks"]

        connection = get_connection()
        cursor = connection.cursor()

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

        cursor.close()
        connection.close()

        return redirect(url_for("maintenance"))

    return render_template("add_maintenance.html")


# ==========================================
# ADD FAULT LOG
# ==========================================

@app.route("/add-fault", methods=["GET", "POST"])
def add_fault():

    if request.method == "POST":

        equip_type = request.form["equip_type"]
        equip_id = request.form["equip_id"]
        fault = request.form["fault"]
        severity = request.form["severity"]
        fault_date = request.form["fault_date"]
        status = request.form["status"]

        connection = get_connection()
        cursor = connection.cursor()

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

        cursor.close()
        connection.close()

        return redirect(url_for("faults"))

    return render_template("add_fault.html")


# ==========================================
# ADD INVENTORY ITEM
# ==========================================

@app.route("/add-inventory", methods=["GET", "POST"])
def add_inventory():

    if request.method == "POST":

        item = request.form["item"]
        qty = request.form["qty"]
        supplier = request.form["supplier"]
        unit_cost = request.form["unit_cost"]

        connection = get_connection()
        cursor = connection.cursor()

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

        cursor.close()
        connection.close()

        return redirect(url_for("inventory"))

    return render_template("add_inventory.html")
# ==========================================
# RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)