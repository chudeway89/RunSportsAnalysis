import json, subprocess, math, time
SID={'football':'sr:sport:1','basketball':'sr:sport:2','baseball':'sr:sport:3'}
H=['-A','Mozilla/5.0 (Linux; Android 12; SM-G991B)','-H','Accept: application/json',
   '-H','Origin: https://www.sportybet.com','-H','Referer: https://www.sportybet.com/ng/',
   '-H','X-Requested-With: XMLHttpRequest']
def curl_get(url,tries=3):
    """GET a SportyBet JSON endpoint. Returns {} on any failure (timeout, bad JSON), never raises: one slow
    response must not kill a whole harvest thread pool."""
    for i in range(tries):
        try:
            r=subprocess.run(['curl','-s','-m','40']+H+[url],capture_output=True,text=True,timeout=50)
            d,_=json.JSONDecoder().raw_decode(r.stdout); return d
        except Exception: time.sleep(2*(i+1))
    return {}
def curl_post(payload,tries=2):
    for i in range(tries):
        try:
            r=subprocess.run(['curl','-s','-m','40','-X','POST']+H+['-H','Content-Type: application/json','-d',json.dumps(payload),
               'https://www.sportybet.com/api/ng/orders/share'],capture_output=True,text=True,timeout=50)
            d,_=json.JSONDecoder().raw_decode(r.stdout); return d
        except Exception: time.sleep(3)
    return {}
def sel(l):
    s={'eventId':l['eid'],'marketId':l['mid'],'outcomeId':l['oid'],'productId':3,'sportId':l['sid']}
    if l.get('spec'): s['specifier']=l['spec']
    return s
def post_ticket(legs,name):
    d=curl_post({'selections':[sel(l) for l in legs],'stake':100,'orderType':1})
    code=d.get('data',{}).get('shareCode')
    # verify
    v=curl_get(f'https://www.sportybet.com/api/ng/orders/share/{code}') if code else {}
    n=len(v.get('data',{}).get('outcomes',[])) if v else 0
    odds=math.prod(l['odds'] for l in legs)
    print(name,code,'legs',len(legs),'verified_events',n,'odds %.1f'%odds)
    return code

_B=None
def board():
    global _B
    if _B is None: _B=json.load(open('board.json'))
    return _B
def ev(team):
    m=[x for x in board() if team.lower() in (x['home']+' v '+x['away']).lower()]
    assert len(m)==1,(team,[(x['home'],x['away']) for x in m])
    return m[0]
def leg(team,mid,out,spec=None,note=''):
    x=ev(team)
    d=curl_get(f"https://www.sportybet.com/api/ng/factsCenter/event?eventId={x['eid']}&productId=3")
    for m in d['data']['markets']:
        if str(m['id'])==str(mid) and (spec is None or m.get('specifier')==spec):
            for o in m['outcomes']:
                if o['desc']==out:
                    return {'eid':x['eid'],'sid':x['sid'],'mid':str(mid),'oid':o['id'],'spec':m.get('specifier') or None,
                            'odds':float(o['odds']),'p':float(o.get('probability') or 0),'active':o.get('isActive',1),
                            'fx':x['home']+' v '+x['away'],'tour':x['tour'],'start':x['start'],'pick':f"{m.get('desc')} {out}".strip(),'note':note}
    raise Exception(('no market',team,mid,out,spec))
