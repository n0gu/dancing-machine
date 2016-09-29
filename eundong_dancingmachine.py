import sys
import eundong_alphabet as ea

myInput = str()
alphabet_dict = {'a':ea.A, 'b':ea.B, 'c':ea.C, 'd':ea.D, 'e':ea.E,
                 'f':ea.F, 'g':ea.G, 'h':ea.H, 'i':ea.I, 'j':ea.J,
                 'k':ea.K, 'l':ea.L, 'm':ea.M, 'n':ea.N, 'o':ea.O,
                 'p':ea.P, 'q':ea.Q, 'r':ea.R, 's':ea.S, 't':ea.T,
                 'u':ea.U, 'v':ea.V, 'w':ea.W, 'x':ea.X, 'y':ea.Y,
                 'z':ea.Z}
output = ['','','','','']

if __name__ == '__main__':
    if len(sys.argv) > 1:
        myInput = sys.argv[1]
    else:
        myInput = raw_input("Give me a string: ")

    for alphabet in myInput:
        for i in range(5):
            output[i] += alphabet_dict[alphabet.lower()][i]
            output[i] += '0'

    for line in output:
        for alphabet in line:
            if alphabet == '0':
                sys.stdout.write(':white:')
            else:
                sys.stdout.write(':hi:')
        sys.stdout.write('\n')
