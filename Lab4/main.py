from ex1 import Stack
from ex2 import Queue
from ex3 import Matrix


def stack_functions():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())


def queue_functions():
    queue = Queue()
    queue.push(4)
    queue.push(5)
    queue.push(6)
    print(queue)
    queue.pop()
    print(queue)
    print(queue.peek())


def matrix_functions():
    matrix = Matrix(3, 3)
    for i in range(3):
        for j in range(3):
            matrix[i, j] = i + j + 1
    print(matrix)
    print(matrix.transpose())
    print(matrix * matrix)


def main():
    print("Stack functions:")
    stack_functions()
    print("\nQueue functions:")
    queue_functions()
    print("\nMatrix functions:")
    matrix_functions()


if __name__ == '__main__':
    main()
