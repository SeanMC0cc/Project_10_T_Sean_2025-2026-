#working with numbers
from pyscript import display, document

def getting_data(e):
        document.getElementById('output').innerHTML = ""

        x = float(document.getElementById("X_val").value)
        y = float(document.getElementById("Y_val").value)
        h = float(document.getElementById("H_val").value)

        area = ((x + y) / 2) * h

        display(f"Trapezoid area is: {area:.2f}", target="output")