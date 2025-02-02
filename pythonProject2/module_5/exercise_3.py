# N = 5
# G = 6.67E-11
# SUN = 3
# #            x[i]        y[i]        vx[i]       vy[i]       m[i]
# earth =     [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
# mars =      [2.2790e+11,0.0000e+00,0.0000e+00,2.4100e+04,6.4190e+23]
# mercury =   [5.7900e+10,0.0000e+00,0.0000e+00,4.7900e+04,3.3020e+23]
# sun =       [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
# venus =     [1.0820e+11,0.0000e+00,0.0000e+00,3.500e+04,4.8690e+24]
#
# planets = [earth,mars,mercury,sun,venus]
#
# x0, y0, vx0, vy0, m0 = sun
#
# t_total = 0
# dt = 1
# t = 2
# while t_total<t:
#     for planet in range(len(planets)):
#         if planets[planet][4] = 1.9890e+30:
#             continue
#         x1, y1, vx1, vy1, m1 = planets[planet]
#         dx = x1 - x0
#         dy = y1 - y0
#         r = (dx**2 + dy**2)**0.5
#         F = G * (m1*m0)