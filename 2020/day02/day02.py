#!/usr/bin/env python3
import sys 
from pprint import pprint
from typing import List, Tuple

def generate_input(FILE: str) -> List[Tuple[int, int, str, str]]:
  ar = []
  with open(FILE, 'r') as f:
    for l in f:
      l = l.strip().split()
      low, high = map(int, l[0].split('-')) 
      letter = l[1][0]
      password = l[2]
      ar.append((low, high, letter, password))
  return ar

def solve_part1(ar: List[Tuple[int, int, str, str]]) -> int:
  res = 0
  for r in ar:
    if r[0] <= r[3].count(r[2]) <= r[1]:
      res += 1
  return res 

def solve_part2(ar: List[Tuple[int, int, str, str]]) -> int:
  res = 0
  for r in ar:
    if int(r[3][r[0]-1] == r[2]) ^ int(r[3][r[1]-1] == r[2]):
      res += 1 
  return res

def main() -> None:
  FILE = 'input02.txt'
  ar = generate_input(FILE)
  print('Part1:', solve_part1(ar))
  print('Part2:', solve_part2(ar))

if __name__ == '__main__':
  main()
  sys.exit(0)
