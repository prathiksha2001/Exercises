from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
# /// - relative path & //// - represents absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#database initialization 
db = SQLAlchemy(app)
# db.init_app(app)
#creating model
class Todo(db.Model):
    # __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200),nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task {}>'.format(self.id) 

# with app.app_context():
#     db.create_all()


@app.route('/', methods = ['POST','GET'])
def index():
    if request.method =='POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()       
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        try: 
            db.session.commit()
            return redirect('/')
        except:
            return "There was a error while updating your task"
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)


# python interactive terminal
# from app import db
# db.create_all() 
