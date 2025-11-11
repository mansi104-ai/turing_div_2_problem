# ------------------------------------------------------------
# Problem: Pixel Compression Tree
# Author: Mansi
# ------------------------------------------------------------
# You are given n pixel intensity values (a1, a2, ..., an)
# and a spatial penalty p. Each time you merge two smallest
# pixel groups, the cost is (w1 + w2 + p). The merged group
# then has a weight of (w1 + w2). You must repeat this until
# only one group remains, and output the minimum total cost.
#
# The optimal merging process follows the same logic as
# Huffman coding, except for the constant penalty p.

# ------------------------------------------------------------
# For local testing (uncomment to debug)
# ------------------------------------------------------------
# if __name__ == "__main__":
#     import io, sys
#     input_data = """\
#     4 3
#     5 2 8 3
#     """
#     sys.stdin = io.StringIO(input_data)
#     solve()
# ------------------------------------------------------------
# Expected output: 38
# ------------------------------------------------------------

if __name__ == "__main__":
    solve()
