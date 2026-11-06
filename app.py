
from flask import Flask, render_template, request

app = Flask(__name__)

class Calculator:

    def perform_calculation(self, values, operators):

        result = values[0]

        for i in range(len(operators)):

            value = values[i + 1]
            operator = operators[i]

            try:

                if operator == "+":
                    result = result + value

                elif operator == "-":
                    result = result - value

                elif operator == "*":
                    result = result * value

                elif operator == "/":
                    result = result / value

                elif operator == "%":
                    result = result % value

                else:
                    raise ValueError("Invalid operator!")

            except ZeroDivisionError:
                raise ValueError("Cannot divide by zero!")

        return result



calc = Calculator()


@app.route("/", methods=["GET", "POST"])
def calculator():

    result = None
    error = None

    if request.method == "POST":

        try:

            # Getting values from HTML
            values = [
                float(x) for x in request.form.getlist("values")
            ]

            # Getting operators from HTML
            operators = request.form.getlist("operators")

            # Validating inputs
            if len(values) < 2:
                raise ValueError("Enter at least 2 values!")

            if len(values) > 20:
                raise ValueError("Maximum 20 values allowed!")

            if len(operators) != len(values) - 1:
                raise ValueError("Invalid number of operators!")

            # Calling class method
            result = calc.perform_calculation(values, operators)

        except ValueError as e:

            error = str(e)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
