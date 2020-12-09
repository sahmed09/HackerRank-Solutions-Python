"""
Answer: -3/4

*** Step 1: Rewrite the 2 lines in proper form ***

Rewrite the 2 lines as:

y = -2 + (-3/4) * x
x = -7/4 + (-3/4) * y

so b1 = -3/4 and b2 = -3/4

*** Step 2: Apply Pearson's Coefficient formula ***

Let p = pearson correlation coefficient
Let x_std = standard deviation of x
Let y_std = standard deviation of y

p = b1 (x_std / y_std)
p = b2 (y_std / x_std)

Multiplying these 2 equations together we get
p^2 = b1 * b2
p^2 = (-3/4) * (-3/4)
p^2 = 9/16
p = 3/4 or -3/4 (depending on correlation of x and y)


*** Step 3: Find out if p is positive or negative ***

Notice that both of the original line equations have negative slopes,
so x and y are negatively correlated by definition. So, p = -3/4


****** Another Way *******
The regression line of y on x is given by Y^ = bxyX + a.
bxy = r * (y_std / x_std) ------- (1)

The regression line of x on y is given by X^ = byxY + a.
byx = r * (x_std / y_std) -------- (2)

(1) * (2) => r^2 = bxy * byx

The regression line of y on x is 3x+4y+8=0. We can rewrite it as Y^ = -(3/4)*X - 2.. bxy = -(3/4)
The regression line of x on y is 4x+3y+7=0. We can rewrite it as X^ = -(3/4)*Y - 7/4.. byx = -(3/4)
r^2 = bxy * byx = -(3/4) * -(3/4) = (9/16). So, r = +- (3/4),
but the slopes are negative, so the value of r will be negative, so r = -(3/4)
"""
