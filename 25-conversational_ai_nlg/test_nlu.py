
# loading the interpreter 
interpreter = Interpreter.load('./models/nlu/default/chat')

# define function to ask question
def ask_question(text):
    print(interpreter.parse(text))

# asking question
ask_question("How many days in January")
ask_question("How many days in March