import pytest
class Test_Demo():
     @pytest.mark.demo
     def test_demo(self):
         a = 5
         b = -1
         assert a != b
         print("我的第⼀个测试⽤例")
     @pytest.mark.smoke
     def test_two(self):
         a = 2
         b = -1
         assert a != b
         print("我的第⼆个测试⽤例")

# @pytest.mark.demo
# @pytest.mark.smoke
# def test_add_02():
#     b = 1 + 2
#     assert 0 == b