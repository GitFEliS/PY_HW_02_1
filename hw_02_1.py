import sys


def generate_latex_table(data):
    """Принимает таблицу, возвращает строку - таблицу в LaTeX"""
    cols = max(len(x) for x in data)
    latex_table = "\\begin{tabular}{|" + "c|" * cols + "}\n"
    latex_rows = ["\t\\hline\n" +
                  " & ".join(map(str, row)) + " \\\\\n" for row in data]
    latex_table += "".join(latex_rows)
    latex_table += "\n\\hline\\end{tabular}"
    return latex_table


if __name__ == "__main__":
    in_list = [x.split() for x in sys.stdin.readlines()]
    print(generate_latex_table(in_list))
