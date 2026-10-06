from gemini import parse_message


while True:
    text = input("\nТы: ")

    if text.lower() in ("exit", "quit", "выход"):
        break

    try:
        result = parse_message(text)

        print("DeepSeek:")
        print(result)

    except Exception as error:
        print("Ошибка:", error)