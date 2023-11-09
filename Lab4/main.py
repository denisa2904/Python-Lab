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
    matrix[0,0] = 1
    matrix[0,1] = 2
    matrix[0,2] = 3
    matrix[1,0] = 4
    matrix[1,1] = 5
    matrix[1,2] = 6
    matrix[2,0] = 7
    matrix[2,1] = 8
    matrix[2,2] = 9
    print(matrix)
    print(matrix.transpose())
    print(matrix*matrix)


def main():
    print("Stack functions:")
    stack_functions()
    print("\nQueue functions:")
    queue_functions()
    print("\nMatrix functions:")
    matrix_functions()


if __name__ == '__main__':
    main()
