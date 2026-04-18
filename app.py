import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)
app.secret_key = "test"
app.debug = False


# -----------------------
# BENCH PRESS
# -----------------------
def get_bench_plan(level):

    if level == "top":
        return {
            "comment": "You have weak triceps and nothing else.",
            "main": [
                "Three, Four or Five Board Press – Close Grip",
                "Pin Press – Close Grip",
                "Two Chains Barbell Press – Close and Medium Grip"
            ],
            "accessory": [
                "JM Press – Flat or Declined",
                "Rolling Dumbbell Extensions – Flat, Incline or Declined",
                "Smith Machine JM Press or Skull Crusher"
            ]
        }

    elif level == "middle":
        return {
            "comment": "Your triceps are weak. You may also be struggling with speed from the bottom of the lift. Remember that things in motion stay in motion, so get that bar moving quickly to get past the middle point.",
            "main": [
                "Medium or Light band tensioned Bench Press – Any grip",
                "Two Board Press – Any grip",
                "Floor Press – Any grip"
            ],
            "accessory": [
                "JM Press – Flat or Declined",
                "Rolling Dumbbell Extensions – Flat, Incline or Declined",
                "Smith Machine JM Press or Skull Crusher"
            ]
        }

    else:
        return {
            "comment": "9 times out of 10, you’re failing at the bottom because the weight is too heavy. If you strain and fail here, reduce load by ~33% and perform 2x10 reps, then take a rest week. It can also be pec or lat weakness affecting stability.",
            "main": [
                "Dips",
                "Dumbbell Bench Press – Flat",
                "Spoto Press – Flat"
            ],
            "accessory": [
                "Lat Pulldown or Row",
                "Cable Pec Fly",
                "Deficit Pushup"
            ]
        }


# -----------------------
# SQUAT
# -----------------------
def get_squat_plan(level):

    if level == "top":
        return {
            "comment": "You lack the power to lock out your knees fully. This is a function of your quad muscles, and one of the easiest things to fix.",
            "main": [
                "Box Squat – Close Stance from a High Box",
                "Pin Squat (aka Andersen Squat)",
                "Front Squat"
            ],
            "accessory": [
                "Leg Extension Machine",
                "Close Stance Leg Press",
                "Goblet Squat with heels elevated"
            ]
        }

    elif level == "middle":
        return {
            "comment": "As with every lift, working on speed will help you explode through this middle section. If you are bending over and failing, work on core and lower back. If you are staying upright, work on quads.",
            "main": [
                "Zercher Squat",
                "Squat with heavy band tension",
                "Box Squat"
            ],
            "accessory": [
                "Leg Extension Machine",
                "Lower back hyperextension",
                "Plank & other core work"
            ]
        }

    else:
        return {
            "comment": "If you fail at the bottom, it may be load too heavy or mobility/form breakdown. Falling forward = ankle mobility/core issue. Staying upright but failing = strength limitation.",
            "main": [
                "Squat with 5 second pause at the bottom of the lift",
                "Good morning",
                "Bulgarian Split Squats"
            ],
            "accessory": [
                "Lower back hyperextension",
                "Plank and other core work",
                "ATG split squat"
            ]
        }


# -----------------------
# DEADLIFT
# -----------------------
def get_deadlift_plan(level):

    if level == "top":
        return {
            "comment": "If you are struggling to lock the weight out at the top, you have an issue with your glutes, or else trapezoids.",
            "main": [
                "Hip thrusts with barbell or machine",
                "Deadlift from pins high",
                "Sumo Deadlift"
            ],
            "accessory": [
                "Bent over barbell shrug",
                "Glute kickback",
                "Single leg RDL"
            ]
        }

    elif level == "middle":
        return {
            "comment": "Speed is needed to burst through the middle section of the lift. You may also need to work on areas above and below the sticking point.",
            "main": [
                "Romanian Deadlift",
                "Deadlift from pins set below the knee",
                "Deadlift with heavy band tension"
            ],
            "accessory": [
                "Lower back hyperextension",
                "Hamstring curl",
                "Plank and other core work"
            ]
        }

    else:
        return {
            "comment": "If the bar is stuck to the floor, the weight may be too heavy. If you can lift more from pins, focus on strength from the floor position.",
            "main": [
                "Deficit deadlift (stand on a weight plate 1–2 inches thick)",
                "Deadlift with 5 second pause 1–2 inches off the floor",
                "Sumo Deadlift"
            ],
            "accessory": [
                "Lower back hyperextension",
                "Hamstring curl",
                "Plank and other core"
            ]
        }


# -----------------------
# ROUTES
# -----------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/concepts")
def concepts():
    return render_template("concepts.html")


@app.route("/weakpoints", methods=["GET"])
def weakpoints():
    return render_template("weakpoints.html")


@app.route("/solutions", methods=["POST"])
def solutions():

    squat = request.form.get("squat")
    bench = request.form.get("bench")
    deadlift = request.form.get("deadlift")

    rec = {
        "bench": get_bench_plan(bench),
        "squat": get_squat_plan(squat),
        "deadlift": get_deadlift_plan(deadlift)
    }

    return render_template("solutions.html", rec=rec)


# -----------------------
# RUN APP
# -----------------------
if __name__ == "__main__":
    debug_flag = str(os.environ.get("DEBUG", "False")).lower() in ("1", "true", "yes")
    app.run(debug=debug_flag)