# Slice keys shared by learn.py (which writes papertrade/learned.json) and build_tickets.py (which reads it).
import re
def band(o): return '<1.30' if o<1.3 else '1.30-1.59' if o<1.6 else '1.60-2.19' if o<2.2 else '2.20-3.99' if o<4 else '4.00+'
def side(r):
    d=r['desc'] or ''
    if d.startswith(('Over','Under')): return d.split()[0]
    m=re.match(r'(Home|Away|Draw)\b',d)
    if m and '(' in d:
        s=re.search(r'\(([+-]?[\d.]+)\)',d)
        return m[1]+(' giving' if s and float(s[1])<0 else ' receiving' if s and float(s[1])>0 else ' level')
    return d if len(d)<=24 and not re.search(r'\d',d) else 'other'
