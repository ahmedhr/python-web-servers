import copy


async def arbis_handler():
    return b"reached arbis"


paths = {
    "/arbis": arbis_handler()
}


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    path = scope['path']
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
