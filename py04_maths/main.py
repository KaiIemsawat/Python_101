import math

friend = 0;

friend = friend + 1;
friend += 1;

print(friend);

friend -= 1;

print(friend);

friend = friend * 3;
friend *= 2;
print(friend)

friend = friend / 2;
friend /= 3;

print(friend);

friend += 1;
print(friend);


friend = friend ** 2;
print(friend);

friend **= 3;
print(friend);

remain_friend = friend%3;
print(remain_friend)

print("---")

x = math.pi;
y = -4;
z = 5;

result = round(x)
round_with_decimal = round(x, 3)
# result = abs(y);
# result = pow(3, 3);
# result = max(x, y, z);
# result = min(x, y, z);
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x);


print(result)
print(round_with_decimal)
print("----")

radius = float(input("Enter the radius of a circle : "));
circumference = 2 * math.pi * radius;

print(f"The circumference i : {round(circumference, 2)}");

print("===")

a = 3;
print(math.pow(a, 3));
b = 9;
print(math.sqrt(b))