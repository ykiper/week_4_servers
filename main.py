from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

def save_to_json(file_name: str, data):
    with open(file_name, "w") as f:
        json.dump(f, data)


def load_from_json(file_name: str):
    with open(file_name, "r") as f:
        data = json.load(f)
    return data



def save_name(file_name:str, name:str):
    with open(file_name, "a") as f:
        f.write(name + "\n")

def update_total_requests(data:list[dict], url: str):
    for endpoint in data:
        if endpoint['url'] == url:
            endpoint['stats']['total_requests_received'] += 1
            return data




@app.get("/test")
def test():
    # endpoints_data = load_from_json("endpoints_data.json")
    # updated_data = update_total_requests(endpoints_data, "/test")
    # save_to_json("endpoints_data.json", updated_data)
    return {'msg': 'hi from test'}

@app.get("/test/:{name}")
def add_names(name:str):
    # endpoints_data = load_from_json("endpoints_data.json")
    # updated_data = update_total_requests(endpoints_data, "/test/:name")
    # save_to_json("endpoints_data.json", updated_data)
    if name:
        save_name("names.txt", name)
        print("Name saved")


class Caesar(BaseModel):
    text:str
    offset:int
    mode: str


@app.post("/caesar")
def caesar_cipher(caesar: Caesar):
    new_text = ""
    for ch in caesar.text:
        if caesar.mode ==  "encrypt":
            ord_ch = ord('a') + (ord('z') - ord('a') + caesar.offset) % (ord('z') - ord('a'))
            print(chr(ord_ch))
            new_text += chr(ord_ch)
        if caesar.mode == 'decrypt':
            ord_ch = ord('a') + (ord('z') - ord('a') - caesar.offset) % (ord('z') - ord('a'))
            new_text += chr(ord_ch)
    if caesar.mode == "encrypt":
        return {"encrypted_text": new_text}
    if caesar.mode == 'decrypt':
        return {"decrypted_text": new_text}





