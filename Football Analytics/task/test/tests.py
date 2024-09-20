from hstest import StageTest, CheckResult, dynamic_test, TestedProgram
import ast
import os


class Football(StageTest):

    @dynamic_test()
    def check_data(self):
        if not os.path.exists("../data"):
            return CheckResult.wrong("The data directory is missing")

        if 'database.sqlite' not in os.listdir("../data/database"):
            return CheckResult.wrong("The database.sqlite file is missing from the data directory")

        return CheckResult.correct()

    @dynamic_test()
    def test_output(self):
        pr = TestedProgram()
        out = pr.start()

        answer = [
            ['FC Barcelona', 234],
            ['Real Madrid CF', 228],
            ['Celtic', 218],
            ['FC Bayern Munich', 193],
            ['Manchester United', 192]
        ]

        if not out:
            return CheckResult.wrong("Print the list of lists")

        if not ("[[" in out) or not ("]]" in out):
            return CheckResult.wrong("The output is a list of lists")

        if not out.startswith("[[") and not out.endswith("]]"):
            return CheckResult.wrong("The output is a list of lists")

        result = ast.literal_eval(out)

        if not len(result) == 5:
            return CheckResult.wrong("Print the top 5 teams with most goals")

        for row in result:
            if len(row) != 2:
                return CheckResult.wrong("The list should contain the team name and the total goals scored")

        if set(i for i, _ in result) != set(j for j, _ in answer):
            return CheckResult.wrong("There is at least one incorrect team returned")

        for v, k in zip(answer, result):
            if v != k:
                return CheckResult.wrong("The teams with most goals should come first")

        return CheckResult.correct()