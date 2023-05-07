def fibonachi(final_value: int):
    fibo = [0, 1]
    while final_value > 0:
        yield fibo[-1]
        fibo.append(fibo[-1] + fibo[-2])
        final_value -= 1