#!/usr/bin/env python3
import sys 
from typing import List
from pprint import pprint

def generate_input(FILE: str) -> List[str]:
  ar = []
  with open(FILE, 'r') as f:
    for l in f:
      ar.append(l[:-1])
  return ar

def solve_part1(grid: List[str], right: int, bottom: int) -> int:
  x,y = 0,0
  res = 0
  width = len(grid[0])

  while y < len(grid) - 1:
    x += right
    y += bottom

    if x >= width:
      x -= width

    if grid[y][x] == '#':
      res += 1

  return res

def solve_part2(grid: List[str], right: int, bottom: int) -> int:
  pass

def main() -> None:
  FILE = 'input03.txt'
  ar = generate_input(FILE)
  print('Part1:', solve_part1(ar, 3, 1))
  # print('Part2:', solve_part2())

if __name__ == '__main__':
  main()
  sys.exit(0)
