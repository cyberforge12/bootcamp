from vector import Vector
floats = [0.0, 1.0, 2.0, 3.0]
# print("sub", floats - [2])
vec1 = Vector(floats)
print(f"From list of floats:    {vec1.values}")
vec2 = Vector((10,15))
print(f"From range:             {vec2.values}")
vec3 = Vector(3)
print(f"From len:               {vec3.values}")

add_i = 10
add_Vec1 = Vector([10])
add_Vec2 = Vector([10.5, 10.1, 20, 30])
sub_err = Vector([1.0, 0.0])
sub1 = Vector([1.0, 2.0, 3.0, 4.0])
mul_i = 10.15
mul_vec1 = [10]
mul_vec2 = [5, 10, 15, 20]
mul_err = [10, 20]
sub_err = [1.0]
print(f"add_i:      {vec1} + {add_i} = {vec1 + add_i}")
print(f"add_Vec1:   {vec1} + {add_Vec1} = {vec1 + add_Vec1}")
print(f"add_Vec2:   {vec1} + {add_Vec2} = {vec1 + add_Vec2}")
print(f"radd:       {add_i} + {vec1} = {add_i + vec1}")
print(f"sub:        {vec1} - {sub1} = {vec1 - sub1}")
print(f"rsub:       {sub1} - {vec1} = {sub1 - vec1}")
print(f"mul_i:      {vec1} * {mul_i} = {vec1 * mul_i}")
print(f"mul_vec1:   {vec1} * {mul_vec1} = {vec1 * mul_vec1}")
print(f"mul_vec2:   {vec1} * {mul_vec2} = {vec1 * mul_vec2}")
print(f"mul_Vec_Vec:{vec1} * {vec1} = {vec1 * vec1}")
print(f"rmul_i:     {mul_i} * {vec1} = {mul_i * vec1}")
print(f"rmul_vec1:  {mul_vec1} * {vec1} = {mul_vec1 * vec1}")
print(f"rmul_vec2:  {mul_vec2} * {vec1} = {mul_vec2 * vec1}")
print(f"str:        {str(vec1)}")
print(f"repr:       {repr(vec1)}")


##Exceptions
# print(f"mul_vec_err:\t{vec1} * {mul_err} = {vec1 * mul_err}")
# print("truediv:", vec1 / 3)
# print("rtruediv:", 10 / vec1)
# print(f"rsub_err:\t{sub_err} - {vec1}:")
# print({sub_err - vec1})
# vec4 = Vector('a')
# print("sub:", vec1 - [10, 0.0])

