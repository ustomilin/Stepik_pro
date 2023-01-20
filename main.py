from fastapi import FastAPI

app = FastAPI()


@app.get("/abc")
async def root():
    return 'Hi'
