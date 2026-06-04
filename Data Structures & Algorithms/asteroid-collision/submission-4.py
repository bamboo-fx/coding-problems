class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # collision only happens when left is positive and right is negative
        # while collision is possible, 3 scenarios, either remove stack, either keep stack,
        # or remove stack and add current asteroid
        # loop through asteroids, check while this is happening, while conditions
        # are while stack, while the positive and negative
        # return stack
        stack = [asteroids[0]]

        # ok basically solution here is just verify if asteroid survives,
        # an asteroid will either die or get appended
        for i in range(1, len(asteroids)):
            alive = True
            while alive and stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(asteroids[i])
            

            # here we exit the while loop, but we decide not to add the asteroid
            # but im having trouble figuring out logic when to add when to not
            # we should only append to stack if 
            
        return stack