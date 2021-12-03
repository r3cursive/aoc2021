#/usr/bin/env python3
import string

test_data="""199
200
208
210
200
207
240
269
260
263"""

def count_increases(input=test_data):
    if type(input) == str:
        input = [int(i) for i in input.split("\n")]

    last=input[0]
    increase_counter=0
    for line in input:
        if line == last:
            print(f"{line} (N/A - same as last or no previous")
        elif line < last:
            print(f"{line} (decreased)")
        elif line > last:
            print(f"{line} (increased)")
            increase_counter+=1

        last=line

    return increase_counter

def sliding_window(input=test_data):
    input = [int(i) for i in input.split("\n")]
    windows = dict.fromkeys(list(string.ascii_lowercase) +
                            [letter1+letter2+letter3 for letter1 in string.ascii_lowercase
                             for letter2 in string.ascii_lowercase
                             for letter3 in string.ascii_lowercase],0)
    counter=0
    for key in windows:
        if counter+2 < len(input):
            windows[key] = input[counter]+input[counter+1]+input[counter+2]
            counter+=1
            print(f"{key}:{windows[key]}")

    return count_increases(list(windows.values()))



if __name__ == "__main__":
    with open("input","r") as f:
        data = f.read()
    print(sliding_window(data))