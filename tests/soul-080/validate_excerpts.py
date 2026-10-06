"""Validate verbatim excerpts against a separately supplied user source file."""
from pathlib import Path
import argparse, hashlib, json, re, zipfile

parser=argparse.ArgumentParser()
parser.add_argument('source', type=Path)
parser.add_argument('--installed', type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parents[2]
source=args.source.read_text()
lines=source.splitlines()
mapping=json.loads((root/'tests/soul-080/source-map.json').read_text())
digest=lambda s:hashlib.sha256(s.encode()).hexdigest()
assert digest(source)==mapping['source_sha256'], 'Wrong source version'
files={'ai-context':'soul-prompt-inventory.md','method-context':'soul-source-context.md'}
for kind,name in files.items():
    actual=re.findall(r'```text\n(.*?)\n```', (root/'references'/name).read_text(), re.S)
    records=[r for r in mapping['records'] if r['kind']==kind]
    assert len(actual)==len(records), (name,'excerpt count')
    for text,r in zip(actual,records):
        expected='\n'.join(lines[r['start_line']-1:r['end_line']])
        assert text==expected and len(text)==r['characters'] and digest(text)==r['sha256'], r['label']
prompts=[]
for r in mapping['records']:
    if r['kind']=='prompt':
        text='\n'.join(lines[r['start_line']-1:r['end_line']])
        assert digest(text)==r['sha256'], r['label']
        prompts.append(text)
assert len(prompts)==6
raw='\n\n\n'.join(prompts)+'\n'
assert (root/'references/soul-questions.md').read_text()==raw
assert digest(raw)==mapping['six_prompts_sha256']=='81a78c8a8924b624331be5bd37aa80cb1e2596c36121d0ef0ccfa8c0e3fb6a5d'
common=['soul-questions.md','soul-prompt-inventory.md','soul-source-context.md','soul-workflow.md']
single=(root/'dist/lingjiang-content.md').read_text()
with zipfile.ZipFile(root/'dist/lingjiang-content.zip') as z:
    for name in common:
        content=(root/'references'/name).read_bytes()
        assert z.read('references/'+name)==content
        assert content.decode() in single
        if args.installed:
            assert (args.installed/'references'/name).read_bytes()==content
print(json.dumps({'source_records':len(mapping['records']),'six_prompts_unchanged':True,'source_and_artifacts':'pass','installed_match':bool(args.installed)}))
