"""
frozensetlà một phiên bản bất biến của set.

Giống như set, nó chứa các phần tử độc nhất, không theo thứ tự và không thể thay đổi.

Khác với set, các phần tử không thể được thêm hoặc xóa khỏi một tập hợp đóng băng.
"""

"""Sử dụng frozenset()hàm tạo để tạo một frozenset từ bất kỳ iterable nào."""
# Tạo một đối tượng frozensetvà kiểm tra kiểu dữ liệu của nó:

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

"""
Method	                Shortcut	Description	
copy()	 	                        Returns a shallow copy	
difference()	        -	        Returns a new frozenset with the difference	
intersection()	        &	        Returns a new frozenset with the intersection	
isdisjoint()	 	                Returns whether two frozensets have an intersection	
issubset()	            <= / <	    Returns True if this frozenset is a (proper) subset of another	
issuperset()	        >= / >	    Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	        Returns a new frozenset with the symmetric differences	
union()	                |	        Returns a new frozenset containing the union
"""