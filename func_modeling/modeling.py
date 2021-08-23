import numpy as np
import matplotlib.pyplot as plt
import datetime
from django.conf import settings

def build_plot(id, function: str, interval, step):
    # функция
    y = eval(function)
    # создаём рисунок с координатную плоскость
    fig = plt.subplots()
    # создаём область, в которой будет
    # - отображаться график
    start = datetime.now().date() - interval
    x = np.linspace(start, datetime.now(), (datetime.now().time().hour()-start.time().hour())/step)
    # значения x, которые будут отображены
    # количество элементов в созданном массиве
    # - качество прорисовки графика
    # рисуем график
    plt.plot(x, y(x))
    fig.savefig(f"{settings.MEDIA_ROOT}/{str(id)}.jpg")
    return f"{settings.MEDIA_ROOT}/default.jpg"
    #return f"{str(id)}.jpg"
