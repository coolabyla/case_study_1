from datetime import datetime, date

a = input('Введите дату в формате дд-мм-гг')
b = '25-09-2009'
a = a.split('-')
b = b.split('-')
aa = datetime(int(a[2]),int(a[1]),int(a[0]))
bb = datetime(int(b[2]),int(b[1]),int(b[0]))
cc = aa-bb
dd=cc.total_seconds()
print(cc) # прошедшие дни
print( 16637000000-int(dd*38241/3600), 'мили\n')
print( (16637000000-int(dd*38241/3600)*1.60934), 'километры\n')
print( (16637000000-int(dd*38241/3600)*1.60934/149597871), 'астрономические единицы\n')
print( (16637000000-int(dd*38241/3600)*1609.34)/299792458, 'задержка связи\n')