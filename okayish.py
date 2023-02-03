from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            AK = int(request.form["averageKinship"])
            Modifier = math.sqrt(AK/50)
        except ValueError:
            return "Invalid value for Average Kinship. Please input a whole number."

        try:
            SO = float(request.form["spilloverRate"])
        except ValueError:
            return "Invalid value for Spillover rate. Please input a number."

        OS = float(request.form["ownerShare"])
        AlchLeft = 1 - SO
        FUD = 20
        FOMO = 10
        ALPHA = 5
        KEK = 2
        CompensationFUD = ((Modifier * FUD) * AlchLeft) * OS
        CompensationFOMO = ((Modifier * FOMO) * AlchLeft) * OS
        CompensationALPHA = ((Modifier * ALPHA) * AlchLeft) * OS
        CompensationKEK = ((Modifier * KEK) * AlchLeft) * OS

        try:
            UG = int(request.form["gotchisUnchanneled"])
        except ValueError:
            return "Invalid value for Gotchis unchanneled. Please input a whole number."

        TotalCompensationFUD = CompensationFUD * UG
        TotalCompensationFOMO = CompensationFOMO * UG
        TotalCompensationALPHA = CompensationALPHA * UG
        TotalCompensationKEK = CompensationKEK * UG

        FUDprice = float(request.form["FUDprice"])
        FOMOprice = float(request.form["FOMOprice"])
        ALPHAprice = float(request.form["ALPHAprice"])
        KEKprice = float(request.form["KEKprice"])
        TotalCompensationUSD = (TotalCompensationFUD * FUDprice) + (TotalCompensationFOMO * FOMOprice) + (TotalCompensationALPHA * ALPHAprice) + (TotalCompensationKEK * KEKprice)
        return render_template("result.html", TotalCompensationFUD=TotalCompensationFUD, TotalCompensationFOMO=TotalCompensationFOMO, TotalCompensationALPHA=TotalCompensationALPHA, TotalCompensationKEK=TotalCompensationKEK, TotalCompensationUSD=TotalCompensationUSD)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
