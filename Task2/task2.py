from Task2.bonus import get_bonus


def task2():
    name = ("Иван", "Андрей", "Макар", "Артем")
    salary = (10, 20, 30, 40)
    premium = ("10%", "20%", "30%", "10%")

    for first_name, sum_salary in enumerate(get_bonus(name, salary, premium)):
        print(f"{first_name} : {sum_salary}")
