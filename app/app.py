from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        linkedin = request.form.get("linkedin")
        github = request.form.get("github")

        education = request.form.get("education")
        skills = request.form.get("skills")
        experience = request.form.get("experience")
        projects = request.form.get("projects")
        certifications = request.form.get("certifications")
        achievements = request.form.get("achievements")

        return render_template(
            "resume.html",
            name=name,
            email=email,
            phone=phone,
            linkedin=linkedin,
            github=github,
            education=education,
            skills=skills,
            experience=experience,
            projects=projects,
            certifications=certifications,
            achievements=achievements
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)