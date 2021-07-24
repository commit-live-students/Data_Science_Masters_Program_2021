# Loading the Agent
rasaNLU = RasaNLUInterpreter("models/nlu/default/chat")
agent = Agent.load("models/dialogue", interpreter= rasaNLU)

# asking question
agent.handle_message('Hi')
>>> [{'recipient_id': 'default', 'text': 'Hey'}]

# once more
agent.handle_message('How many days in January')
>>> [{'recipient_id': 'default', 'text': 'There are 31 days in the mentioned month.'}]

# once more
agent.handle_message('How many days in April')
>>> [{'recipient_id': 'default', 'text': 'There are 30 days in the mentioned month.'}]

# once more
agent.handle_message('Bye')
>>> [{'recipient_id': 'default', 'text': 'Goodbye'}]