
import mysql.connector
import random
from datetime import date, timedelta


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
# SELECT PLANT
# -----------------------------------

plant_id = int(input("Enter Plant ID (1, 2 or 3): "))


# -----------------------------------
# PLANT CAPACITY
# -----------------------------------

plant_capacities = {
    1: 5.0,
    2: 10.0,
    3: 7.5
}

if plant_id not in plant_capacities:
    print("Invalid Plant ID.")
    cursor.close()
    connection.close()
    exit()

capacity_mw = plant_capacities[plant_id]


# -----------------------------------
# GENERATE DATA FOR 5 DAYS
# -----------------------------------

start_date = date.today() - timedelta(days=4)

for i in range(5):

    simulation_date = start_date + timedelta(days=i)

    # -----------------------------------
    # GENERATE WEATHER VALUES
    # -----------------------------------

    temperature = round(random.uniform(25, 38), 2)
    irradiance = round(random.uniform(400, 1000), 2)
    humidity = round(random.uniform(40, 85), 2)


    # -----------------------------------
    # CALCULATE POWER GENERATION
    # -----------------------------------

    energy = round(
        (irradiance / 1000) * capacity_mw * 1000 * 0.85,
        2
    )

    peak_power = round(
        (irradiance / 1000) * capacity_mw,
        2
    )

    efficiency = round(random.uniform(80, 95), 2)


    # -----------------------------------
    # CHECK WEATHER DATA
    # -----------------------------------

    cursor.execute("""
        SELECT Weather_ID
        FROM Weather_Data
        WHERE Plant_ID = %s AND Weather_Date = %s
    """, (plant_id, simulation_date))

    existing_weather = cursor.fetchall()

    if existing_weather:

        print(
            simulation_date,
            "- Weather data already exists."
        )

    else:

        cursor.execute("""
            INSERT INTO Weather_Data
            (Plant_ID, Weather_Date, Temperature, Irradiance, Humidity)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            plant_id,
            simulation_date,
            temperature,
            irradiance,
            humidity
        ))

        print(
            simulation_date,
            "- Weather data inserted."
        )


    # -----------------------------------
    # CHECK POWER GENERATION
    # -----------------------------------

    cursor.execute("""
        SELECT Gen_ID
        FROM Power_Generation
        WHERE Plant_ID = %s AND Gen_Date = %s
    """, (plant_id, simulation_date))

    existing_generation = cursor.fetchall()

    if existing_generation:

        print(
            simulation_date,
            "- Power generation data already exists."
        )

    else:

        cursor.execute("""
            INSERT INTO Power_Generation
            (Plant_ID, Gen_Date, Energy_kWh, Peak_MW, Efficiency)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            plant_id,
            simulation_date,
            energy,
            peak_power,
            efficiency
        ))

        print(
            simulation_date,
            "- Power generation data inserted."
        )


# -----------------------------------
# SAVE CHANGES
# -----------------------------------

connection.commit()


# -----------------------------------
# CLOSE CONNECTION
# -----------------------------------

cursor.close()
connection.close()

print("\nSimulation completed successfully!")
print("Database connection closed.")

