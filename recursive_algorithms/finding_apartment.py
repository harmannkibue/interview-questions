blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    },
]

requirements = ["gym", "school", "store"]

"""
[[0, 1, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1]]
"""


def find_block(blocks):
    final_block = []
    count = 0
    dist = []
    for index1, value in enumerate(blocks):
        print("The block passed ", value, index1)
        for index2, value2 in enumerate(value):
            if value2 == 0:
                for i in blocks[index1:]:
                    if i[index2] == 1:
                        dist.append(blocks.index(i) - index1)
                        print("THE dist ", dist)
        dist = []
    final_block.append(dist)
    print("FInal ", final_block)

    return None


def blocks_to_matrix(blocks, requirements):
    block_arr = []
    for i in blocks:
        inner_list = []
        for j in i:
            if i[j]:
                inner_list.append(1)
            else:
                inner_list.append(0)
        block_arr.append(inner_list)
        inner_list = []

    return find_block(block_arr)


print(blocks_to_matrix(blocks, requirements))

"""
[[0, 1, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 1, 1]]
"""
