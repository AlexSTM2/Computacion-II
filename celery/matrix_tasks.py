from celery_app import app
import math

@app.task
def pot(num):
    print(f"Calculating {num}^{num}.")
    return math.pow(num, num)

@app.task
def root(num):
    print(f"Calculating the root of {num}.")
    return math.sqrt(num)

@app.task
def log(num):
    print(f"Calculating the log of {num}.")
    return math.log10(num)