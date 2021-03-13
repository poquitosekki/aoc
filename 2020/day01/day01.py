#!/usr/bin/env python3
import sys
from typing import List

def generate_input(FILE: str) -> List[int]:
  ar = []
  with open(FILE, 'r') as f:
    for l in f:
      ar.append(int(l))
  return ar

def solve_part1(ar: List[int]) -> int:
  d = {}
  for i, e in enumerate(ar):
    if (2020 - e) in d:
      return (e * (2020 - e)) 
    else:
      d[e] = i
  return -1 

def solve_part2(ar: List[int]) -> int:
  for i in range(len(ar) - 2):
    for j in range(i+1, len(ar) - 1):
      for k in range(j+1, len(ar)):
        if ar[i]+ar[j]+ar[k] == 2020:
          return ar[i]*ar[j]*ar[k]
  return -1

def better_solve(ar: List[int]) -> int:
  d = {} 
  for i, e in enumerate(ar):
    if (2020 - e) in d and (2020 - (2020 - e)) in d:
      return (e * (2020 - e) * (2020 - (2020 - e)))
    else: 
      d[e] = i
  return -1

def main() -> None:
  FILE = 'input01.txt'
  ar = generate_input(FILE)
  print('Part1:', solve_part1(ar))
  print('Part2:', solve_part2(ar))
  
if __name__ == '__main__':
  main()
  sys.exit(0)
