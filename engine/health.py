# Step health for the scheduled workflow. Every pipeline step runs through this wrapper, so a failure is RECORDED
# (papertrade/health.json, shown in JOURNAL.md) and still lets the later steps run; the last workflow step then
# calls `health.py check`, which turns the run red if anything failed.  Before Nov 21 steps ended in
# `|| echo "... (non-fatal)"`, which hid a crash in tape_grade.py for 16 days.
#   python3 health.py reset
#   python3 health.py run <name> [--timeout SEC] -- <command ...>
#   python3 health.py check
import sys,os,json,time,subprocess,datetime as dt
HERE=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(HERE,'..','papertrade','health.json')
def load():
    try: return json.load(open(F))
    except Exception: return {'steps':{}}
def save(h):
    os.makedirs(os.path.dirname(F),exist_ok=True)
    json.dump(h,open(F+'.tmp','w'),indent=1); os.replace(F+'.tmp',F)
def main(a):
    if not a: print(__doc__ or 'usage: health.py reset|run|check'); return 2
    if a[0]=='reset':
        save({'started':dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M'),'steps':{}}); return 0
    if a[0]=='check':
        h=load(); bad=[k for k,v in h.get('steps',{}).items() if not v.get('ok')]
        for k,v in h.get('steps',{}).items(): print(f"{'ok  ' if v.get('ok') else 'FAIL'} {k:22} {v.get('seconds',0):6.0f}s {v.get('error','')[:160]}")
        return 1 if bad else 0
    if a[0]=='run':
        name=a[1]; rest=a[2:]; timeout=None
        if rest and rest[0]=='--timeout': timeout=float(rest[1]); rest=rest[2:]
        if rest and rest[0]=='--': rest=rest[1:]
        t0=time.time(); err=''
        try:
            p=subprocess.run(rest,timeout=timeout,stderr=subprocess.PIPE,text=True)
            sys.stderr.write(p.stderr or ''); rc=p.returncode
            if rc: err=' | '.join((p.stderr or '').strip().splitlines()[-3:])
        except subprocess.TimeoutExpired: rc=124; err=f'timeout after {timeout:.0f}s'
        except Exception as ex: rc=127; err=repr(ex)
        h=load(); h.setdefault('steps',{})[name]=dict(ok=rc==0,rc=rc,seconds=round(time.time()-t0,1),error=err[:500])
        save(h); print(f"[health] {name}: {'ok' if rc==0 else 'FAILED rc='+str(rc)} in {time.time()-t0:.0f}s",flush=True)
        return 0      # never stop the pipeline here; `check` fails the run at the end
    return 2
if __name__=='__main__': sys.exit(main(sys.argv[1:]))
