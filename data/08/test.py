import subprocess
import time

def run(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = process.stdout.readlines()
    code = process.wait()
    return code, out

def test(command, expected_code, expected_value):
    code, out = run(command)
    if code != expected_code:
        print 'return value', expected_code, '(expected) !=', code
        return
    if code != 0:
        return
    i = 0
    for line in out:
        try:
            if line.rstrip() != expected_value[i]:
                print expected_value[i], '(expected) !=', line.rstrip()
                return
            i += 1
        except ValueError:
            print 'invalid output'
            return
        except IndexError:
            print 'invalid output'
            return
    if i != len(expected_value):
        print 'empty output'
        return

test('./test', 1, [ ])
test('./test bad_file_name', 1, [ ])
test('./test book.txt', 0, [ '76370 the', '48013 and', '40411 to', '33586 a', '27692 he', '26901 of', '23856 was', '21252 in', '20867 i', '18207 her' ])

print 'bencmarking'
start = time.time()
run('./test book.txt')
finish = time.time()
print finish - start, 'sec'

print 'my time: 0.626339912415 sec'
