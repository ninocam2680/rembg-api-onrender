from fastapi import FastAPI, UploadFile, File
from rembg import remove
from fastapi.responses import Response

app = FastAPI()

@app.post("/remove")
async def remove_bg(file: UploadFile = File(...)):
    input_bytes = await file.read()
    output_bytes = remove(input_bytes)
    return Response(content=output_bytes, media_type="image/png")
