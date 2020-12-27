import difflib
import os
import subprocess
from tempfile import mkstemp

import click
from termcolor import colored


def diff(old, new, display=True):
    if not isinstance(old, list):
        old = (str(old)).splitlines()
    if not isinstance(new, list):
        new = (str(new)).splitlines()

    line_types = {" ": "white", "-": "red", "+": "green", "?": "pink"}

    if display:
        for line in difflib.Differ().compare(old, new):
            if line.startswith("?") or line.startswith(" "):
                continue
            print()
            print(colored(line, line_types[line[0]]))

    return old != new


def list_split(command):
    res = []
    for i in command.split(" "):
        res.append(i)
    return res


def main(precommand, *args, **kwargs):
    if precommand:
        os.system(precommand)

    tests_count = int(kwargs["count"] or 100)
    executables_exist = True
    try:
        generator = kwargs["testcase_generator"] or "generator"
        with open(generator, encoding="utf-8") as f:
            print(colored(f"testcase generator accesible as `{f.name}`", "green"))
    except:
        executables_exist = False
        print(colored("could not access testcase generator", "red"))

    try:
        bruteforce = kwargs["bruteforce"] or "bruteforce"
        with open(bruteforce, encoding="utf-8") as f:
            print(colored(f"bruteforce executable accesible as `{f.name}`", "green"))
    except:
        executables_exist = False
        print(colored("could not access bruteforce executable", "red"))

    try:
        optimized = kwargs["optimized"] or "optimized"
        with open(optimized, encoding="utf-8") as f:
            print(colored(f"optimized executable accesible as `{f.name}`", "green"))
    except:
        executables_exist = False
        print(colored("could not access optimized executable", "red"))

    if not executables_exist:
        print(
            (
                "Could not access some executables, make sure they exist "
                "and path is provided in '.cpcrc' "
                "or in the command as a flag. Type `cpc -h` for help."
            )
        )
        exit(1)

    print("Initializing tests...")
    for test in range(tests_count):
        with open(f"./{generator}") as f:
            generator_process = subprocess.run(
                [f.name], stdout=subprocess.PIPE, shell=True
            )

            generated_input = generator_process.stdout.decode("utf-8")

        with open(f"./{bruteforce}") as f:
            bruteforce_process = subprocess.Popen(
                [f.name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True
            )
            bruteforce_process.stdin.write(generated_input.encode("utf-8"))
            bruteforce_process.stdin.close()
            bruteforce_output = (
                bruteforce_process.stdout.read().decode("utf-8").splitlines()
            )

        with open(f"./{optimized}") as f:
            optimized_process = subprocess.Popen(
                [f.name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True
            )
            optimized_process.stdin.write(generated_input.encode("utf-8"))
            optimized_process.stdin.close()
            optimized_output = (
                optimized_process.stdout.read().decode("utf-8").splitlines()
            )

        if not diff(bruteforce_output, optimized_output):
            print(".", end="")
        else:
            print(colored(f"Failed for input:\n{generated_input}", "red"))
            no_halt = kwargs["no_halt"] if kwargs["no_halt"] is not None else False
            if not no_halt:
                exit(1)

    print(colored("\nAll tests ran successfully!\n", "green"))


if __name__ == "__main__":
    main()
