# def strounter(string): #сложность O(n*m)
#     for simbol in set(string):
#         counter = 0
#         for sub_symbol in string:
#             if simbol == sub_symbol:
#                 counter += 1
#         print(simbol, counter)
#
# strounter('aaaabbbccd')
#
# def strounter(string): #сложность O(n**2)
#     for simbol in string:
#         counter = 0
#         for sub_symbol in string:
#             if simbol == sub_symbol:
#                 counter += 1
#         print(simbol, counter)
#
# strounter('aaaabbbccd')

# def strounter(string):
#     syms_counter = {}
#     for symbol in string:
#         syms_counter[symbol] = syms_counter.get(symbol, 0)+ 1
#     print(syms_counter)
#
# strounter('aaaabbbccd')


