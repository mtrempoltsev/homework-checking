def isPing(line):
    line = line.rstrip()
    if line == "ping":
        return True
    if line == "pong":
        return False
    print("not ping not pong")
    quit()

n = 0
with open("/out/pingpong.txt") as file:
    line = file.readline()
    if not line:
        print("empty output")
        quit()

    last = isPing(line)
    for line in file:
        current = isPing(line)
        if last == current:
            print("failed")
            quit()
        last = current
        n += 1

if n < 500000:
    print(n, "< 1000000")
    quit()

print("ok")