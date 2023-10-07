class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stuck_in_queue = 0
        while stuck_in_queue < len(students):
            student = students.pop(0)
            if sandwiches[0] == student:
                sandwiches.pop(0)
                stuck_in_queue = 0
            else:
                students.append(student)
                stuck_in_queue += 1
        return stuck_in_queue
        