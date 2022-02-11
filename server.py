from flask import Flask, render_template, template_rendered  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checker():
    return 'Hello checkerboard'  # Return the string 'Hello World!' as a response

@app.route('/<int:num>')
def checker_num(num):
    return render_template('index.html', rows=num)


@app.route('/<int:num>/<string:color>')
def colorOne(num, color):
    return render_template('index.html', rows=num, color=color)

@app.route('/<int:num>/<string:color>/<string:color2>')
def colortwo(num, color, color2):
    return render_template('index.html', rows=num, color=color, color2=color2)











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)