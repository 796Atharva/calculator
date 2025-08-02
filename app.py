from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = "Error (division by zero)" if num2 == 0 else num1 / num2
            else:
                result = "Invalid operator"
        except:
            result = "Invalid input"
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
