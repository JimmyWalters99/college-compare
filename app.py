from flask import Flask
from flask import Flask, render_template, request
import tuition_tracker_json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/aboutUs")
def about():
    return render_template("aboutUs.html")


@app.route("/ourGoal")
def goal():
    return render_template("our_goal.html")


@app.route("/comparePage")
def comparepage():
    return render_template("compare.html")


@app.route("/comparer", methods=["GET", "POST"])
def compare_results():
    if request.method == "POST":
        name1 = request.form["college1"]
        name1_valid = tuition_tracker_json.name_check(name1)

        name2 = request.form["college2"]
        name2_valid = tuition_tracker_json.name_check(name2)
        if name1_valid and name2_valid:
            return render_template(
                "table_result.html",
                name1=name1,
                type1=tuition_tracker_json.private_or_public(name1),
                location1=tuition_tracker_json.get_location(name1),
                price1=tuition_tracker_json.get_sticker_price(name1),
                accept_rate1=tuition_tracker_json.get_acceptance_rate(name1),
                grad_rate1=tuition_tracker_json.get_grad_rate(name1),
                local_weather1=tuition_tracker_json.get_current_weather(name1),
                local_temp1=tuition_tracker_json.get_current_temp(name1),
                total_enroll1=tuition_tracker_json.get_total_enroll(name1),
                male_ratio1=tuition_tracker_json.get_male_ratio(name1),
                female_ratio1=tuition_tracker_json.get_female_ratio(name1),
                school_url1=tuition_tracker_json.get_website(name1),
                
                name2=name2,
                type2=tuition_tracker_json.private_or_public(name2),
                location2=tuition_tracker_json.get_location(name2),
                price2=tuition_tracker_json.get_sticker_price(name2),
                accept_rate2=tuition_tracker_json.get_acceptance_rate(name2),
                grad_rate2=tuition_tracker_json.get_grad_rate(name2),
                local_weather2=tuition_tracker_json.get_current_weather(name2),
                local_temp2=tuition_tracker_json.get_current_temp(name2),
                total_enroll2=tuition_tracker_json.get_total_enroll(name2),
                male_ratio2=tuition_tracker_json.get_male_ratio(name2),
                female_ratio2=tuition_tracker_json.get_female_ratio(name2),
                school_url2=tuition_tracker_json.get_website(name2),
            )
        else:
            if not name1_valid and not name2_valid:
                return render_template(
                    "suggestions.html",
                    suggestions=str(tuition_tracker_json.name_suggestion(name1))
                    + str(tuition_tracker_json.name_suggestion(name2)),
                )
            if name1_valid and not name2_valid:
                return render_template(
                    "suggestions.html",
                    suggestions=str(tuition_tracker_json.name_suggestion(name2)),
                )
            if name2_valid and not name1_valid:
                return render_template(
                    "suggestions.html",
                    suggestions=str(tuition_tracker_json.name_suggestion(name1)),
                )


if __name__ == "__main__":
    app.run(debug=True)
