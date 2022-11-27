from sanic import Sanic

from first_route import bp

app = Sanic("MyHelloWorldApp")
app.blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234, debug=True)





