import base64
from PIL import Image
from sanic import Sanic
from sanic import response

app = Sanic("Req")
HOST = "localhost"
PORT = 8081

@app.route("/")
async def send(request):
    return await response.file_stream(
        "../source/sample_image.jpg",
        chunk_size=1024,
        mime_type="application/metalink4+xml",
        headers={
            "Content-Disposition": 'Attachment; filename="image.jpg"',
            "Content-Type": "application/metalink4+xml",
        },
    )

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)