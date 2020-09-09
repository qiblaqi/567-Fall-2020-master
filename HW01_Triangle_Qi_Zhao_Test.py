import unittest
import HW01_Triangle_Qi_Zhao as Triangle

class TestTriangle(unittest.TestCase):
    def test_case(self):
        self.assertEqual(Triangle.classify_triangle(2,2,3),"isoceles")
        self.assertEqual(Triangle.classify_triangle(3,2,2),"isoceles")
        self.assertEqual(Triangle.classify_triangle(3,4,5),"right")
        self.assertEqual(Triangle.classify_triangle(3.0,4.0,5.0),"right")
        self.assertEqual(Triangle.classify_triangle(5,4,3),"right")
        self.assertEqual(Triangle.classify_triangle(4,5,3),"right")
        self.assertEqual(Triangle.classify_triangle(3,3,3),"equilateral")
        self.assertEqual(Triangle.classify_triangle(3.5,3.5,3.5),"equilateral")
        self.assertEqual(Triangle.classify_triangle(2,3,4),"scalene")
        self.assertEqual(Triangle.classify_triangle(4,3,2),"scalene")
        self.assertEqual(Triangle.classify_triangle(2.2,3.3,4.4),"scalene")        
    
    def test_case_2(self):
        self.assertEqual(Triangle.classify_triangle(-3,-3,-3),"not a triangle")
        self.assertEqual(Triangle.classify_triangle(0,0,0),"not a triangle")
        self.assertEqual(Triangle.classify_triangle(3,0,0),"not a triangle")
        self.assertEqual(Triangle.classify_triangle(-2,-2,3),"not a triangle")

if __name__ == '__main__':
    unittest.main()