def product_key(product):
    return (-int(product["priority"]), product["deadline"], int(product["price"]), product["id"])

def merge_sort_products(products):
    if len(products) <= 1:
        return list(products)
    mid = len(products) // 2
    left = merge_sort_products(products[:mid])
    right = merge_sort_products(products[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if product_key(left[i]) <= product_key(right[j]):
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
