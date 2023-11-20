# pip install python-multipart
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# 바이트 단위로 데이터를 전달  받고 메모리에 저장됨
# @app.post("/files")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}         
@app.post("/files")
async def create_file(file: bytes | None = File(default=None)):
    if( not file):
        return {"message": "파일이 존재하지 않음"}
    else:
        return {"file_size": len(file)}         


# File()를 따로 생성할 필요가 없음
# 만약 파일의 크기가 메모리 사이즈 이상을 넘어가면 디스크에 저장
# 이미지, 비디오, 큰 바이너리 파일 등과 같은 파일에 적합
# 파일에 저장된 메타데이터 정보를 해당 구문을 통하여 얻을 수 있음
# @app.post("/uploadfile")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}
@app.post("/uploadfile")
async def create_upload_file(file: UploadFile | None = None):
    if ( not file ):
        return {"message": "파일이 존재하지 않음"}
    else :
        return {"filename": file.filename}