import re

# # 1. Simple matching
# text = "The phone number is 123-456-7890."
# pattern = r'\d{3}-\d{3}-\d{4}'  # Pattern for a phone number
# match = re.search(pattern, text)

# if match:
#     print(f"Phone number found: {match.group()}")
# else:
#     print("No phone number found.")

# 2. Extracting multiple matches
# multiline_text = """Name: Alice
# Age: 30
# Name: Bob
# Age: 25"""
# pattern_name_age = r'Name: (\w+)\nAge: (\d+)'
# matches = re.findall(pattern_name_age, multiline_text)

# for name, age in matches:
#     print(f"Name: {name}, Age: {age}")

# # 3. Text replacement
# text_to_modify = "Dogs are awesome, but cats are also awesome."
# pattern_cats = r'cats'
# new_text = re.sub(pattern_cats, 'birds', text_to_modify)
# print(f"Modified text: {new_text}")

# 4. Text splitting
text_to_split = "This is a sentence. And here is another sentence."
pattern_sentence = r'\.'
sentences = re.split(pattern_sentence, text_to_split)
print("Sentences: ", sentences)
