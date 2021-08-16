# -*- coding: utf-8 -*-

import re

"""
(Θ３Θ)
(O_o)
눈_눈
oェo
ŎдŎ
OÅO
TAT
QAQ
ˆωˆ
oˇ罒ˇo
ಥ_ಥ
ŏ_ŏ
ಠ_ಠ
乛д乛
ÒωÓױ
ᕕᐛᕗ
ヾˆ_ˆノ
ì_í
(oˆ_ˆo)         // 与o^_^o区分
"""

(oˆ_ˆo)=_=33                         # 33
o=(ˆωˆ)=(oˆ_ˆo)-(oˆ_ˆo)            # 0
c=(ŎдŎ)=(ŏ_ŏ)=(oˆ_ˆo)// (oˆ_ˆo)      # 1
(oˆ_ˆo)=(c^_^o)                             # 32
ヾˆ_ˆノ=(ì_í)=(ŏ_ŏ)+(ŎдŎ)          # 2
(oˇ罒ˇo)=(ì_í)+ヾˆ_ˆノ                # 4
(눈_눈)=ヾˆ_ˆノ*(oˇ罒ˇo)              # 8
(乛д乛)=(oˆ_ˆo)//ヾˆ_ˆノ              # 16
(ಠ_ಠ)=ヾˆ_ˆノ*(oˆ_ˆo)                 # 64
(ಥ_ಥ)=ᕕᐛᕗ=ヾˆ_ˆノ*(ಠ_ಠ)                   # 128
(O_o)=(o^_^o)+(ಠ_ಠ)               # 97
(oェo)=(ì_í)+(ŏ_ŏ)                  # 3
(Θ３Θ)=(ŏ_ŏ)+(oˇ罒ˇo)                # 5
(OÅO)=ヾˆ_ˆノ*(ಥ_ಥ)               # 256
(TAT)=(ì_í)+(Θ３Θ)                  # 7
(QAQ)=(Θ３Θ)+(O_o)+(눈_눈)           # 110
(ŎдŎ)={(ˆωˆ):('c'),(ŏ_ŏ):'%>_<%'[ˆωˆ]}
(ÒωÓױ)=exec
(ÒωÓױ)('(ˆωˆ)'+'='+(ŎдŎ)[ˆωˆ]+((ŎдŎ)[ŏ_ŏ]+(ŎдŎ)[ˆωˆ])%((ヾˆ_ˆノ+(o^_^o)+ヾˆ_ˆノ*(oˆ_ˆo)+(oˇ罒ˇo)+(ŏ_ŏ)))+((ŎдŎ)[ŏ_ŏ]+(ŎдŎ)[ˆωˆ])%(((乛д乛)+(ŏ_ŏ)+(o^_^o)+(ಠ_ಠ))),(ŎдŎ))
(ŎдŎ)[ˆωˆ]=(ŎдŎ)['ˆωˆ']
(ŎдŎ)['O_o']=(ŎдŎ)[ˆωˆ](c^_^o)      # ' '
(ŎдŎ)['QAQ']=(ŎдŎ)[ˆωˆ]((oˇ罒ˇo)+(O_o))     # 'e'
(ÒωÓױ)('print(1)',(ŎдŎ))

with open('template.py', encoding='utf-8') as f:
    template = re.match('[\s\S]*?"""[\s\S]*?"""([\s\S]*?)with', f.read()).group(1).strip('\n')
    template = template.replace('%', '%%').replace("(ÒωÓױ)('print(1)'", '%s(ÒωÓױ)(%s')
    template = re.sub('\n+', ';', template)
    template = re.sub('[ ]*?#.*?;', ';', template)
template = '# -*- coding: utf-8 -*-\n' + template
print(template)