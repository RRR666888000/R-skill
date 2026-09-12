#!/usr/bin/env python3
"""Validate package structure and artifacts, not creative quality or all hosts."""
from pathlib import Path
import hashlib,json,re,zipfile,tempfile,shutil,subprocess,sys
if not __debug__:raise RuntimeError("Run validation without Python -O; assertions must remain enabled.")
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
entry=(ROOT/'SKILL.md').read_text(encoding='utf-8')
assert entry.startswith('---\n') and '\n---\n' in entry[4:]
assert re.search(r'^name: lingjiang-content$',entry,re.M)
assert re.search(r'^description: .+',entry,re.M)
for p in [ROOT/'SKILL.md',*sorted((ROOT/'references').glob('*.md'))]:
    s=p.read_text(encoding='utf-8')
    assert not re.search(r'/Users/|/home/|[A-Z]:\\|file://|mcp__|tools\.exec_command',s),p
    for ref in re.findall(r'\]\(([^)]+)\)',s):
        if ref.startswith(('https://','http://','#')):continue
        target=(p.parent/ref.split('#')[0]).resolve()
        assert target.is_relative_to(ROOT) and target.is_file(),(p,ref)
m=json.loads((ROOT/'dist/manifest.json').read_text())
for rel,digest in m['skill_files'].items():assert sha(ROOT/rel)==digest,rel
for rel,digest in m['artifacts'].items():assert sha(ROOT/'dist'/rel)==digest,rel
single=(ROOT/'dist/lingjiang-content.md').read_text(encoding='utf-8')
for p in (ROOT/'references').glob('*.md'):assert p.read_text(encoding='utf-8') in single,p
anchors=set(re.findall(r'<a id="([^"]+)"',single))
assert all(x in anchors for x in re.findall(r'\]\(#([^)]+)\)',single))
assert not re.search(r'\]\((?!#|https?://)[^)]+\)',single)
with zipfile.ZipFile(ROOT/'dist/lingjiang-content.zip') as z:
    assert z.testzip() is None and set(z.namelist())==set(m['skill_files'])
    assert 'SKILL.md' in z.namelist() and 'LICENSE' in z.namelist()
    assert (ROOT/'LICENSE').read_text(encoding='utf-8') in single
    for rel in z.namelist():assert z.read(rel)==(ROOT/rel).read_bytes(),rel
    with tempfile.TemporaryDirectory(prefix='skill-relocation-') as temp:
        moved=Path(temp)/'中文 path with spaces';z.extractall(moved)
        shutil.rmtree(moved/'agents')
        assert (moved/'SKILL.md').is_file()
        for ref in re.findall(r'\]\((references/[^)#]+\.md)\)',entry):assert (moved/ref).is_file()
duration=json.loads(subprocess.check_output([sys.executable,str(ROOT/'scripts/estimate_duration.py'),'--units','418','--cpm-min','120','--cpm-max','120','--pause-seconds','3'],text=True))
assert duration['spoken_units']==418
assert duration['speech_seconds']=={'min':209.0,'max':209.0}
assert duration['total_seconds']=={'min':212.0,'max':212.0}
print(json.dumps({'version':m['version'],'structure':'pass','relative_links':'pass','artifact_hashes':'pass','root_skill_zip':'pass','portable_relocation':'pass','scope':'Static package and same-source artifacts; not model behavior, all-host discovery or real video performance.'},ensure_ascii=False))
