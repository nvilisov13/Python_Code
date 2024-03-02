import random
from matplotlib.pyplot import *


def graph() -> None:
    name_list = ['apple', 'orange', 'lemon', 'raspberry', 'pineapple', 'grape', 'pear', 'watermelon',
                 'melon', 'currant']
    num_list = [random.randrange(0, 100) for i in range(10)]
    print(name_list)
    print(num_list)
    title('Fruits')
    xlabel('Fruits')
    ylabel('Count')
    bar(name_list, num_list, color='orange')
    show()
    ion()


print(time.strftime('%d.%m.%Y %H:%m', time.localtime()))
time.sleep(1)
graph()
