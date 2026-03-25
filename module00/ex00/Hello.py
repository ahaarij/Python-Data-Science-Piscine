ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
# change tuple
try:
    new_tuple = list(ft_tuple)
    new_tuple.remove('toto!')
    ft_tuple = tuple(new_tuple)
    country = ("UAE!",)
    ft_tuple += country
except ValueError:
    print("Error with Tuple!")

# change set

try:
    city = "Abu Dhabi!"
    ft_set.remove("tutu!")
    ft_set.add(city)
except Exception as e:
    print("Error with Set! {e}")

# change dict

try:
    ft_dict["Hello"] = "42 Abu Dhabi!"
except Exception as e:
    print("Error with Dict! {e}")


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
