docker run -d --name redis-server -p 6379:6379 -v redis_data:/data redis:latest
docker stop redis-server
docker start redis-server