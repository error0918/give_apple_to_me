# 한글 문자 분해
def decompose_hangul(char):
    if not ('가' <= char <= '힣'):
        return None
    code_point = ord(char) - 0xAC00
    initial = code_point // (21 * 28)
    medial = (code_point % (21 * 28)) // 28
    final = code_point % 28
    cho = chr(0x1100 + initial)
    jung = chr(0x1161 + medial)
    jong = chr(0x11A7 + final) if final else ''
    return cho, jung, jong


# 한글 문자 합성
def compose_syllable(cho, jung, jong=''):
    if not cho or not jung:
        return ''
    cho_index = ord(cho) - 0x1100
    jung_index = ord(jung) - 0x1161
    jong_index = ord(jong) - 0x11A7 if jong else 0
    syllable_code = 0xAC00 + (cho_index * 21 * 28) + (jung_index * 28) + jong_index
    return chr(syllable_code)


# 한글 종성 특수 문자 합성
def combine_jong(jong1, jong2):
    combined_jong_mapping = {
        (to_final('ㄱ'), to_final('ㅅ')): '\u11AA',  # ᆨ + ᆺ -> ᆪ (ㄳ)
        (to_final('ㄴ'), to_final('ㅈ')): '\u11AC',  # ᆫ + ᆽ -> ᆬ (ㄵ)
        (to_final('ㄴ'), to_final('ㅎ')): '\u11AD',  # ᆫ + ᇂ -> ᆭ (ㄶ)
        (to_final('ㄹ'), to_final('ㄱ')): '\u11B0',  # ᆯ + ᆨ -> ᆰ (ㄺ)
        (to_final('ㄹ'), to_final('ㅁ')): '\u11B1',  # ᆯ + ᆷ -> ᆱ (ㄻ)
        (to_final('ㄹ'), to_final('ㅂ')): '\u11B2',  # ᆯ + ᆸ -> ᆲ (ㄼ)
        (to_final('ㄹ'), to_final('ㅅ')): '\u11B3',  # ᆯ + ᆺ -> ᆳ (ㄽ)
        (to_final('ㄹ'), to_final('ㅌ')): '\u11B4',  # ᆯ + ᇀ -> ᆴ (ㄾ)
        (to_final('ㄹ'), to_final('ㅍ')): '\u11B5',  # ᆯ + ᇁ -> ᆵ (ㄿ)
        (to_final('ㄹ'), to_final('ㅎ')): '\u11B6',  # ᆯ + ᇂ -> ᆶ (ㅀ)
        (to_final('ㅂ'), to_final('ㅅ')): '\u11B9',  # ᆸ + ᆺ -> ᆹ (ㅄ)
    }
    return combined_jong_mapping.get((jong1, jong2), None)


