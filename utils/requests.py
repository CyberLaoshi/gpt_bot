# import requests
from transformers import AutoTokenizer

class GPT():
  CONTENT = "You are a creative teacher of English who makes funny and interesting tasks. Provide me with a new task according to my description."

  def __init__(self,system_content=CONTENT):
    self.system_content = system_content
    self.URL = 'http://localhost:1234/v1/chat/completions'
    self.HEADERS = {'Content-Type': 'application/json'}
    self.assistant_content = 'Do the tasks in several steps.'
    self.max_tokens = 256

  def __str__(self):
    return f'I am a {self.system_content} requesting {self.URL} with {self.HEADERS} in {self.max_tokens}. I should {self.assistant_content}'

  @staticmethod
  def count_tokens(text):
    model_id = "mistralai/Mistral-7B-Instruct-v0.1"
    tokenizer = AutoTokenizer.from_pretrained(model_id)  # название модели
    return len(tokenizer.encode(text))


new_gpt = GPT()
# print(new_gpt)
print(new_gpt.count_tokens("Make a task where a student is supposed to fill the gaps with these words: "))