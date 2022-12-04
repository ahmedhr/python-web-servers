import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    path = scope['path']

    async def arbis_handler():
        return b"reached arbis"

    paths = {
        "/": arbis_handler()
    }
    executioner = paths[path]
    reslt = await executioner
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': reslt,
    })


if __name__ == "__main__":
    uvicorn.run("my_server:app", port=5001, log_level="info")
