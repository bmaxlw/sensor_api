import redis, os

def get_redis(redis_host: str = os.getenv('REDIS_HOST', 'localhost'), 
              redis_port: str = os.getenv('REDIS_PORT', 6379)) -> redis.Redis:
    return redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def populate_redis(r_session: redis.Redis) -> None:
    sensors_base = {
        "d7828b2e-de80-4812-b0e9-a2f20ac41b71": {"min": 50.00, "max": 1900.00},
        "d53e992d-584e-4cb2-829b-221d92cf1d35": {"min": 60.00, "max": 2000.00},
        "abdcc6e2-3f7b-4f31-aaea-3dbede05c7ae": {"min": 70.00, "max": 2000.00},
        "891aafc8-43c9-445b-9a54-4cedb94a676f": {"min": 50.00, "max": 1900.00},
        "73ab7318-8e89-45d4-a570-dea7328abbd5": {"min": 70.00, "max": 2000.00},
        "232d39f5-e254-4096-8fd5-09c1a5f55792": {"min": 100.00, "max": 2100.00},
        "bfa43876-29c2-47ac-9b0e-6a840526e849": {"min": 100.00, "max": 2100.00},
        "d26ce4ea-eed8-4d91-84cf-a4092e2ffcb1": {"min": 50.00, "max": 1900.00},
        "14f1e9e9-2428-4bf4-8738-ebe89e0b4712": {"min": 75.00, "max": 150.00},
        "8aa2940d-9c5e-4875-b32b-680f278acd8d": {"min": 100.00, "max": 200.00},
    }

    for k,v in sensors_base.items():
        r_session.set(k,f"{v.get("min")},{v.get("max")}")
