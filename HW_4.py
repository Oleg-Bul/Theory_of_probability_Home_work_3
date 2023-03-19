# В университет на факультеты A и B поступило равное количество студентов,
#  а на факультет C студентов поступило столько же, сколько на A и B вместе.
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7,
#  а для студента факультета C - 0.9.
# Студент сдал первую сессию. Какова вероятность, что он учится:
#       a). на факультете A
#       б). на факультете B
#       в). на факультете C


a = 0.8
b = 0.7
c = 0.9
faculty_a = 0.25
faculty_b = 0.25
faculty_c = 0.5

PD = faculty_a*a+faculty_b*b+faculty_c*c
print(f'Полная вероятность наступления события D, P(D) = {PD}')

# по формуле Байеса
a_given = faculty_a*a/PD
b_given = faculty_b*b/PD
c_given = faculty_c*c/PD
print(f'\nВероятность того, что студент учится на факультете А: \
{a_given:.4f} или {a_given*100:.2f} %\n'
      f'Вероятность того, что студент учится на факультете B: \
{b_given:.4f} или {b_given*100:.2f} %\n'
      f'Вероятность того, что студент учится на факультете C: \
{c_given:.4f} или {c_given*100:.2f} %')