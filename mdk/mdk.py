import time
import matplotlib.pyplot as plt
plt.plot([])
flg = plt.gcf()
ax = plt.gca()

while True:
    numbers = []
    with open(r"C:\Users\Kul33\source\repos\servertest\servertest\bin\Debug\netcoreapp3.1\info.txt", "r") as file:
        for line in file:
                line = line.strip()
                line = line.replace(",",".")
                number = float(line)
                numbers.append(number)

    ax.clear()
    plt.title("Потребление ОЗУ")
    ax.plot(numbers)
    flg.canvas.draw()
    plt.show()

    time.sleep(5)