#!/usr/bin/env python3
"""Build portable text and a root-SKILL ZIP. Maintenance only, standard library."""
from pathlib import Path
import hashlib,json,re,zipfile
ROOT=Path(__file__).resolve().parents[1]
entry=(ROOT/'SKILL.md').read_text(encoding='utf-8')
body=entry.split('---',2)[2].lstrip()
version=re.search(r'version:\s*"([^"]+)"',entry).group(1)
refs=list(dict.fromkeys(re.findall(r'\]\((references/[^)#]+\.md)\)',body)))
assert refs and all((ROOT/x).is_file() for x in refs)
start=body.index('## 在不同 Agent 中使用');end=body.index('## 先接住当前任务',start)
body=body[:start]+'## 使用这份单文件\n\n本文件包含完整方法与参考章节，不需其他文件、命令或原始课程。按本次问题取用下方章节；整份文本读入仍会占用上下文，不能把“按需取用”理解为已经减少输入量。用户当前要求与宿主规则优先。\n\n'+body[end:]
for ref in refs:body=body.replace(']('+ref+')','](#section-'+Path(ref).stem+')')
text='# 凌酱 Skill · 通用单文件版\n\n版本 '+version+'。面向所有短视频创作者；适用于能读取完整附件或文本的Agent。\n\n'+body
for ref in refs:text+='\n\n---\n\n<a id="section-'+Path(ref).stem+'"></a>\n\n'+(ROOT/ref).read_text(encoding='utf-8')
text+='\n\n---\n\n## License\n\n'+(ROOT/'LICENSE').read_text(encoding='utf-8')+'\n'
dist=ROOT/'dist';dist.mkdir(exist_ok=True)
(dist/'lingjiang-content.md').write_text(text,encoding='utf-8')
runtime_scripts=[ROOT/'scripts'/'estimate_duration.py']
assert all(p.is_file() for p in runtime_scripts)
files=[ROOT/'SKILL.md', ROOT/'LICENSE']+sorted((ROOT/'references').glob('*.md'))+sorted((ROOT/'agents').glob('*.yaml'))+runtime_scripts
with zipfile.ZipFile(dist/'lingjiang-content.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in files:
        info=zipfile.ZipInfo(str(p.relative_to(ROOT)),date_time=(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,p.read_bytes())
manifest={'version':version,'skill_files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'artifacts':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [dist/'lingjiang-content.md',dist/'lingjiang-content.zip']},'single_file_characters':len(text),'runtime_dependencies':[],'optional_runtime_dependencies':['Python 3.9+ for scripts/estimate_duration.py']}
(dist/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'version':version,'skill_files':len(files),'single_file_characters':len(text)},ensure_ascii=False))
