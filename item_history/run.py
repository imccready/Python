from main import app

app.run(debug=app.config['DEBUG'], port=80)