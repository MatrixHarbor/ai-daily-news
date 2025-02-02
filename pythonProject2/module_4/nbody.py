N = 5
G = 6.67E-11
SUN = 3
#            x[i]        y[i]        vx[i]       vy[i]       m[i]
earth =     [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars =      [2.2790e+11,0.0000e+00,0.0000e+00,2.4100e+04,6.4190e+23]
mercury =   [5.7900e+10,0.0000e+00,0.0000e+00,4.7900e+04,3.3020e+23]
sun =       [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus =     [1.0820e+11,0.0000e+00,0.0000e+00,3.500e+04,4.8690e+24]

planets = [earth,mars,mercury,sun,venus]

x0, y0, vx0, vy0, m0 = sun
# x1, y1, vx1, vy1, m1 = earth
# x2, y2, vx2, vy2, m2 = mars
# x3, y3, vx3, vy3, m3 = mercury
# x4, y4, vx4, vy4, m4 = venus

t_total = 0
dt = 25000
t = 157788000
while t_total < t:
    for planet in range(len(planets)):
        # Skip the Sun by checking its mass
        if planets[planet][4] == 1.9890e+30:
            continue
        # print(planets[planet])
        # print(planets[planet][0])

        x1,y1,vx1,vy1,m1 = planets[planet] # extract current planets' values
        # print(x1,y1,vx1,vy1,m1)

        dx = x1 - x0
        dy = y1 - y0
        # print(dx)
        # print(dy)
        r = (dx**2 + dy**2)**0.5
        # print(r)
        F = G * (m1 * m0) / (r ** 2)
        # print(F)
        Fx = -F * (dx / r)
        Fy = -F * (dy / r)
        # print(Fx)
        # print(Fy)
        ax = Fx / m1
        ay = Fy / m1
        # print(ax)
        # print(ay)

        vx1 += ax * dt
        vy1 += ay * dt

        x1 += vx1 * dt
        y1 += vy1 * dt
        # print(x1)
        # print(y1)
        planets[planet] = [x1,y1,vx1,vy1,m1] # store the updated values back in the planets[planet]


    t_total += dt
for planet in range(len(planets)): # print the 5 values of every planet
    x1, y1, vx1, vy1, m1 = planets[planet] # give values to x1 y1 vx1 vy1 m1
    print(f"{x1:.4e} {y1:.4e} {vx1:.4e} {vy1:.4e} {m1:.4e}")




# Below are the wrong code that I have tried.



# for i in range(len(planets[planet])):
#     print(planets[planet][i])
# print(f'{x1:.4e} {y1:.4e} {vx1:.4e} {vy1:.4e} {m1:.4e}')

# print(f"{x1:.4e}")
# print(f"{planets[planet][1]:.4e}")
# print(f"{x1:.4e} {y1:.4e} {vx1:.4e} {vy1:.4e} {m1:.4e}")
    # print(planets[planet])
        # for i in range(len(planets[planet])):
        #     print(planets[planet][i])
        # for i in range(len(planets[planet])):
            # print(i)
            # print(planets[planet][i])


            # dx[planet] = planets[planet][0] - x0
            # dy[planet] = planets[planet][1] - y0
            # print(dx[planet])
            # print(dy[planet])
            # r = (dx**2 + dy**2)**0.5
            #
            # F = G * (planets[planet][4] - m0) / (r ** 2)
            #
            # Fx = -F * (dx / r)
            # Fy = -F * (dy / r)
            #
            # ax[i] = Fx / planets[planet][4]
            # ay[i] = Fy / planets[planet][4]
            #
            # vx[i] += ax[i] * dt
            # vy[i] += ay[i] * dt