import os
import time
import random
from datetime import datetime
import psycopg2

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "postgres"),
    "database": os.getenv("DB_NAME", "weather_db"),
    "user": os.getenv("DB_USER", "weather_user"),
    "password": os.getenv("DB_PASSWORD", "weather_pass"),
    "port": 5432
}

def generate_weather_data():
    base_temp = 10
    daily_variation = 10 * random.uniform(-1, 1)
    temperature = round(base_temp + daily_variation + random.uniform(-2, 2), 2)

    humidity = random.randint(30, 90)
    if temperature > 25:
        humidity = random.randint(20, 60)

    pressure = round(755 + random.uniform(-10, 10), 2)
    wind_speed = round(random.uniform(0, 15), 2)
    if random.random() < 0.1:
        wind_speed = round(random.uniform(10, 25), 2)

    return {
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure,
        "wind_speed": wind_speed
    }

def save_to_db(data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        query = """
        INSERT INTO weather_metrics 
        (temperature, humidity, pressure, wind_speed)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (
            data["temperature"],
            data["humidity"],
            data["pressure"],
            data["wind_speed"]
        ))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] данные записаны: "
              f"temp={data['temperature']}°C, "
              f"humidity={data['humidity']}%, "
              f"pressure={data['pressure']}мм, "
              f"wind={data['wind_speed']}м/с")
        
    except Exception as e: 
        print(f"ошибка записи в дб: {e}")

def main():
    print("старт генератора")
    

    for i in range(10):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.close()
            print("БД доступна")
            break
        except:
            print(f"ожидание БД... {i+1}")
            time.sleep(2)
    
    while True:
        weather_data = generate_weather_data()
        save_to_db(weather_data)
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"критическая ошибка: {e}")
        time.sleep(5)