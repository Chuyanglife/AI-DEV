# -*- coding: utf-8 -*-
# 2^1 + 2^2 + ... + 2^n µÄ‚€Î»”µ
n = int(input().strip())

if n <= 0:
    print(0)
else:
    # index = n % 4
    # Œ¦‘ª‚€Î»”µžé: index=0 -> 0, 1->2, 2->6, 3->4
    mapping = [0, 2, 6, 4]
    print(mapping[n % 4])
