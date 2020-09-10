import numpy as np
import matplotlib.pyplot as plt

def estimation_coefficient(x, y):
    #Number of points
    num = np.size(x)

    #Average of x and y nelan vector
    av_x, av_y = np.mean(x), np.mean(y)

    #Cross-deviation and deviation about x
    XD_xy = np.sum(y*x) - num*av_y*av_x
    XD_xx = np.sum(y*x) - num*av_x*av_x

    #regres coefficient
    regco1 = XD_xy / XD_xx
    regco2 = av_y - regco1 * av_x

    return(regco1, regco2)

def plot_the_reg_line(x,y,b):
    plt.scatter(x, y, color= "m", marker="o", s=30)

    #respons vect
    y_predict = b[0]+b[1] * x

    #color to the regression line
    plt.plot(x, y_predict, color= "r")

    #labels
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def main():
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,3,2,5,7,8,8,9,10,12])

    
    #coeff estimation
    b= efficient_coeff(x,y)

    print("Coefficient Estimation is : \nregco1={} \
                \nregco2={}".format(regco1,regco2))

    plot_the_reg_line(x,y,b)

    if __name__ == "__main__":
        main()
