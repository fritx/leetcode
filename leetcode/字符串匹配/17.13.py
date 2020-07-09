# 17.13. 恢复空格 - 中等
# https://leetcode-cn.com/problems/re-space-lcci/


# 2. 尝试建立完全树索引 - wip
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        idxDct = self.buildIndexDict(dictionary)

        N = len(sentence)
        max_reco = 0
        i = 0
        memo = {}

        def recurse(curr_sen: str, curr_reco: int) -> None:
            nonlocal max_reco, memo
            if not curr_sen:
                return
            if curr_sen in memo:
                return
            left, first = curr_sen[1:], curr_sen[0]

            recurse(left, curr_reco)
            memo[left] = 1

            p = idxDct
            while first in p:  # 首字符匹配
                left, first = first[1:], first[0]
                curr_reco += 1
                max_reco = max(max_reco, curr_reco)
                p = p[first]

            recurse(left, curr_reco)
            memo[left] = 1

        recurse(sentence, 0)
        return N - max_reco

    # 构建字典索引树
    def buildIndexDict(self, dictionary: List[str]):
        # https://blog.csdn.net/bencodeben/java/article/details/47955381
        def deepMerge(dict1, dict2) -> None:
            for key in dict2.keys():
                if key not in dict1.keys():
                    dict1[key] = dict2[key]
                else:
                    deepMerge(dict1[key], dict2[key])

        def recurse(word: str, currDct) -> None:
            if not word:
                return
            first, left = word[0], word[1:]
            nextDct = {}
            recurse(left, nextDct)
            if first in currDct:
                deepMerge(currDct[first], nextDct)
            else:
                currDct[first] = nextDct

        dct = {}
        for word in dictionary:
            recurse(word, dct)
        return dct


# 1. 暴力递归+记忆化+首字符索引(lv1) - 超时
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        indexes = {}  # 首字符 索引 level1
        for word in dictionary:
            first = word[0]
            indexes[first] = indexes[first] + \
                [word] if first in indexes else [word]

        memo = {}  # 记忆化
        reco = 0

        def recurse(s: str, acc: int) -> None:
            nonlocal reco, memo
            if not s or (s in memo and memo[s] >= acc):
                return
            memo[s] = acc
            first = s[0]
            if first in indexes:  # 首字符匹配 尝试单词匹配
                for word in indexes[first]:
                    wlen = len(word)
                    if s[0: wlen] == word:  # 单词匹配
                        # print(["matched", word, s[wlen:]])
                        reco = max(reco, acc + wlen)
                        recurse(s[wlen:], acc + wlen)  # 选择匹配单词 跳过单词
                        if not s[wlen:]:
                            # print(["break", s[wlen:], acc + wlen])
                            break
                    recurse(s[1:], acc)  # 选择不匹配单词 下一位字符
            else:
                recurse(s[1:], acc)  # 首字符不匹配 下一位字符

        recurse(sentence, 0)
        return len(sentence) - reco
