from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder= 'templates')



todos = []


@app.route('/')     #'/' is the root route
def index():
    return render_template('index.html', todos = todos)

@app.route('/add', methods = ['POST'])      #'/add' is the route for adding a new todo item, and it only accepts POST requests
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods = ['GET', 'POST'])      #'/edit/<int:index>' is the route for editing a todo item, where <int:index> is a placeholder for the index of the todo item in the list. This route accepts both GET and POST requests. GET requests are used to display the edit form, while POST requests are used to update the todo item with the new task value submitted from the form.
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo = todo, index = index)

@app.route('/check/<int:index>')        #'/check/<int:index>' is the route for toggling the completion status of a todo item, where <int:index> is a placeholder for the index of the todo item in the list. When this route is accessed, it toggles the 'done' status of the specified todo item and then redirects back to the index page.
def check(index):
    todos[index] ['done'] = not todos[index]['done']
    return redirect(url_for("index")) 

@app.route('/delete/<int:index>')       #'/delete/<int:index>' is the route for deleting a todo item, where <int:index> is a placeholder for the index of the todo item in the list. When this route is accessed, it deletes the specified todo item from the list and then redirects back to the index page.
def delete(index):
    del todos[index]
    return redirect(url_for("index"))  



if __name__ == '__main__':
    app.run(debug = True)

