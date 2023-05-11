# a simple implementation of spectrum-based fault localization using
# python coverage information

# need: test file, source file, 
import collections
import argparse
import os
import importlib
import coverage
import inspect
import unittest
import math

# Class to manage fualt localization tallies
class FL:
    def __init__(self):
        # how many tests have passed/failed
        self.totalpassed = 0
        self.totalfailed = 0

        # keep track of lines executed on failed/passed tests and how many times each was executed
        # lambda returns defualt value if not found
        self.failed_lines = collections.defaultdict(lambda: 0)
        self.passed_lines = collections.defaultdict(lambda: 0)

    def passed(self, executable, missed):
        self.totalpassed += 1
        self._add_to_dict(self.passed_lines, executable, missed)

    def failed(self, executable, missed):
        self.totalfailed += 1
        self._add_to_dict(self.failed_lines, executable, missed)

    def tarantula(self, line):

        if self.totalfailed == 0 or self.totalpassed ==0:
            return None

        numerator = self.failed_lines[line] / self.totalfailed
        denom = (self.failed_lines[line] / self.totalfailed) +  (self.passed_lines[line] / self.totalpassed)

        if denom == 0:
            return None
        
        return numerator/denom

    def ochia (self, line):
        if self.totalfailed == 0 or self.totalpassed == 0:
            return None

        numerator = self.failed_lines[line]
        denom = math.sqrt(self.totalfailed * (self.failed_lines[line] + self.passed_lines[line]))

        if denom == 0:
            return None
        
        return numerator/denom
 
    def _add_line_to_dict(self, mapping, line):
        if line not in mapping:
            mapping[line] = 0
        mapping[line] += 1

    def _add_to_dict(self, mapping, executable, missed):
        # tested lines are the difference between the executable and the missed lines
        tested = set(executable).difference(set(missed))
        for l in tested:
            self._add_line_to_dict(mapping, l)
        



# create a command line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("test_file", help="path to the test file to run")
parser.add_argument("target_file", help="the file to localize")

# parse the command line arguments
args = parser.parse_args()

print(f"The test file is {args.test_file} and the target file is {args.target_file}")

# we need to import the test file as a module, index 0 doesnt have file name
module = os.path.splitext(os.path.basename(args.test_file))[0]
print(f"The module name is {module}")

# loading test module
spec = importlib.util.spec_from_file_location(module, args.test_file)
i = importlib.util.module_from_spec(spec)
spec.loader.exec_module(i)

cov = coverage.Coverage()
fl = FL()
# use inspect module to determine what is avalible to us in another module
for name, obj in inspect.getmembers(i):
    # skip everything thats not a class
    if not inspect.isclass(obj):
        continue

    # load each test with unittest
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(obj)

    #loop through tests in suite
    for test in suite:
        
        # erase any coverage information
        cov.erase()
        cov.start
        # run a test and get result
        res = test.run()
        cov.stop
        _, stmts, missing, _ = cov.analysis(args.target_file)

        if res.wasSuccessful:
            fl.passed(stmts,missing)
        else:
            fl.failed(stmts,missing)

print(f"we passed {fl.totalpassed} tests and failed {fl.totalfailed} tests")

# calculate tarantula score for each line in code
_, stmts, _, _ = cov.analysis(args.target_file)

# map each line number to its tarantula score
tarantula_scores = [
    (i, fl.tarantula(i)) for i in stmts if fl.tarantula(i) is not None
]
tarantula_scores.sort(reverse=True, key= lambda x: x[1])
print(tarantula_scores[:30])

ochiai_scores = [
    (i, fl.ochiai(i)) for i in stmts if fl.ochiai(i) is not None
]
ochiai_scores.sort(reverse=True, key= lambda x: x[1])
print(ochiai_scores[:30])
