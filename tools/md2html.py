import re, html, sys
src, dst = sys.argv[1], sys.argv[2]
t=open(src,encoding='utf-8').read()
def inline(s):
    s=html.escape(s,quote=False)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])',r'<em>\1</em>',s)
    return s
out=[]; i=0; L=t.split('\n')
while i<len(L):
    l=L[i]
    if l.startswith('<figure'):
        j=i
        while '</figure>' not in L[j]: j+=1
        out.append('\n'.join(L[i:j+1])); i=j+1; continue
    if l.startswith('```'):
        j=i+1; buf=[]
        while not L[j].startswith('```'): buf.append(html.escape(L[j])); j+=1
        out.append('<pre>'+'\n'.join(buf)+'</pre>'); i=j+1; continue
    m=re.match(r'(#{1,3}) (.*)',l)
    if m: n=len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i+=1; continue
    if l.strip()=='---': out.append('<hr>'); i+=1; continue
    if l.startswith('>'):
        buf=[]
        while i<len(L) and L[i].startswith('>'): buf.append(L[i][1:].strip()); i+=1
        def bq(par):
            ls=par.split('\n'); h=[]; txt=[]; li=[]
            for x in ls:
                if x.startswith('- '): li.append('<li>'+inline(x[2:])+'</li>')
                else: txt.append(x)
            r='<p>'+inline(' '.join(txt))+'</p>' if txt else ''
            return r+('<ul>'+''.join(li)+'</ul>' if li else '')
        out.append('<blockquote>'+''.join(bq(p) for p in '\n'.join(buf).split('\n\n') if p.strip())+'</blockquote>'); continue
    if l.startswith('- '):
        buf=[]
        while i<len(L) and L[i].startswith('- '): buf.append('<li>'+inline(L[i][2:])+'</li>'); i+=1
        out.append('<ul>'+''.join(buf)+'</ul>'); continue
    if l.strip()=='': i+=1; continue
    buf=[]
    while i<len(L) and L[i].strip() and not re.match(r'(#|>|- |```|<figure|---)',L[i]): buf.append(L[i]); i+=1
    out.append('<p>'+inline(' '.join(buf))+'</p>')
css='''body{max-width:720px;margin:40px auto;padding:0 20px;font:19px/1.65 Georgia,serif;color:#1a1a1a;background:#fbf9f4}
h1{font-size:2em;line-height:1.2}h2{margin-top:2.2em;border-bottom:1px solid #d8cfbd;padding-bottom:.2em}h3{margin-top:1.6em}
blockquote{margin:1.2em 0;padding:.6em 1.1em;background:#f3eee2;border-left:4px solid #8a6d3b}
figure{margin:1.8em 0;text-align:center}figure svg{max-width:100%;height:auto}figcaption{font-size:.8em;color:#555;margin-top:.5em;text-align:left}
pre{background:#f3eee2;padding:1em;overflow-x:auto;font-size:.8em}table.verbos{margin:auto;border-collapse:collapse}table.verbos td,table.verbos th{border:1px solid #d8cfbd;padding:.4em .7em;text-align:left}
hr{border:0;border-top:1px solid #d8cfbd;margin:2.5em 0}code{font-size:.85em}'''
titulo=re.search(r'^# (.*)',t,flags=re.M).group(1)
open(dst,'w',encoding='utf-8').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{html.escape(titulo)}</title><style>{css}</style></head><body>'+'\n'.join(out)+'</body></html>')
print('OK', dst)
