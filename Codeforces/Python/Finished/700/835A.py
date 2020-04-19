chars, speed_a, speed_b, ping_a, ping_b = map(int, input().split(" "))
first = chars * speed_a + ping_a * 2
second = chars * speed_b + ping_b * 2
if first < second:
    print("First")
elif first > second:
    print("Second")
elif first == second:
    print("Friendship")