from hstest import CheckResult, StageTest, dynamic_test, TestedProgram
import ast, math
import re

END_RESULT = "No one is going to be lucky"
INVALID_RESULT = "No one is joining for the party"


class BillSplitterTest(StageTest):

    @dynamic_test(data=['0', '-1'])
    def test_noone(self, inp):
        pr = TestedProgram()
        pr.start()
        output = pr.execute(inp)
        lines = output.splitlines()
        non_empty_line_count = sum(1 for line in lines if line.strip())
        if non_empty_line_count != 1:
            return CheckResult.wrong('When a zero or negative input provided as a number of friends '
                                     f'your program should output only one non-empty line')
        if (re.sub(r"\s", '', INVALID_RESULT.strip().lower())
                not in re.sub(r"\s", '', output.strip().lower())):
            return CheckResult.wrong('When a zero or negative input provided as a number of friends '
                                     f'your program should output "{INVALID_RESULT}" string')
        return CheckResult.correct()

    test_data = [
        [5, ["Marc", "Jem", "Monica", "Anna", "Jason"], 100, True],
        [3, ["Jake", "Sam", "Irina"], 109, False],
        [2, ["Jake", "Sam"], 109, False],
    ]

    @dynamic_test(data=test_data)
    def test(self, num, friends, total, luckypick):
        pr = TestedProgram()
        pr.start()
        for inp in [str(num)] + friends + [str(total)]:
            pr.execute(inp)
        output = pr.execute(str('Yes' if luckypick else 'No'))
        if luckypick:
            name = output.strip().split(' ')[0].lower()
            if name not in [n.lower() for n in friends]:
                return CheckResult.wrong(
                    "Expected output is a random name from dictionary keys, but we got something else")
            else:
                return CheckResult.correct()
        if (re.sub(r"\s", '', END_RESULT.strip().lower())
                not in re.sub(r"\s", '', output.strip().lower())):
            return CheckResult.wrong('When a "No" option is provided as an input for a lucky feature '
                                     f'your program should output "{END_RESULT}" string')
        return CheckResult.correct()


if __name__ == '__main__':
    BillSplitterTest().run_tests()
