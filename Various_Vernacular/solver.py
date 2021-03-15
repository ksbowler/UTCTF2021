pl = "Provisionsgeschafte von Amgeordneten setzen CDU und CSU unter Druck.utflag"
ci = "Hkgxologflutleiaymt xgf Azutgkrftmtf ltmntf ERW wfr ELW wfmtk Rkweq.wmysau"

c = "wmysau{foeim_Tfusoli}"
d = {}
for i in range(len(ci)):
	d[ci[i]] = pl[i]
	d[ci[i].upper()] = pl[i].upper()
	d[ci[i].lower()] = pl[i].lower()
trans = str.maketrans(d)
print(c.translate(trans))
