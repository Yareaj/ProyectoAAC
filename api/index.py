from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import the core modules from local directory
from core.dynamic_array import DynamicArray
from core.arithmetic import (
    decimal_a_base_b, 
    base_b_a_decimal,
    suma_digitos_base_b, 
    resta_digitos_base_b, 
    multiplicacion_digitos_base_b
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request Model
class OperationRequest(BaseModel):
    u: int
    v: int
    base: int

@app.get("/decimal_to_base/{decimal}/{base}")
def decimal_to_base(decimal: int, base: int):
    if base < 2:
        return {"error": "Base must be at least 2"}
    digitos, b_string, size = decimal_a_base_b(decimal, base)
    return {
        "digits": [digitos.get(i) for i in range(len(digitos))],
        "base_string": b_string,
        "size": size
    }

@app.get("/base_to_decimal/{base}")
def base_to_decimal(base: int):
    if base < 2:
        return {"error": "Base must be at least 2"}
    digitos = DynamicArray()
    base_list = [890,567,234,1]
    for dig in base_list:
        digitos.push(int(dig))
    decimal = base_b_a_decimal(digitos, base)
    return {
        "decimal": decimal
    }

@app.post("/suma")
def suma(data: OperationRequest):
    result = suma_digitos_base_b(data.u, data.v, data.base)
    return result

@app.post("/resta")
def resta(data: OperationRequest):
    result = resta_digitos_base_b(data.u, data.v, data.base)
    return result

@app.post("/multiplicacion")
def multiplicacion(data: OperationRequest):
    result = multiplicacion_digitos_base_b(data.u, data.v, data.base)
    return result

# This is the entry point for Vercel
handler = app
