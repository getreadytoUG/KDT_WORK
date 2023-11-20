from fastapi import FastAPI, File, UploadFile
import shutil as sh
import os

app = FastAPI()

@app.post("/uploadfile")
async def upload_file(file: UploadFile):
    if ( not file ):
        return {"message": "파일이 없습니다."}
    else:
        save_dir = os.path.join("C:\Hong\KDT\FastAPI", file.filename)
        with open(save_dir, "wb") as dest_file:
            sh.copyfileobj(file.file, dest_file)
        return {"message": "success"}