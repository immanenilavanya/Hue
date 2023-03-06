import base64
from io import BytesIO
from PIL import Image
from sanic import Sanic, response, text
from sanic.exceptions import SanicException
import palette_extraction as pe

app = Sanic("Hue")
HOST = "localhost"
PORT = 8080

@app.route('/file', methods=['POST'])
async def handle_request(request):
    try:
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            raise SanicException("No file uploaded")

        # Get the file contents as bytes
        file_contents = uploaded_file.body

        # Process the file (for example, extract a color palette)
        image = Image.open(BytesIO(file_contents))
        palette = pe.extract_palette(image)

        # Return a response with the palette as JSON
        return response.json({'palette': palette})
        
    except SanicException as e:
        return text(str(e), status=400)
    except Exception as e:
        return text("Server error", status=500)

if __name__ == "_main_":
    app.run(host=HOST, port=PORT, debug=True)