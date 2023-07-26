from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello there!'

@app.get('/property/{id}')
def property(id):
    return f'This is a property page {id}'

@app.get('/movies')
def movies():
    return {'movie list: ': {'movie1', 'movie2'}}