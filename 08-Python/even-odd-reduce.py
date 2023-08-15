import functools

nos_list = [3, 1, 4, 2, 5]

def count_even_odd(result, number):
    if number % 2 == 0:
        result['even'] += 1
    else:
        result['odd'] += 1
    return result

number_stats = functools.reduce(count_even_odd, nos_list, {'even' : 0, 'odd' : 0})
print(number_stats)