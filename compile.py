# -*- coding: utf-8 -*-

from OptionDict import OptionDict
import random


class CompileDict(OptionDict):
    def __init__(self, *args, **kwargs):
        super(CompileDict, self).__init__(*args, **kwargs)
        self.nums, self.strings = [], []
        self[0] = '(ˆωˆ)'
        self[1] = '(ŏ_ŏ)'
        self[2] = ['(ì_í)', 'ヾˆ_ˆノ']
        self[3] = '(oェo)'
        self[4] = '(oˇ罒ˇo)'
        self[5] = '(Θ３Θ)'
        self[7] = '(TAT)'
        self[8] = '(눈_눈)'
        self[16] = '(乛д乛)'
        self[32] = ['(oˆ_ˆo)', '(c^_^o)']
        self[33] = '(o^_^o)'
        self[64] = ['(ಠ_ಠ)']
        self[97] = '(O_o)'
        self[110] = '(QAQ)'
        self[128] = ['(ಥ_ಥ)', 'ᕕᐛᕗ']
        self[256] = '(OÅO)'
        self['-'] = "('-')"
        self['='] = "('=')"
        self['_'] = "('_')"
        self['+'] = "('+')"
        self['*'] = "('*')"
        self['c'] = "('c')"
        self['o'] = "('o')"
        self['0'] = "('0')"
        self['O'] = "('O')"
        self[' '] = "(ŎдŎ)['O_o']"
        self['e'] = "(ŎдŎ)['QAQ']"
        self['%'] = "(ŎдŎ)[ŏ_ŏ]"
        self['(Θ３Θ)'] = "'(Θ３Θ)'"
        self['(O_o)'] = "'(O_o)'"
        self['(눈_눈)'] = "'(눈_눈)'"
        self['(oェo)'] = "'(oェo)'"
        self['(ŎдŎ)'] = "'(ŎдŎ)'"
        self['(OÅO)'] = "'(OÅO)'"
        self['(TAT)'] = "'(TAT)'"
        self['(QAQ)'] = "'(QAQ)'"
        self['(ˆωˆ)'] = "'(ˆωˆ)'"
        self['(oˇ罒ˇo)'] = "'(oˇ罒ˇo)'"
        self['(ಥ_ಥ)'] = "'(ಥ_ಥ)'"
        self['(ŏ_ŏ)'] = "'(ŏ_ŏ)'"
        self['(ಠ_ಠ)'] = "'(ಠ_ಠ)'"
        self['(乛д乛)'] = "'(乛д乛)'"
        self['(ÒωÓױ)'] = "'(ÒωÓױ)'"
        self['ᕕᐛᕗ'] = "'ᕕᐛᕗ'"
        self['ヾˆ_ˆノ'] = "'ヾˆ_ˆノ'"
        self['(ì_í)'] = "'(ì_í)'"
        self['(oˆ_ˆo)'] = "'(oˆ_ˆo)'"
        self.compress_args = []
        self.template = """# -*- coding: utf-8 -*-
(oˆ_ˆo)=_=33;o=(ˆωˆ)=(oˆ_ˆo)-(oˆ_ˆo);c=(ŎдŎ)=(ŏ_ŏ)=(oˆ_ˆo)// (oˆ_ˆo);(oˆ_ˆo)=(c^_^o);ヾˆ_ˆノ=(ì_í)=(ŏ_ŏ)+(ŎдŎ);(oˇ罒ˇo)=(ì_í)+ヾˆ_ˆノ;(눈_눈)=ヾˆ_ˆノ*(oˇ罒ˇo);(乛д乛)=(oˆ_ˆo)//ヾˆ_ˆノ;(ಠ_ಠ)=ヾˆ_ˆノ*(oˆ_ˆo);(ಥ_ಥ)=ᕕᐛᕗ=ヾˆ_ˆノ*(ಠ_ಠ);(O_o)=(o^_^o)+(ಠ_ಠ);(oェo)=(ì_í)+(ŏ_ŏ);(Θ３Θ)=(ŏ_ŏ)+(oˇ罒ˇo);(OÅO)=ヾˆ_ˆノ*(ಥ_ಥ);(TAT)=(ì_í)+(Θ３Θ);(QAQ)=(Θ３Θ)+(O_o)+(눈_눈);(ŎдŎ)={(ˆωˆ):('c'),(ŏ_ŏ):'%%>_<%%'[ˆωˆ]};(ÒωÓױ)=exec;(ÒωÓױ)('(ˆωˆ)'+'='+(ŎдŎ)[ˆωˆ]+((ŎдŎ)[ŏ_ŏ]+(ŎдŎ)[ˆωˆ])%%((ヾˆ_ˆノ+(o^_^o)+ヾˆ_ˆノ*(oˆ_ˆo)+(oˇ罒ˇo)+(ŏ_ŏ)))+((ŎдŎ)[ŏ_ŏ]+(ŎдŎ)[ˆωˆ])%%(((乛д乛)+(ŏ_ŏ)+(o^_^o)+(ಠ_ಠ))),(ŎдŎ));(ŎдŎ)[ˆωˆ]=(ŎдŎ)['ˆωˆ'];(ŎдŎ)['O_o']=(ŎдŎ)[ˆωˆ](c^_^o);(ŎдŎ)['QAQ']=(ŎдŎ)[ˆωˆ]((oˇ罒ˇo)+(O_o));%s(ÒωÓױ)(%s,(ŎдŎ))
"""

    def __setitem__(self, key, value):
        super(CompileDict, self).__setitem__(key, value)
        self.nums = sorted([n for n in self.keys() if isinstance(n, int)])
        self.strings = sorted([s for s in self.keys() if isinstance(s, str)], key=len, reverse=True)

    def __getitem__(self, k) -> str:
        if isinstance(k, int):
            if k > 256:
                return "(%s*%s+%s)" % (self[k//256], self[256], self[k % 256])
            combination = []
            while k > 0:
                stat[k] = stat[k]+1 if stat.__contains__(k) else 1
                b = [n for n in self.nums if n <= k][-1]
                combination.append(super(CompileDict, self).__getitem__(b))
                k -= b
            random.shuffle(combination)
            return "(%s)" % '+'.join(combination)
        elif isinstance(k, str):
            if k in self.strings:
                return super(CompileDict, self).__getitem__(k)
            else:
                stat[k] = stat[k]+1 if stat.__contains__(k) else 1
                return '(ŎдŎ)[ˆωˆ](%s)' % self[ord(k)]

    def __call__(self, k, *args, **kwargs):
        return self.compile(k, False)

    def compress(self, words):
        subs = sorted(['(ŎдŎ)[%s]' % self[i] for i in range(2, len(words))], key=len)
        for sub, w in zip(subs, words):
            src = self.encode(w)
            if len(src) > len(sub) and not self.__contains__(w):
                self.compress_args.append('%s=%s;' % (sub, src))
                self[w] = sub

    def encode(self, code):
        encoded = '+'.join([self[k] for k in split_by_dict(code, self.strings + list(set(code)), 0)])
        return encoded

    def compile(self, code, compress=True):
        if compress:
            words = build_bpe(code)
            self.compress(sorted(words.keys(), key=words.__getitem__, reverse=True))
            encoded = self.encode(code)
        else:
            encoded = self.encode(code)
        return self.template % (''.join(self.compress_args), encoded)


def split_by_dict(s, grams, i):
    s, res = s.split(grams[i]), []
    for j in range(len(s)):
        for next_i in range(i+1, len(grams)):
            if grams[next_i] in s[j]:
                res += split_by_dict(s[j], grams, next_i)
                break
        else:
            res += s[j]
        res.append(grams[i])
    return res[:-1]


def build_bpe(s, vocab=254):
    bpe_freq = {k: s.count(k) for k in list(s)}
    while True:
        grams = sorted(bpe_freq.keys(), key=len, reverse=True)
        s_list = split_by_dict(s, grams, 0)
        bpe_freq = {k: (s_list.count(k)-1)*len(k) for k in set(s_list)}
        baseline = sorted(bpe_freq.values(), reverse=True)[vocab-1] if len(bpe_freq) >= vocab else 0
        new_grams = {}
        for i in range(len(s_list)-1):
            gram = s_list[i] + s_list[i+1]
            if (s.count(gram)-1)*len(gram) > baseline:
                new_grams[gram] = (s.count(gram)-1)*len(gram)
        bpe_freq.update(new_grams)
        if len(new_grams) == 0:
            break
    bpe_freq = {k: bpe_freq[k] for k in bpe_freq.keys() if bpe_freq[k] > 0}
    bpe_freq = {k: bpe_freq[k] for k in sorted(bpe_freq.keys(), key=bpe_freq.__getitem__, reverse=True)[:vocab]}
    # print(sorted(bpe_freq.items(), key=lambda x: x[1]))
    return bpe_freq


cmp_dict = CompileDict()
stat = {}
with open('compile_min.py', encoding='utf-8') as f:
    source = f.read()
target = cmp_dict.compile(source, True)
# print(sorted(stat.items(), key=lambda x: x[1]))
print(target)