def to_independent(cho):
    to_independent_mapping = {
        # 독립
        '\u3131': '\u3131',  # ㄱ -> ㄱ
        '\u3132': '\u3132',  # ㄲ -> ㄲ
        '\u3134': '\u3134',  # ㄴ -> ㄴ
        '\u3137': '\u3137',  # ㄷ -> ㄷ
        '\u3138': '\u3138',  # ㄸ -> ㄸ
        '\u3139': '\u3139',  # ㄹ -> ㄹ
        '\u3141': '\u3141',  # ㅁ -> ㅁ
        '\u3142': '\u3142',  # ㅂ -> ㅂ
        '\u3143': '\u3143',  # ㅃ -> ㅃ
        '\u3145': '\u3145',  # ㅅ -> ㅅ
        '\u3146': '\u3146',  # ㅆ -> ㅆ
        '\u3147': '\u3147',  # ㅇ -> ㅇ
        '\u3148': '\u3148',  # ㅈ -> ㅈ
        '\u3149': '\u3149',  # ㅉ -> ㅉ
        '\u314A': '\u314A',  # ㅊ -> ㅊ
        '\u314B': '\u314B',  # ㅋ -> ㅋ
        '\u314C': '\u314C',  # ㅌ -> ㅌ
        '\u314D': '\u314D',  # ㅍ -> ㅍ
        '\u314E': '\u314E',  # ㅎ -> ㅎ
        # 초성
        '\u1100': '\u3131',  # ᄀ -> ㄱ
        '\u1101': '\u3132',  # ᄁ -> ㄲ
        '\u1102': '\u3134',  # ᄂ -> ㄴ
        '\u1103': '\u3137',  # ᄃ -> ㄷ
        '\u1104': '\u3138',  # ᄄ -> ㄸ
        '\u1105': '\u3139',  # ᄅ -> ㄹ
        '\u1106': '\u3141',  # ᄆ -> ㅁ
        '\u1107': '\u3142',  # ᄇ -> ㅂ
        '\u1108': '\u3143',  # ᄈ -> ㅃ
        '\u1109': '\u3145',  # ᄉ -> ㅅ
        '\u110A': '\u3146',  # ᄊ -> ㅆ
        '\u110B': '\u3147',  # ᄋ -> ㅇ
        '\u110C': '\u3148',  # ᄌ -> ㅈ
        '\u110D': '\u3149',  # ᄍ -> ㅉ
        '\u110E': '\u314A',  # ᄎ -> ㅊ
        '\u110F': '\u314B',  # ᄏ -> ㅋ
        '\u1110': '\u314C',  # ᄐ -> ㅌ
        '\u1111': '\u314D',  # ᄑ -> ㅍ
        '\u1112': '\u314E',  # ᄒ -> ㅎ
        # 종성
        '\u11A8': '\u3131',  # ᆨ -> ㄱ
        '\u11A9': '\u3132',  # ᆩ -> ㄲ
        '\u11AB': '\u3134',  # ᆫ -> ㄴ
        '\u11AE': '\u3137',  # ᆮ -> ㄷ
        '\u11AF': '\u3139',  # ᆯ -> ㄹ
        '\u11B7': '\u3141',  # ᆷ -> ㅁ
        '\u11B8': '\u3142',  # ᆸ -> ㅂ
        '\u11BA': '\u3145',  # ᆺ -> ㅅ
        '\u11BB': '\u3146',  # ᆻ -> ㅆ
        '\u11BC': '\u3147',  # ᆼ -> ㅇ
        '\u11BD': '\u3148',  # ᆽ -> ㅈ
        '\u11BE': '\u314A',  # ᆾ -> ㅊ
        '\u11BF': '\u314B',  # ᆿ -> ㅋ
        '\u11C0': '\u314C',  # ᇀ -> ㅌ
        '\u11C1': '\u314D',  # ᇁ -> ㅍ
        '\u11C2': '\u314E',  # ᇂ -> ㅎ
    }
    return to_independent_mapping.get(cho, cho)

# 독립 및 초성 문자를 종성 문자로 변환
def to_final(cho):
    to_final_mapping = {
        # 독립
        '\u3131': '\u11A8',  # ᄀ -> ᆨ (ㄱ)
        '\u3132': '\u11A9',  # ᄁ -> ᆩ (ㄲ)
        '\u3134': '\u11AB',  # ᄂ -> ᆫ (ㄴ)
        '\u3137': '\u11AE',  # ᄃ -> ᆮ (ㄷ)
        '\u3139': '\u11AF',  # ᄅ -> ᆯ (ㄹ)
        '\u3141': '\u11B7',  # ᄆ -> ᆷ (ㅁ)
        '\u3142': '\u11B8',  # ᄇ -> ᆸ (ㅂ)
        '\u3145': '\u11BA',  # ᄉ -> ᆺ (ㅅ)
        '\u3146': '\u11BB',  # ᄊ -> ᆻ (ㅆ)
        '\u3147': '\u11BC',  # ᄋ -> ᆼ (ㅇ)
        '\u3148': '\u11BD',  # ᄌ -> ᆽ (ㅈ)
        '\u314A': '\u11BE',  # ᄎ -> ᆾ (ㅊ)
        '\u314B': '\u11BF',  # ᄏ -> ᆿ (ㅋ)
        '\u314C': '\u11C0',  # ᄐ -> ᇀ (ㅌ)
        '\u314D': '\u11C1',  # ᄑ -> ᇁ (ㅍ)
        '\u314E': '\u11C2',  # ᄒ -> ᇂ (ㅎ)
        # 초성
        '\u1100': '\u11A8',  # ᄀ -> ᆨ (ㄱ)
        '\u1101': '\u11A9',  # ᄁ -> ᆩ (ㄲ)
        '\u1102': '\u11AB',  # ᄂ -> ᆫ (ㄴ)
        '\u1103': '\u11AE',  # ᄃ -> ᆮ (ㄷ)
        '\u1105': '\u11AF',  # ᄅ -> ᆯ (ㄹ)
        '\u1106': '\u11B7',  # ᄆ -> ᆷ (ㅁ)
        '\u1107': '\u11B8',  # ᄇ -> ᆸ (ㅂ)
        '\u1109': '\u11BA',  # ᄉ -> ᆺ (ㅅ)
        '\u110A': '\u11BB',  # ᄊ -> ᆻ (ㅆ)
        '\u110B': '\u11BC',  # ᄋ -> ᆼ (ㅇ)
        '\u110C': '\u11BD',  # ᄌ -> ᆽ (ㅈ)
        '\u110E': '\u11BE',  # ᄎ -> ᆾ (ㅊ)
        '\u110F': '\u11BF',  # ᄏ -> ᆿ (ㅋ)
        '\u1110': '\u11C0',  # ᄐ -> ᇀ (ㅌ)
        '\u1111': '\u11C1',  # ᄑ -> ᇁ (ㅍ)
        '\u1112': '\u11C2',  # ᄒ -> ᇂ (ㅎ)
        # 종성
        '\u11A8': '\u11A8',  # ᄀ -> ᆨ (ㄱ)
        '\u11A9': '\u11A9',  # ᄁ -> ᆩ (ㄲ)
        '\u11AB': '\u11AB',  # ᄂ -> ᆫ (ㄴ)
        '\u11AE': '\u11AE',  # ᄃ -> ᆮ (ㄷ)
        '\u11AF': '\u11AF',  # ᄅ -> ᆯ (ㄹ)
        '\u11B7': '\u11B7',  # ᄆ -> ᆷ (ㅁ)
        '\u11B8': '\u11B8',  # ᄇ -> ᆸ (ㅂ)
        '\u11BA': '\u11BA',  # ᄉ -> ᆺ (ㅅ)
        '\u11BB': '\u11BB',  # ᄊ -> ᆻ (ㅆ)
        '\u11BC': '\u11BC',  # ᄋ -> ᆼ (ㅇ)
        '\u11BD': '\u11BD',  # ᄌ -> ᆽ (ㅈ)
        '\u11BE': '\u11BE',  # ᄎ -> ᆾ (ㅊ)
        '\u11BF': '\u11BF',  # ᄏ -> ᆿ (ㅋ)
        '\u11C0': '\u11C0',  # ᄐ -> ᇀ (ㅌ)
        '\u11C1': '\u11C1',  # ᄑ -> ᇁ (ㅍ)
        '\u11C2': '\u11C2',  # ᄒ -> ᇂ (ㅎ)
    }
    return to_final_mapping.get(cho, None)



