import connexion  # adds the module to the program
from flask import render_template

app = connexion.App(__name__, specification_dir="./")  # additional app creation
app.add_api("swagger.yml")  # configure the system to provide the connexion functionality


@app.route("/")
def home():
    user = {"name":"Krishna",
            "age": 25}
    return render_template("home.html", user_obj=user)

@app.route("/users")
def get_users():
    return [
    {"name":"Ram", "email":"Ram@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"}
]



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
