# http://codeforces.com/contest/785/problem/A

n = int(input())

polyhedron = {'Tetrahedron': 4,
              'Cube': 6,
              'Octahedron': 8,
              'Dodecahedron': 12,
              'Icosahedron': 20}

ans = 0

for i in range(n):

    ans += polyhedron[input()]

print(ans)
