from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    value = {
        "name":"Bishal Shrestha",
        "age": 18,
        "roll_no": 8,
        "faculty":"Bsc.CSIT",
        "semester": 2,
        }
    return value