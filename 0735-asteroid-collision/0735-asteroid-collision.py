class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack.pop()

                # Compare the sizes of the asteroids
                if abs(top) == abs(asteroid):
                    # Both asteroids explode
                    break
                elif abs(top) > abs(asteroid):
                    # The top asteroid survives, push it back to the stack
                    stack.append(top)
                    break
            else:
                stack.append(asteroid)

        return stack
