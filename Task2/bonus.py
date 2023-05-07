def get_bonus(name, salary, premium):
    yield {name[i]: salary[i] * (1 + float(premium[i][:-1]) / 100) for i in range(len(name))}
