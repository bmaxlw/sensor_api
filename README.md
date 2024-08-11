**Local setup**

Requirements: Python, Docker (with Docker-compose)

1. git clone `repo_reference`
2. Create `.env` in a repo root:
   `export REDIS_PASSWORD="..."`
   `export REDIS_PORT=...`
   `export REDIS_DATABASES="..."`
   `export API_PORT=...`
   `export DOCKER_REPO="rutkos"` # in case you use existing image
   `
3. Run `sudo docker-compose up`
