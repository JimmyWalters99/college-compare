from flask import Flask
from flask import Flask, render_template, request
from tuition_tracker_json import stat_list
app = Flask(__name__)
@app.route('/', methods = ["GET", "POST"])
def table_maker():
    if request.method == "POST":
        #college1 = request.form["college1"]
        college1 = 'Babson College'
        info1 = stat_list(college1)
        #stat_list is a function which returns all the outputs from the web scrape code into one list.
        if info:
            return render_template(
                "table_result.html",
                first_choice = college1
                info = info1
            )
        else:
            return render_template("GC_HTML_CODE.html", error = True)
    return render_template("GC_HTML_CODE.html", error = None)   
if __name__ == "__main__":
    app.run(debug=True)  