# 검색 키워드 생성
def generate_search_keywords(word):
    word = ''.join(word.split())
    keywords = []

    # 입력 과정 키워드
    buffer = ''
    idx = 0

    while idx < len(word):
        char = word[idx]
        decomposition = decompose_hangul(char)
        if decomposition:
            cho, jung, jong = decomposition

            # 초성 추가
            buffer_initial = buffer + to_independent(cho)
            if buffer_initial not in keywords:
                keywords.append(buffer_initial)

            # 초성 + 중성 조합
            syllable = compose_syllable(cho, jung)
            buffer = buffer + syllable
            if buffer not in keywords:
                keywords.append(buffer)

            # 초성 + 중성 + 종성 조합
            if jong:
                syllable_with_jong = compose_syllable(cho, jung, jong)
                buffer = buffer[:-1] + syllable_with_jong
                if buffer not in keywords:
                    keywords.append(buffer)

            # 뒷 초성과 이음 처리
            if idx + 1 < len(word):
                next_char = word[idx + 1]
                next_decomposition = decompose_hangul(next_char)
                if next_decomposition:
                    next_cho, next_jung, next_jong = next_decomposition
                    combined_jong = combine_jong(jong, to_final(next_cho))
                    if combined_jong:
                        # 복합 종성으로 결합하는 경우
                        syllable_combined = compose_syllable(cho, jung, combined_jong)
                        buffer_combined = buffer[:-1] + syllable_combined
                        if buffer_combined not in keywords:
                            keywords.append(buffer_combined)
                    elif jong == '':
                        # 복합 종성이 아니고 문자가 중성으로 끝나는 경우
                        syllable_combined = compose_syllable(cho, jung, to_final(next_cho))
                        incomplete_syllable = buffer[:-1] + syllable_combined
                        if incomplete_syllable not in keywords:
                            keywords.append(incomplete_syllable)
            idx += 1
        else:
            # 한글이 아닌 경우 그대로 추가
            buffer += char
            if buffer not in keywords:
                keywords.append(buffer)
            idx += 1

    # 초성 과정 키워드
    buffer2 = ''
    idx2 = 0
    while idx2 < len(word):
        char = word[idx2]
        decomposition = decompose_hangul(char)
        if decomposition:
            cho = decomposition[0]
            buffer2 = buffer2 + cho
            keywords.append(buffer2)
        idx2 += 1

    # 글자 부분 부분 키워드
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substr = word[i:j]
            keywords.append(substr)
    return keywords
