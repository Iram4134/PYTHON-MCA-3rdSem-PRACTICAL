stu={
      "name":["IRAM"],
      "roll_no":19,
      "course":"MCA"
    }
print(stu)
del stu["roll_no"]
print(stu)
print(stu.get("name"))
print(stu.keys())
print(stu.values())
print (stu.items())
print(stu.pop("course"))
print(stu)
print(stu.popitem())
print(stu)
print(stu.setdefault("roll_no",19))
print(stu)
print(stu.setdefault("course","MCA"))
print(stu)
print(stu.update({"name":"IRAM-jan","roll_no":199,"course":"MCA_3rd"}))
print(stu)

