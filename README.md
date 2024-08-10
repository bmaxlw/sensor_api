**Local setup**

Requirements: Python, Docker (with Docker-compose)

1. git clone <repo_reference>
2. Create **env.sh** in a repo root:
   `
   export REDIS_PASSWORD="..."
   export REDIS_PORT="..."
   export REDIS_DATABASES="..."
   export REDIS_HOST="..."
   `
3. Make **env.sh** executable by calling `chmod +x env.sh` from a repo root
4. Execute **env.sh** using `source env.sh` from a repo root
5. Run `pip3 install -r src/requirements.txt` from repo root
6. Run `docker-compose up` from a repo root to run **redis**
7. Run `fastapi dev src/main.py` from a repo root to run the **API**
