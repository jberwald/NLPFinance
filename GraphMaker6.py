import numpy as np
import matplotlib.pyplot as plt
#being and are is was were such respectively

month6 = [0.13432114339261744, 0.13070778814925374, 0.07757332689552239, 0.10612745647761195, 0.07967581145112783, 0.118419279481203, 0.09881274305185185, 0.07388165092481203, 0.07336617819548871, 0.06628191906666667].reverse()
month1 = [0.04722740553959732, 0.013503490843283584, 0.010485078641791044, 0.014651025000000002, 0.010671578541353383, 0.016890992511278194, 0.028585024118518522, 0.017298776984962405, 0.003468580045112782, 0.03492300662962963].reverse()
month12 = [0.23307211420335572, 0.25633622097014924, 0.09010450613432835, 0.2266902184402985, 0.18404534486466168, 0.17013743163909772, 0.1578879693925926, 0.19374364934586463, 0.17166847891729325, 0.1302754777925926].reverse()
month3 = [0.10776608001006711, 0.05320868275373134, 0.052689136082089555, 0.05807722190298507, 0.04509193318045113, 0.05772970553383458, 0.05856569325925925, 0.038111984203007515, 0.026795022864661653, 0.034749678237037035].reverse()
x = [1,2,3,4,5,6,7,8,9,10]

plt.xlabel('Readability Score Bins')
plt.ylabel('Mean Returns')
plt.title('Relative Readability Score vs. Returns')
plt.plot(x, month1, '-o', color='black', marker='^', ms=14, lw=2, alpha=1, mfc='black', label='1 Month')
plt.plot(x, month3, '-o', color='blue', marker='o', ms=10, lw=2, alpha=1, mfc='blue', label='3 Month')
plt.plot(x, month6, '-o', color='red', marker='s', ms=12, lw=2, alpha=1, mfc='red', label='6 Month')
plt.plot(x, month12, '-o', color='green', marker='*', ms=14, lw=2, alpha=1, mfc='green', label='12 Month')
plt.legend(loc=1)

plt.show()
