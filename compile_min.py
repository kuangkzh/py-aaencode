def cpl(s):
 if isinstance(s,int):
   return "(%s*%s+%s)"%(cpl(s//256),d[256],cpl(s%256)) if s>256 else "(%s)" % '+'.join([d[2**i] for i in range(8) if 2**i&s!=0])
 else:
  return '+'.join(['((ŎдŎ)[ŏ_ŏ]+(ŎдŎ)[ˆωˆ])%%(%s)' % cpl(ord(c)) for c in s])
d={1:'(ŏ_ŏ)',2:'(ì_í)',4:'(oˇ罒ˇo)',8:'(눈_눈)',16:'(乛д乛)',32:'(oˆ_ˆo)',64:'(ಠ_ಠ)',128:'(ಥ_ಥ)',256:'ヾˆ_ˆノ*(ಥ_ಥ)'}
t="# -*- coding: utf-8 -*-\n(oˆ_ˆo)=_=33;o=(ˆωˆ)=(oˆ_ˆo)-(oˆ_ˆo);c=(ŎдŎ)=(ŏ_ŏ)=(oˆ_ˆo)// (oˆ_ˆo);(oˆ_ˆo)=(c^_^o);ヾˆ_ˆノ=(ì_í)=(ŏ_ŏ)+(ŎдŎ);(oˇ罒ˇo)=(ì_í)+ヾˆ_ˆノ;(눈_눈)=ヾˆ_ˆノ*(oˇ罒ˇo);(乛д乛)=(oˆ_ˆo)//ヾˆ_ˆノ;(ಠ_ಠ)=ヾˆ_ˆノ*(oˆ_ˆo);(ಥ_ಥ)=ヾˆ_ˆノ*(ಠ_ಠ);(ŎдŎ)={(ˆωˆ):('c'),(ŏ_ŏ):'%%>_<%%'[ˆωˆ]};(ÒωÓױ)=exec;(ÒωÓױ)(%s,(ŎдŎ))"
print("encoded:\n",t % cpl(input("enter source code:\n")))
