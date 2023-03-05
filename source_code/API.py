import base64
from PIL import Image
from sanic import Sanic, json
from sanic.views import stream
from sanic import response, text
import palette_extraction as pe
import request_send as req_s

app = Sanic("Hue")
HOST = "localhost"
PORT = 8080

@app.route('/file')
@stream
async def handle_request(request):
    try:
        result = ""
        while True:
            body = await request.stream.read()
            if body is None:
                break
            result += body
        return text(body)
    except:
        return json({"upload" : "failed"}, status = 400)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)