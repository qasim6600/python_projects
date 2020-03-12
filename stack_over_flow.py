# perfect diamond
x = int(input("enter number = "))
k = x
for i in range(1,x,2):
    print(' '*k + "*"*i)
    k -= 1
else:
    k = k+2
    for j in range(i-2,0,-2):
        print(' '*k + "*"*j)
        k += 1
# finding the rating of user
question1 = 10*(2) - 2*(5)
question2 = 10*(10) - 10*(0)
question_points = question1 + question2
ans1 = 15*(1)
ans2 = 15*(0) + 10*(10) - 2*(0)
ans3 = 15*(0) + 10*(3) - 2*(2)
ans_points = ans1 + ans2 + ans3
total_rating = question_points + ans_points
print('total points for Questions = {} '.format(question_points))
print('total points for Answers = {} '.format(ans_points))
print('Rating of user  = {} '.format(total_rating))
print('\n')

# defining the functions

# defining the distance


def distance_compare(x,y):
    x = float(input('enter distance 1 = '))
    y = float(input('enter distance 2 = '))
    if x > y:
        print(x)
    else:
        print(y)


def swap_int(x,y):
    x = int(input('enter first number to swap = '))
    y = int(input('enter second number to swap = '))
    x = x + y
    y = x - y
    x = x - y
    print(x,y)


def float_sep(number):
    number = float(input('enter float number = '))
    x = number // 1
    y = number % 1
    y = round(y, 4)
    print('Integer part of number is {} '.format(int(x)))
    print('Float part of number is {} '.format(y))


if __name__ == '__main__':
    float_sep(89.76)
    swap_int(88,97)
    a,b = 78.9,78.6
    distance_compare(a,b)











