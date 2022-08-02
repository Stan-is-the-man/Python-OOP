from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def test_constructor_with_no_course(self):
        student = Student('Stan')
        self.assertEqual("Stan", student.name)
        self.assertEqual({}, student.courses)

    def test_constructor_with__course(self):
        student = Student('Stan', {"Python": []})
        self.assertEqual("Stan", student.name)
        self.assertEqual({"Python": []}, student.courses)

    def test_enroll_if_course_name_in_courses(self):
        student = Student('Stan', {"Python": []})
        result = student.enroll("Python", ["note 1", "note 2"], "courses_notes")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note 1", "note 2"], student.courses["Python"])

    def test_enroll_if_add_course_notes_is_equal_to_y(self):
        student = Student('Stan')
        result = student.enroll("Python", ["note 1", "note 2"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note 1", "note 2"], student.courses["Python"])

    def test_enroll_if_add_course_notes_is_empty_string(self):
        student = Student('Stan')
        result = student.enroll("Python", ["note 1", "note 2"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note 1", "note 2"], student.courses["Python"])

    def test_enroll_all_ok(self):
        student = Student('Stan')
        result = student.enroll("Python", ["note 1", "note 2"], "Something")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], student.courses["Python"])

    def test_add_notes_if_course_name_in_courses(self):
        student = Student('Stan', {"Python": ["note 1"]})
        result = student.add_notes("Python", "note 2")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note 1", "note 2"], student.courses["Python"])

    def test_add_notes_if_course_name_not_in_courses_raise_exception(self):
        student = Student('Stan', {"Python": ["note 1"]})
        with self.assertRaises(Exception) as ex:
            student.add_notes("Java Script", "note 2")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_corse_in_courses(self):
        student = Student('Stan', {"Python": ["note 1"], "Java": ["note 1"]})
        result = student.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({"Java": ["note 1"]}, student.courses)

    def test_leave_corse_not_in_courses_raises_exception(self):
        student = Student('Stan', {"Python": ["note 1"], "Java": ["note 1"]})
        with self.assertRaises(Exception) as ex:
            student.leave_course("C++")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
