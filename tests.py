from functions.write_file_content import write_file
from functions.run_python import run_python_file


def test_write_file():
    print("\n=== Testing write_file ===\n")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)


def test_run_python():
    print("\n=== Testing run_python_file ===\n")
    # Test running a valid Python file
    result = run_python_file("calculator", "main.py")
    print(f"Test 1: run_python_file(\"calculator\", \"main.py\")\nResult:\n{result}\n")
    
    # Test running a test file
    result = run_python_file("calculator", "tests.py")
    print(f"Test 2: run_python_file(\"calculator\", \"tests.py\")\nResult:\n{result}\n")
    
    # Test running a file outside the working directory
    result = run_python_file("calculator", "../main.py")
    print(f"Test 3: run_python_file(\"calculator\", \"../main.py\")\nResult:\n{result}\n")
    
    # Test running a non-existent file
    result = run_python_file("calculator", "nonexistent.py")
    print(f"Test 4: run_python_file(\"calculator\", \"nonexistent.py\")\nResult:\n{result}\n")


def test():
    test_write_file()
    test_run_python()


if __name__ == "__main__":
    test()
