from flask import Flask, render_template, request,session
app = Flask(__name__)
app.secret_key = "CCC"

@app.route('/')
def home():

    return render_template('homepage.html')
    

@app.route('/you_page_questions')
def about_user():
    user = request.args.get("person")
    session['name']= user 
    return render_template('about_you_questions.html',user_name = session['name'])

@app.route('/answers')
def user_answers():
    food_ingredient = request.args.get('ingredient')
    city = request.args.get('city')
    season = request.args.get('season')
    fun_fact = request.args.get('fun')

    return render_template('user_answers.html',user_food_ingredient=food_ingredient,user_city=city,user_season=season,user_fun_fact=fun_fact,user_name = session['name'])




if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
