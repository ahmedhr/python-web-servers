# Python Web Servers
Testing out Sanic, fastAPI and Custom ASGI app servers

## Sanic
- Runs using Sanic's native internal server OR using Uvicorn ASGI

## FastAPI and Minimal Custom Server
- Runs using Uvicorn ASGI

## As a Service [Linux]
- You can also run the servers as a Linux service (check the service-files directory)
- And use Nginx as the web server to forward requests to the service ports (check the Nginx configs)
