class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque

        students_queue = deque(students)
        sandwiches_stack = sandwiches

        while students_queue and sandwiches_stack:
            if students_queue[0] == sandwiches_stack[0]:
                students_queue.popleft()
                sandwiches_stack.pop(0)
            else:
                students_queue.append(students_queue.popleft())
                if all(student != sandwiches_stack[0] for student in students_queue):
                    break

        return len(students_queue)
#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/