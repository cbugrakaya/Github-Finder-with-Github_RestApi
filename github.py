from flask import Flask,render_template,request
import requests


app = Flask(__name__)
base_url = "https://api.github.com/users/"


@app.route("/",methods=["GET","POST"])
def index():
    
    if request.method == "POST":
        github_name = request.form.get("githubname")
        reponse_user = requests.get(base_url + github_name)
        reponse_repos = requests.get(base_url + github_name + "/repos")

        user_info = reponse_user.json()
        repos = reponse_repos.json()
        
        return render_template("index.html",profile = user_info,repos = repos)
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
