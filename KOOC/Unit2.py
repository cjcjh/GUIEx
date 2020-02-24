def foo (id , name):
    print(id, name)
    id = name
    print(id)
    name = id
    print(name)
    return (id, name)

id = 3
name = "kim"

id, name = foo(id, name)
# foo(3, kim)
# kim
# 3


print("id = ", id, ", name = ", name)