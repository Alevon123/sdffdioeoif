#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return 'Что такое глобальное потепление?'

@app.route('/')
def index():
    return 'Cоздавал Алексей Степаненко'

@app.route('/')
def index():
    return 'Проблема глобального потепления...'



@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    address = request.form['address']

    with open('form.txt', 'a') as file:
        file.write(name + ' ' + email  + ' '  + address  + ' '  + date + '\n')
        print((file.write))

    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,
                           email=email,
                           date=date,
                           address=address
                           )

app.run(debug=True)
