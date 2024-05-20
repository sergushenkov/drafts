from functools import reduce

nums = [1, 2, 3, 10, 4, 5]

print(
    min(
        reduce(
            lambda a, c: (
                (c, a[0]) if c > a[0] else (a[0], c) if c > a[1] else (a[0], a[1])
            ),
            nums,
            (nums[0], nums[0]),
        )
    )
)
