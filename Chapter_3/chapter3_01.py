from typing import Union

def print_name_x_times(name: str, times: int) -> None:
    for _ in range(times):
        print(name)

text: str = "John"

x: str | int = ""