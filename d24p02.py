import z3

inputdata = open('d24i01.txt', 'r')
lines = inputdata.readlines()

hailstones = []

for line in lines:
    (px, py, pz) = [int(x) for x in line.split(' @ ')[0].split(', ')]
    (vx, vy, vz) = [int(x) for x in line.split(' @ ')[1].split(', ')]
    hailstones.append(((px, py, pz), (vx, vy, vz)))


rpx, rpy, rpz, rvx, rvy, rvz = z3.Reals("rpx rpy rpz rvx rvy rvz")
solver = z3.Solver()
for k, hs in enumerate(hailstones[:3]):
    tK = z3.Real(f"t{k}")
    solver.add(tK > 0)
    solver.add(rpx + tK * rvx == hs[0][0] + tK * hs[1][0])
    solver.add(rpy + tK * rvy == hs[0][1] + tK * hs[1][1])
    solver.add(rpz + tK * rvz == hs[0][2] + tK * hs[1][2])
solver.check()
total = sum(solver.model()[var].as_long() for var in [rpx, rpy, rpz])
m = solver.model()
#print(m[z3.Real('t0')])
#print(m[z3.Real('t1')])
#print(m[z3.Real('t2')])
#print(m[rpx])
#print(m[rpy])
#print(m[rpz])
print(total)
