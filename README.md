# FastAPI task

## Setup
- Clone project and run `docker-compose up`.
- Check all is running OK `docker-compose ps`. All services must be in `Up` state.

## Usage
```json
GET
http://localhost:8888/GetStats
```
```json
POST http://localhost:8888/AddTasks
Content-Type: application/json
{
  "taskid": "1",
  "description": "Description",
  "params": {
    "test1": "stringA",
    "test2": "stringB"
  }
}
```

## TODO:
Make two services
1. Service `A` two endpoints
   - `/GetStats`. Returns a single number — the number of successfully processed `AddTasks` calls since the service started.
   - `/AddTasks`. Adds messages to the queue, example:
```json
{
  "taskid": "1",
  "description": "Description",
  "params": {
    "test1": "stringA",
    "test2": "stringB"
  }
}
```
2. Service `B` aka Listener. When reading messages, it prints them to `stdout`.

## Tech stack: 
`fastapi`, `aio-pika`, `rabbitmq`