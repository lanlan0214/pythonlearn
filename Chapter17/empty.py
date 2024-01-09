####################################################################### Tkinter
# # from tkinter import *

# # root = Tk()
# # myLabel = Label(root, text="This is my text")
# # myLabel.pack()

# # root.mainloop()
# import tkinter as tk

# root = tk.Tk()

# canvas = tk.Canvas(root, width=300, height=300) # 視窗變大
# canvas.pack()

# def hello():
#   label = tk.Label(root, text="Hello World!", fg="green", font=('helvetica', 12, 'bold'))
#   canvas.create_window(150, 200, window=label)

# button = tk.Button(text="Click Me!!", fg="black", command=hello)
# canvas.create_window(150, 150, window=button)

# root.mainloop()
####################################################################### Flask
from flask import Flask, jsonify, render_template

# create flask app
app = Flask(__name__)

@app.route("/")
@app.route("/hello/<name>")
# def index():
#     return "This is my homepage!!"
def home(name=None):
  return render_template('index.html', name=name)
@app.route("/info", methods=['POST'])
def returnSomething():
  # Javascript Object Notation
  return jsonify({'info': 'You have successfully make a request.'})
  
if __name__ == '__main__':
    app.run(debug=True)
