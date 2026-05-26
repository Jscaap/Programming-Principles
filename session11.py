# testing functions
def get_formatted_name(first, last):
    full_name = f"{first}{last}"
    return full_name

from name_function import get_formatted_name
print("Enter 'q' at any time to quit")
while True:
    first = input("\n Please give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
formatted_name = get_formatted_name(first,last)
print(f"Formatted name: {formatted_name}")


# testing functions - unit tests and test cases
from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name("Janis", "Joplin")
    assert formatted_name == "Janis Joplin"
    

# testing functions - a failing test
from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name("Janis")
    assert formatted_name == "Janis Joplin"
    
    
# testing a class - class example: AnonymousSurvey
# testing a class involves verifying the behaviour of its methods
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)
        
    def store_response(self, new_response):
        self.responses.append(new_response)
        
    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print(f" - {response}")
            
            
# testing a class - testing a AnonymousSurvey class
from survey import AnonymousSurvey

def test_store_single_response():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert "English" in language_survey.responses
    
def test_store_three_responses():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
        
        
# example
# add_fun.py
def add(num1, num2):
    result = num1 + num2
    return result

# test_fun.py
from add_fun import add

def test_add_pos():
    assert add(4,5) == 9
def test_add_neg():
    assert add(-3,-5) == -8
def test_add_mix():
    assert add(-5,9) == 4