# TODO Найдите количество книг, которое можно разместить на дискете
vol_in_mb = 1.44  # мб
vol_in_bytes = vol_in_mb * 1024 ** 2
pages = 100
str_ = 50
symbol_ = 25
vol_1_symbol = 4  # байты
count = round(vol_in_bytes / (pages * str_ * symbol_ * vol_1_symbol))
print("Количество книг, помещающихся на дискету:", count)
