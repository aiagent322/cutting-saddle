import re
fp='fr/selle-cutting-acheter.html'
c=open(fp,encoding='utf-8').read()
c=re.sub(r'https://cuttingsaddles\.com','https://www.cuttingsaddles.com',c)
old='</form>\n  </div>\n</div>\n\n<footer class="site-'
new='</form>\n  </div>\n</div>\n</div>\n</div>\n\n<footer class="site-'
c=c.replace(old,new,1)
open(fp,'w',encoding='utf-8').write(c)
mp='saddle-matchmaker.html'
m=open(mp,encoding='utf-8').read()
m=m.replace('</script>\n</body>\n</html>\n\n<script>\nvar answers','</script>\n\n<script>\nvar answers',1)
open(mp,'w',encoding='utf-8').write(m)
import glob
tb=0
for f in glob.glob('**/*.html',recursive=True):
    if '.git' in f: continue
    x=re.sub(r'<script.*?</script>','',open(f,errors='ignore').read(),flags=re.DOTALL)
    x=re.sub(r'<style.*?</style>','',x,flags=re.DOTALL)
    for t in ['html','body','div']:
        if len(re.findall(r'<'+t+r'[\s>]',x))!=len(re.findall(r'</'+t+r'>',x)): tb+=1; print('IMBALANCE',f,t)
print('tag imbalances:',tb)
print('fr www ok:', 'https://cuttingsaddles.com' not in open(fp).read())
print('matchmaker clean:', open(mp,errors='ignore').read().rfind('</html>')==open(mp,errors='ignore').read().find('</html>'))
