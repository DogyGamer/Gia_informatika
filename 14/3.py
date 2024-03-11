alph = [0,1,2,3,4,5,6,7,8,9,"A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for p in range(10, 36):
    for x_ in range(0, p):
        for y_ in range(0,p):
            
            x = str(alph[x_])
            y = str(alph[y_])

            f = int(f"32{x}8", base=p)
            g = int(f"{x}{x}{x}9", base=p)
            h = int(f"{y}{y}02", base=p)

            if f+g == h:

                print(y, x, p)
                print(int(f"{y}{y}{x}", base=p))
            