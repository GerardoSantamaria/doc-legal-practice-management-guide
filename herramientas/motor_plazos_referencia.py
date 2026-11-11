import datetime as d
D=d.date.fromisoformat
def rng(a,b):
    a,b=D(a),D(b); return {a+d.timedelta(i) for i in range((b-a).days+1)}
def inh(x,cal): return x.weekday()>=5 or x in cal
def sig_habil(x,cal):
    x+=d.timedelta(1)
    while inh(x,cal): x+=d.timedelta(1)
    return x
def calc(notif,plazo,cal,tipo='H',gracia=True,prorroga=0,hasta=None):
    n=D(notif); total=plazo+prorroga
    if total==0: return 'SIN_VENCIMIENTO'
    if tipo=='H':
        x=n;c=0
        while c<total:
            x+=d.timedelta(1)
            if hasta and x>D(hasta): return 'CALENDARIO_NO_CARGADO'
            if not inh(x,cal): c+=1
    else:
        x=n+d.timedelta(total)
        if inh(x,cal): x=sig_habil(x,cal)
    g=sig_habil(x,cal) if gracia else None
    if hasta and g and g>D(hasta): return 'CALENDARIO_NO_CARGADO'
    return x.strftime('%a %d/%m/%Y'), g and g.strftime('%a %d/%m/%Y')
jun={D('2024-06-17'),D('2024-06-20'),D('2024-06-21')}
print(1,calc('2024-06-03',10,set()))
print(2,calc('2024-06-03',10,jun))
print(3,calc('2024-03-20',5,{D('2024-03-24')}))
print('3b',calc('2024-03-20',5,{D('2024-03-24'),D('2024-03-28'),D('2024-03-29'),D('2024-04-02')}))
print(4,calc('2024-07-11',5,rng('2024-07-15','2024-07-26')))
dic={D('2024-12-25')}|rng('2025-01-01','2025-01-31')
print(5,calc('2024-12-20',10,dic))
print(6,calc('2024-12-20',10,{D('2024-12-25')},hasta='2024-12-31'))
print(7,calc('2024-06-03',0,jun))
print(8,calc('2024-06-03',10,jun,gracia=False))
print(9,calc('2024-06-03',10,jun,prorroga=1))
print(10,calc('2024-06-01',3,set()))
print(11,calc('2024-06-12',5,jun,tipo='C'))
print(12,calc('2024-07-17',3,rng('2024-07-15','2024-07-26')))
