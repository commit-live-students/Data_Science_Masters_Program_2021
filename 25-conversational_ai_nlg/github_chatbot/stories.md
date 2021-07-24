
## happy path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet
* mood_great               <!-- user utterance, in format intent[entities] -->
  - utter_happy
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_goodbye
  
## curious path 1               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action the bot should execute -->
* mood_curious
  - utter_ask_link
* inform{"group":"A"}  
  - action_retrieve_link
  - utter_did_that_help
* mood_affirm
  - utter_happy

## curious path 2
* greet
  - utter_greet
* mood_curious
  - utter_ask_link
* inform{"group":"B"}
  - action_retrieve_link
  - utter_did_that_help
* mood_deny
  - utter_goodbye
  
## curious path 3
* greet
  - utter_greet
* mood_curious{"group":"A"}
  - action_retrieve_link
  - utter_did_that_help
* mood_affirm
  - utter_happy
  
## strange user
* mood_affirm
  - utter_happy
* mood_affirm
  - utter_unclear

## say goodbye
* goodbye
  - utter_goodbye

## fallback
- utter_unclear

