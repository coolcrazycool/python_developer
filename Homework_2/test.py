from korpat import patient


a = patient()
a.create("Коловрат", 'КоЛоВраТов', '9 Января 00', '+7 914 764-78', 'заграничный паспорт', '141738474')
print(a.name)
print(a.surname)
print(a.phone_numb)
print(a.birth_date)
print(a.doc_type)
print(a.doc_numb)