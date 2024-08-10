import datetime, random, src.database as db
from fastapi import FastAPI

app = FastAPI()
red = db.get_redis()
db.populate_redis(r_session=red)

@app.get("/sensors")
def get_temperature_sensors():

    sensors: dict[str, dict] = {}
    keys: list[str] = red.keys('*')
    for key in keys:
        sensors[key] = {"min": red.get(key).split(',')[0], 
                        "max": red.get(key).split(',')[1]}

    responses: list[dict] = [
        {
            "sensor_id": sid,
            "sensor_date": datetime.date.today(),
            "sensor_time": datetime.datetime.now().strftime("%H:%M:%S"),
            "sensor_limit_low": tmap.get("min"), 
            "sensor_limit_high": tmap.get("max"),
            "sensor_temp_low": round(random.uniform(float(red.get(sid).split(",")[0]),
                                              float(red.get(sid).split(",")[0])*1.025 if random.randint(1,10)%2==0 
                                              else float(red.get(sid).split(",")[0])*0.975),2),
            "sensor_temp_high": round(random.uniform(float(red.get(sid).split(",")[1]),
                                              float(red.get(sid).split(",")[1])*1.025 if random.randint(1,10)%2==0 
                                              else float(red.get(sid).split(",")[1])*0.975),2),
            "sensor_temp_low_prev": float(red.get(sid).split(",")[0]),
            "sensor_temp_high_prev": float(red.get(sid).split(",")[1])
        } for sid, tmap in sensors.items()     
    ]

    redis_log = list(zip([sensor_id for sensor_id in sensors.keys()], 
                         [f"{response.get("sensor_temp_low")},{response.get("sensor_temp_high")}" for response in responses]))
    
    for record in redis_log:
        red.set(*record)

    return responses