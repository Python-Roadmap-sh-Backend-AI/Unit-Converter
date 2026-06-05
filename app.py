from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/length", methods=["POST","GET"])
def length():
    result = None

    length_units = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }
    if request.method == "POST":
        value = float(request.form.get("value"))
        from_unit = request.form.get("from_unit")
        to_unit = request.form.get("to_unit")

        base_value = value * length_units[from_unit]
        result = base_value / length_units[to_unit]

        print(value, from_unit, to_unit)
    return render_template("length.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)