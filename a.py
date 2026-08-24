import re, json, glob
c=open('index.html',encoding='utf-8').read()
def fx(m): return '<script type="application/ld+json">'+re.sub(r'<a href="[^"]*">([^<]*)</a>',r'\1',m.group(1))+'</script>'
open('index.html','w',encoding='utf-8').write(re.sub(r'<script type="application/ld\+json">(.*?)</script>',fx,c,flags=re.DOTALL))
I=re.compile(r'(&#\d+;|[\d\u00bc\u00bd\u00be])"(?![,:}\]])')
def fi(m): return '<script type="application/ld+json">'+I.sub(r'\1\\"',m.group(1))+'</script>'
for fp in glob.glob('used-saddles/*.html'):
    x=open(fp,encoding='utf-8').read()
    open(fp,'w',encoding='utf-8').write(re.sub(r'<script type="application/ld\+json">(.*?)</script>',fi,x,flags=re.DOTALL))
h=open('history.html',encoding='utf-8').read().replace('<title>Cutting Saddle History | Ranch Origins to <a href="ncha-competition.html">NCHA competition</a></title>','<title>Cutting Saddle History | Ranch Origins to NCHA Competition</title>')
open('history.html','w',encoding='utf-8').write(h)
m=open('saddle-matchmaker.html',encoding='utf-8').read().replace('https://cuttinghorsesaddles.com/saddle-matchmaker.html','https://www.cuttingsaddles.com/saddle-matchmaker.html')
open('saddle-matchmaker.html','w',encoding='utf-8').write(m)
for fp in [f for f in glob.glob('**/*.html',recursive=True) if '.git' not in f]:
    x=open(fp,encoding='utf-8',errors='ignore').read(); o=x; x=re.sub(r'cowhorsesaddle\.com','cowhorsessaddles.com',x)
    if x!=o: open(fp,'w',encoding='utf-8').write(x)
def al(fp,d):
    x=open(fp,encoding='utf-8').read()
    if 'application/ld+json' in x: return
    b='<script type="application/ld+json">\n'+json.dumps(d,ensure_ascii=False)+'\n</script>'
    open(fp,'w',encoding='utf-8').write(x.replace('</head>',b+'\n</head>',1))
al('contact.html',{"@context":"https://schema.org","@type":"ContactPage","name":"Contact David Solum","url":"https://www.cuttingsaddles.com/contact.html","mainEntity":{"@type":"Person","name":"David Solum","jobTitle":"Certified Used Saddle Specialist","telephone":"+1-417-793-1403","email":"davidsolumsales@gmail.com","worksFor":{"@type":"Organization","name":"CuttingSaddles.com"}}})
al('saddle-matchmaker.html',{"@context":"https://schema.org","@type":"WebApplication","name":"Cutting Saddle Matchmaker","url":"https://www.cuttingsaddles.com/saddle-matchmaker.html","applicationCategory":"BusinessApplication","operatingSystem":"Web"})
c4=open('404.html',encoding='utf-8').read()
im=sorted(glob.glob('images/saddles/*.png')+glob.glob('images/saddles/*.jpg'))
if im and 'og:image' not in c4: c4=re.sub(r'(<link rel="canonical"[^>]*>)',r'\1\n<meta property="og:image" content="https://www.cuttingsaddles.com/'+im[0]+'">',c4,count=1)
if 'application/ld+json' not in c4: c4=c4.replace('</head>','<script type="application/ld+json">\n'+json.dumps({"@context":"https://schema.org","@type":"WebPage","name":"Page Not Found","url":"https://www.cuttingsaddles.com/404.html"},ensure_ascii=False)+'\n</script>\n</head>',1)
open('404.html','w',encoding='utf-8').write(c4)
print('metadata fixes applied')
