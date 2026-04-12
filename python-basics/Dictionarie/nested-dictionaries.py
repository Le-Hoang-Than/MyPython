"""Một từ điển có thể chứa các từ điển khác, điều này được gọi là từ điển lồng nhau."""
# Tạo một từ điển chứa ba từ điển con:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Tạo ba từ điển, sau đó tạo một từ điển chứa cả ba từ điển kia:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

"""
Để truy cập các mục từ một từ điển lồng nhau, sử dụng tên của các từ điển, bắt đầu từ từ điển bên ngoài:
"""

# In tên của  child2:

print(myfamily["child2"]["name"])

# Lặp qua các khóa và giá trị của tất cả các từ điển lồng nhau:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])