#example of random input generation
import random
import os
import subprocess
import tempfile


def fuzzer(max_length=100, char_start=32, char_range=32):
    # generate string up to max length in char-start to char-start+range
    string_length = random.randrange(1, max_length+1)

    out = ""
    for i in range(string_length):
        out += chr(random.randrange(char_start, char_start+char_range))

    return out

#only executes if we run this python file
if __name__ == "__main__":
    basename = "input.txt"
    tempdir = tempfile.mkdtemp()
    FILE = os.path.join(tempdir,basename)
    print(FILE)

    runs = []
    for i in range(100):
        #open file and write to it
        data = fuzzer()
        with open(FILE, "w") as f:
            f.write(data)

        #run BC on file
        result = subprocess.run(["bc",FILE], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        #result holds info
        runs.append((data, result))

        # clean up
    os.remove(FILE)
    os.removedirs(tempdir)

    #analyze runs
    #list computation
    correct_runs = [(data,result) for (data, result) in runs if result.stderr == ""]
    print("correct runs:", len(correct_runs))
    