"""
      1
    2   3
4   5   6   7
이렇게 생긴 이진트리를 전위, 중위, 후위순회해보자

전위, 중위, 후위라는 단어는 root 를 언제 순회하는지에 대한 의미이다.

전위: root -> left subtree -> right subtree
중위: left subtree -> root -> right subtree
후위: left subtree -> right subtree -> root

전위는 pre, 중위는 mid, 후위는 post 메서드를 보면 된다.

세 메서드는 print(idx) 를 언체 호출하느냐에 다라 차이를 둔다.

전위의 경우, root 를 먼저 찍기 때문에 print(idx) 를 실행하고, left 와 right 에 대해서 pre 메서드를 호출한다.

중위의 경우, 가장 왼쪽의 node 를 먼저 출력해야 한다.
따라서, mid(left) 를 통해 가장 왼쪽의 노드로 간 뒤, 더 이상 호출할 왼쪽 자식이 없으면, 그 때 root 를 출력한다.
그 이후 mid(right) 를 호출한다.

후위의 경우는 생략한다.

"""


def pre(idx):
    if idx > 7:
        return

    left = idx * 2
    right = idx * 2 + 1

    print(idx)
    pre(left)
    pre(right)


def mid(idx):
    if idx > 7:
        return

    left = idx * 2
    right = idx * 2 + 1

    mid(left)
    print(idx)
    mid(right)


def post(idx):
    if idx > 7:
        return

    left = idx * 2
    right = idx * 2 + 1

    post(left)
    post(right)
    print(idx)


if __name__ == '__main__':
    post(1)
