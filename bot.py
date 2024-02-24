# import requests
# from transformers import AutoTokenizer


def count_tokens(text):
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")  # название модели
    return len(tokenizer.encode(text))


print('Привет!')
print('Я твой помощник для решения задач по математике. Можешь ввести любую задачу, и я постараюсь её решить.')
print('Если введёшь слово "Продолжить", я продолжу объяснять задачу.')
print('Для завершения диалога введи слово "Конец".')

system_content = "Ты - дружелюбный помощник для решения задач по математике. Давай подробный ответ с решением на русском языке"
assistant_content = "Решим задачу по шагам: "

task = ""
answer = ""
max_tokens_in_task = 2048

while True:
    user_content = input()

    if count_tokens(user_content) > max_tokens_in_task:
        print("Текст задачи слишком длинный!")
        continue

    if user_content.lower() == 'конец':
        break

    if user_content.lower() != "продолжить":
        task = user_content
        answer = ""

    resp = requests.post(
        'http://localhost:1234/v1/chat/completions',
        headers={"Content-Type": "application/json"},

        json={
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content + answer},
            ],
            "temperature": 1,
            "max_tokens": 2048
        }
    )

    if resp.status_code == 200 and 'choices' in resp.json():
        result = resp.json()['choices'][0]['message']['content']
        if result == "":
            print("Объяснение закончено")
        else:
            answer += result
        print(result)
    else:
        print('Не удалось получить ответ от нейросети')
        print('Текст ошибки:', resp.json())

# import requests
# resp = requests.post( # POST запрос
#     # эндпоинт
#     'http://localhost:1234/v1/chat/completions',
#     # заголовок
#     headers={"Content-Type": "application/json"},
#     # тело запроса
#     json={
#         "messages": [
#             {"role": "user", "content": "What is the capital of France? Answer with only one word."},
#         ],
#         "temperature": 1.2,
#         "max_tokens": 10,
#     }
# )
#
# # Печатаем ответ
# print(resp.json())