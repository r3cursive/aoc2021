#/usr/bin/env python3
test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def navigate(input,aim,horizontal,vertical):
    input_action,val = input.split()
    val=int(val)
    if input_action in "down":
        aim += val
    elif input_action in "up":
        aim -= val
    elif input_action in "forward":
        horizontal += val
        vertical+=aim*val

    return aim,horizontal,vertical




if __name__ == "__main__":
    aim=0
    horizontal=0
    vertical=0
    with open("input","r") as f:
        data = f.readlines()

    for line in data:
        aim, horizontal, vertical = navigate(line,aim,horizontal,vertical)

    print(horizontal*vertical)