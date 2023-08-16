from fastapi import FastAPI
app = FastAPI()

@app.get("/primerapi")
def fununo(name: str):
    return ("Hola "+name+" bienvenido!")

@app.get("sumador")
def sumador(num1: float, num2: float):
    res = num1+num2
    return("El resultado es: "+ res)
