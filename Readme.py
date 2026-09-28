def min_rotations_balanced(s: str) -> int:
    n = len(s)
    
    # Helper function to check if a string is balanced
    def is_balanced(t: str) -> bool:
        countA, countB = 0, 0
        for ch in t:
            if ch == 'A':
                countA += 1
            else:
                countB += 1
            if countA < countB:  # prefix condition violated
                return False
        return countA == countB
    
    # Try all rotations
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_balanced(rotated):
            return i
    return -1
