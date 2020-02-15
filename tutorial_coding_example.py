import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

names = {1: "Unipolar NRZ", 2: "Unipolar RZ", 3: "Manchester coding", 4: "Differential Manchester coding"}


def line_convert(bits, no):
    ax1.grid()
    x1 = list(range(len(bits) + 1))
    x = [0]
    for i in x1[1:-1]:
        x.append(i)
        x.append(i)
    x.append(x1[-1])
    y = []
    for i in bits:
        y.append(int(i))
        y.append(int(i))
    # print(x,y)
    ax1.plot(x, y, 'r-.o')
    for i in range(len(bits)):
        ax1.text(i + 0.5, 0.5, bits[i], rotation=0, size=20,
                 ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.98, 0.96, 0.59), ))
    ax1.set_title(names[no], fontdict={'weight': 'bold', 'size': 17})


def rz_line_convert(bits, no):
    ax2.grid()
    x1 = list(range(len(bits) * 2 + 1))
    x = [0]
    for i in x1[1:-1]:
        x += [int(i), int(i)]
    x.append(x1[-1])
    y = []
    for i in bits:
        if int(i) == 1:
            y += [1, 1, 0, 0]

        elif int(i) == 0:
            y += [0, 0, 0, 0]
    ax2.plot(x, y, 'g-.^')
    j = 0
    for i in range(0, len(bits) * 2, 2):
        ax2.text(i + 1, 0.5, bits[j], rotation=0, size=20,
                 ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.98, 0.96, 0.59), ))
        j += 1
    ax2.set_title(names[no], fontdict={'weight': 'bold', 'size': 17})


def mc_line_convert(bits, no):
    ax3.grid()
    x1 = list(range(len(bits) * 2 + 1))
    x = [0]
    for i in x1[1:-1]:
        x += [int(i), int(i)]
    x.append(x1[-1])
    y = []
    for i in bits:
        if int(i) == 1:
            y += [1, 1, 0, 0]

        elif int(i) == 0:
            y += [0, 0, 1, 1]

    ax3.plot(x, y, 'b-.s')
    j = 0
    for i in range(0, len(bits) * 2, 2):
        ax3.text(i + 1, 0.5, bits[j], rotation=0, size=20,
                 ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.98, 0.96, 0.59), ))
        j += 1
    ax3.set_title(names[no], fontdict={'weight': 'bold', 'size': 17})


def differential_manchester(bits, no):
    inp1 = [int(i) for i in bits]
    li, lock, pre = [], False, ''
    for i in range(len(inp1)):
        if inp1[i] == 0 and not lock:
            li.append(-1)
            li.append(-1)
            li.append(1)
            lock = True
            pre = 'S'
        elif inp1[i] == 1 and not lock:
            li.append(1)
            li.append(1)
            li.append(-1)
            lock = True
            pre = 'Z'
        else:
            if inp1[i] == 0:
                if pre == 'S':
                    li.append(-1)
                    li.append(1)
                else:
                    li.append(1)
                    li.append(-1)
            else:
                if pre == 'Z':
                    pre = 'S'
                    li.append(-1)
                    li.append(1)
                else:
                    pre = 'Z'
                    li.append(1)
                    li.append(-1)
    j = 0
    for i in range(0, len(bits) * 2, 2):
        ax4.text(i + 1, 0.5, bits[j], rotation=0, size=20,
                 ha="center", va="center", bbox=dict(boxstyle="round", ec=(0., 0., 0.), fc=(0.98, 0.96, 0.59), ))
        j += 1
    ax4.grid()
    ax4.plot(li, color='red', drawstyle='steps-pre', marker='>')
    ax4.set_title(names[no], fontdict={'weight': 'bold', 'size': 17})


def plot(bits):
    line_convert(bits, 1)
    mc_line_convert(bits, 3)
    rz_line_convert(bits, 2)
    differential_manchester(bits, 4)
    plt.subplots_adjust(hspace=0.55)
    plt.show()


if __name__ == '__main__':
    plot(input("Enter Bits to Convert: ").strip())
