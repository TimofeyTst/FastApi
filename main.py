from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'I am a function'

@app.get('/about')
def about():
    return {'Fuck':' We haven`t code it yet'}