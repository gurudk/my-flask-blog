from sklearn import svm

import random
import numpy as np
import pymysql
import matplotlib.pyplot as plt
import time


def current_millisecond():
    return int(round(time.time() * 1000))


def get_max_span(arg_spans):
    max_span = 0
    max_key = 0
    for key, value in arg_spans.items():
        v_span = value[1] - value[0]
        if v_span > max_span:
            max_span = v_span
            max_key = key
    return max_key


def do_experiment():
    inputs = None
    while inputs != 'Exit':
        delays = random.randint(0, max_delays)
        if delays in spans:
            _arr = spans[delays]
            _start = _arr[0]
            _end = _arr[1]
            money = random.randint(_start, _end)
        else:
            money = random.randint(min_money, max_money)

        print('\n1)(100, 0)\n2)(' + str(money) + ',' + str(delays) + ')\n')
        print("Please Select: ")
        _start_time = current_millisecond()
        inputs = input()
        while inputs != 'Exit':
            if inputs == '1':
                print('You have choose option 1')
                if delays in spans:
                    _span = spans[delays]
                    # update the bottom value
                    _span[0] = money
                else:
                    _span = np.zeros(2)
                    _span[0] = money
                    _span[1] = max_money
                    spans[delays] = _span
                _response_time = current_millisecond() - _start_time
                with con:
                    cur = con.cursor()
                    cur.execute(
                        'INSERT INTO time_preference (ref_money, ref_delays, option_money, option_delays, '
                        'selected, user_id, experiment_id, response_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                        (ref_money, ref_delays, money, delays, 1, user_id, experiment_id, _response_time)
                    )
                    con.commit()
                    cur.close()

                break
            elif inputs == '2':
                print('Your have choose option 2')
                if delays in spans:
                    _span = spans[delays]
                    # update the top value
                    _span[1] = money
                else:
                    _span = np.zeros(2)
                    _span[1] = money
                    _span[0] = min_money
                    spans[delays] = _span

                _response_time = current_millisecond() - _start_time
                with con:
                    cur = con.cursor()
                    cur.execute(
                        'INSERT INTO time_preference (ref_money, ref_delays, option_money, option_delays, '
                        'selected, user_id, experiment_id, response_time) VALUES (%s,%s,%s,%s,%s,%s,%s, %s)',
                        (ref_money, ref_delays, money, delays, 2, user_id, experiment_id, _response_time)
                    )
                    con.commit()
                    cur.close()

                break
            else:
                print('Please Select from 1 or 2.')
                inputs = input()
                continue

        print(inputs)

    print(spans)


def draw_preference():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM time_preference")

        rows = cur.fetchall()
        red_x = []
        red_y = []
        green_x = []
        green_y = []
        X = np.zeros((len(rows), 2))
        y = np.zeros(len(rows))
        print(X.shape)
        i = 0
        for row in rows:
            X[i, 0] = row[4]
            X[i, 1] = 10000/row[3]
            y[i] = row[5]
            if 1 == row[5]:
                green_x.append(row[4])
                green_y.append(10000/row[3])
            else:
                red_x.append(row[4])
                red_y.append(10000/row[3])
            i = i + 1
            # print("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        # plt.plot(red_x, red_y, 'r.', green_x, green_y, 'g.')
        # plt.show()
        print(X)
        print(y)

        np.random.seed(0)
        order = np.random.permutation(len(rows))
        X = X[order]
        y = y[order].astype(np.float)

        clf = svm.SVC(kernel='poly', gamma='auto', verbose=True, cache_size=7000)
        clf.fit(X, y)
        plt.figure()
        plt.clf()
        plt.scatter(X[:, 0], X[:, 1], c=y, zorder=10, cmap=plt.cm.Paired,
                    edgecolor='k', s=20)

        plt.axis('tight')
        x_min = X[:, 0].min()
        x_max = X[:, 0].max()
        y_min = X[:, 1].min()
        y_max = X[:, 1].max() + 30

        XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
        Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(XX.shape)
        plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
        plt.contour(XX, YY, Z, colors=['k', 'k', 'k'],
                    linestyles=['--', '-', '--'], levels=[-5, 0, 5])
        plt.title = 'Indifference Curve'

        exp_X = np.arange(0, 11)
        plt.plot(exp_X, 100*(0.9**exp_X), 'r--',)
        plt.plot(exp_X, 100*(0.93**exp_X), 'r--',)
        plt.plot(exp_X, 100*(0.96**exp_X), 'r--',)

        plt.plot(exp_X, 100/(1 + 0.05 * exp_X), 'b--',)
        plt.plot(exp_X, 100/(1 + 0.1 * exp_X), 'b--',)
        plt.plot(exp_X, 100/(1 + 0.15 * exp_X), 'b--',)

        plt.show()


con = pymysql.connect('localhost', 'beconlab', 'beconlab', 'beconlab')

spans = {}
ref_money = 100
ref_delays = 0
min_money = 100
max_money = 500
max_delays = 10
user_id = 88
experiment_id = 88

#do_experiment()
draw_preference()










