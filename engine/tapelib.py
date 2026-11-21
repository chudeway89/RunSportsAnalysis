# Shared helpers for the market tape (every market on every fixture).
#   papertrade/tape/<date>[_HHMMSS_who].csv.gz   committed, append-only raw prices (tape_store.py)
#   cache/tape_graded/<kick-off date>.jsonl.gz    settled outcomes, rebuilt incrementally (tape_grade.py), not committed
import os,glob,gzip,json,re
HERE=os.path.dirname(os.path.abspath(__file__))
TAPE_DIR=os.path.join(HERE,'..','papertrade','tape')
PART_DIR=os.path.join(HERE,'cache','tape_graded')
_D=re.compile(r'(\d{4}-\d{2}-\d{2})')
def file_date(path):
    m=_D.search(os.path.basename(path)); return m[1] if m else '0000-00-00'
def tape_files():
    """Raw tape files, oldest first (file name starts with the harvest date and time, so name order = time order)."""
    return sorted(glob.glob(os.path.join(TAPE_DIR,'*.csv.gz')),key=lambda f:os.path.basename(f))
def part_path(day): return os.path.join(PART_DIR,f'{day}.jsonl.gz')
def part_days(): return sorted(file_date(f) for f in glob.glob(os.path.join(PART_DIR,'*.jsonl.gz')))
def iter_graded(days=None):
    """Yield settled outcomes one at a time, kick-off day by day; within a day rows are grouped by fixture (eid)."""
    for d in (days or part_days()):
        p=part_path(d)
        if not os.path.exists(p): continue
        with gzip.open(p,'rt') as f:
            for line in f:
                if line.strip(): yield json.loads(line)
