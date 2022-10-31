import json
import os


#template

class MadLibs:
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions

    @classmethod
    def from_json_file(cls, filename, path="./templates"):
        fpath = os.path.join(path, filename)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib


#get user input
def get_words(word_descriptions):
    words = [] #list to hold inputted words 
    print("Provide the following:")
    for description in word_descriptions:
        user_word = input(f"{description}: ")
        words.append(user_word) 
    return words

#build the story
def build_story(template, words):
    story = template.format(*words) #formats the template and passes in each element of the list as an argument
    return story




temp_name = "my_stay_at_hospital.json"
mad_lib = MadLibs.from_json_file(temp_name)
words = get_words(mad_lib.word_descriptions)
story = build_story(mad_lib.template, words)

print(story)



#insert a list and choose amount of entries