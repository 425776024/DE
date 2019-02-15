from src.DE_Main import *

times = 30
func = [H15, H16]
name = ['H15', 'H16']


def F1(funci, namei):
    F_V = np.zeros(times)
    Info = np.zeros(4)
    best = 10000
    worst = -10000
    success = 0
    for i in range(times):
        vi, success_tag = run(i, funci)
        success += success_tag
        if vi < best:
            best = vi
        if vi > worst:
            worst = vi
        F_V[i] = vi
    Info[0], Info[1], Info[2], Info[3] = best, np.sum(F_V) / times, worst, success / times
    print(Info, F_V)
    np.savetxt('data/v/%s.csv' % (namei), F_V)
    np.savetxt('data/i/%s_info.csv' % (namei), Info)
    print(namei, '结束')


for i in range(0, len(name)):
    fi = func[i]
    F1(fi, name[i])
