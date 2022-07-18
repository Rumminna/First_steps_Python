l = int(input())
w = int(input())
h = int(input())
percent = float(input())

v = l * w * h
liters = v / 1000
percent = percent / 100
liters = liters * (1 - percent)

print(f"{liters:.3f}")
