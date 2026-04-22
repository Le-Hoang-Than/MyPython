from solution import execute_command

def test_execute_command():
    s ={1,2,3,4,5,6,7,8,9}
    # với một tập hợp số nguyên nhỏ .pop() thường sẽ loại bỏ phần tử đầu tiên
    cmd_list = [['remove', '9'], ['discard','8'],'pop']
    assert execute_command(s,cmd_list) == 28