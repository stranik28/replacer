from fastapi import FastAPI

app = FastAPI()


async def remove_non_digits(input_string):
    digits_only = ""

    for char in input_string:
        if char.isdigit():
            digits_only += char

    return digits_only


async def remove_non_letters(input_string):
    letters_only = ""

    for char in input_string:
        if char.isalpha():
            letters_only += char

    return letters_only


async def remove_letters_and_digits(input_string):
    symbols_only = ""

    for char in input_string:
        if not char.isalpha() and not char.isdigit() and not char.isspace():
            symbols_only += char

    return symbols_only


@app.get("/only_digit/{data}")
async def only_digit(data: str):
    return await remove_non_digits(data)


@app.get("/only_words/{data}")
async def only_words(data: str):
    return await remove_non_letters(data)


@app.get("/only_chars/{data}")
async def only_chars(data: str):
    return await remove_letters_and_digits(data)


@app.post("/only_digit/")
async def only_digit(data: str):
    return await remove_non_digits(data)


@app.post("/only_words/")
async def only_words(data: str):
    return await remove_non_letters(data)


@app.post("/only_chars/")
async def only_chars(data: str):
    return await remove_letters_and_digits(data)
