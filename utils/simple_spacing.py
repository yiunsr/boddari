from konlpy.tag import Mecab
mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")

def is_next_spacing(pos, next_pos, word, next_word):
    next_josa = False
    next_comma = False
    next_vcp_or_vcn = False
    if next_pos and next_pos.startswith("J"):
        next_josa = True
    if next_word and next_word == ",":
        next_comma = True
    if next_pos and next_pos in ["VCP", "VCN"]:
        next_vcp_or_vcn = True

    # 맨 마지막 조사
    if pos.startswith("J") and next_josa is False and next_comma is False:
        return True
    # 의존 명사, 단위를 나타내는 의존명사
    elif pos in ["NNB", "NNBC"] \
            and next_josa is False and next_vcp_or_vcn is False:
        return True
    # 관형형 전성 어미,  ~하'는'
    elif pos == "ETM":
        return True
    # 연결 어미
    elif pos.endswith("EC") and next_comma is False:
        return True
    # 마침표, 물음표, 느낌표
    elif pos == "SF":
        return True
    # 콤마
    elif pos == "SC" and word == ",":
        return True
    # 일반부사, 접속부사
    elif pos in ["MAG", "MAJ"]:
        return True
    # 관형사형 접속어미 (XSV+ETM)도 포함하기 위해
    elif pos.endswith("ETM"):
        return True
    # 관형사
    elif pos == "MM":
        return True

    # next_pos 에 의해 결정되는 경우
    # MAJ
    elif next_pos == "MAJ":
        return True
    # [눈 씻고] 찾다.
    elif pos in ["NNG"] and next_pos == "VV":
        return True
    return False

def re_spacing(sen):
    pos_tags = mecab.pos(sen)
    new_sen = ""
    for idx, pos_tag in enumerate(pos_tags):
        next_word = None
        next_pos = None
        if idx + 1 < len(pos_tags):
            next_pos_tag = pos_tags[idx+1]
            next_word = next_pos_tag[0]
            next_pos = next_pos_tag[1]
        word = pos_tag[0]
        pos = pos_tag[1]
        if is_next_spacing(pos, next_pos, word, next_word):
            new_sen += word + " "
        else:
            new_sen += word
    return new_sen


sen = """
도호쿠 지방 태평양 해역 지진은 2011년 3월 11일 14시 46분 18.1초(JST) 미야기 현 앞바다에서 일어난 지진이다."""
# sen = """이제 이 별명은 더 이상 유지할 수 없어 보인다."""
re_sen = re_spacing(sen)
print(re_sen)
