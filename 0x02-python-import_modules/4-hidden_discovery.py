#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    d = dir(hidden_4)
    avoid = "__"

    for i in range(0, len(d)):
        if avoid not in d[i]:
            print(d[i])
