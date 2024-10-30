from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    start_request = State()
    full_name = State()
    phone_number = State()
    birth_year = State()
    position = State()
    region = State()
    nationality = State()
    education = State()
    experience = State()
    marriage = State()
    russian_level = State()
    english_level = State()
    other_language = State()
    first_answer = State()
    salary = State()
    second_answer = State()
    convince = State()
    driver_license = State()
    has_car = State()
    third_answer = State()
    fourth_answer = State()
    c1_program_level = State()
    fifth_answer = State()
    sixth_answer = State()
    worked_furniture = State()
    image = State()