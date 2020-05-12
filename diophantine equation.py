Diophantine equation is a polynomial equation. I will explain briefly what is polynomial equation. Polynomial equation contains
two or more unknown variables. For instance x and y. In this challenge, you have to find the number of x and y that match with
the result

This coding challenge I get when I faced coding interview from Devoteam. According to me, this is hard level coding challenge
if you seldom touch polynomial equation in math field. But, I'm personally think that it is medium level.

x, y = (x >=0, y >=0)

Here I give the equation and result that you have to achieve:
X^2 - 4*Y^2 = n

if there is no solution put []

solution[90005] = [[45003, 22501], [9003, 4499], [981, 467], [309, 37]]
solution[90002] = []

Lets code:

class solution():
    def diophantine_equation(self, n):
        import math
        result=[]
        for i in range(1, int(math.sqrt(n)+1)):
            if n % i == 0:
                j = n//i
                x = (j+i)//2
                y = (j-i)//4
                if (x >= 0) and (y >= 0) and (j == (x+2*y)) and (i == (x-2*y)):
                    result.append([x,y])
        return sorted(result, reverse=True)

    
n = 90005
solution().diophantine_equation(n)
