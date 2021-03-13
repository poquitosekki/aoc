#!/usr/bin/env python3
import os
from typing import List

def generate_input(FILE: str) -> List[int]:
  ar = []
  with open(FILE, 'r') as f:
    for l in f:
      ar.append(int(l))
  return ar

def solve_part1():
  pass

def solve_part2():
  pass

def main() -> None:
  FILE = 'sample0x.txt'
  ar = generate_input(FILE)
  print('Part1:', solve_part1())
  print('Part2:', solve_part2())

if __name__ == '__main__':
  main()
  sys.exit(0)
