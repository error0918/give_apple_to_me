import tkinter
import pyglet
import platform
from enum import Enum
from dataclasses import dataclass
from ui import widget
from ui.last_screen import end_screen
from util import theme, screen, controller


"""
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
def combine_jong(jong1, cho2):
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
    return combined_jong_mapping.get((jong1, cho2), None)

# 독립 및 초성 문자를 종성 문자로 변환
def to_final(choseong):
    initial_to_final_mapping = {
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
    }
    return initial_to_final_mapping.get(choseong, None)


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
            buffer_initial = buffer + cho
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
    return keywords


# 테스트 실행
words = ["랍스터", "복숭아", "머리", "고장난 냉장고", "할아버지"]
for word_ in words:
    print(f"{word_}: {generate_search_keywords(word_)}")
"""


"""
class TestScreen(screen.Screen): # 가전
    def __init__(self, root):
        self.root = root
        self.appbar = widget.AppBar(root, title="테스트 스크린", action=None)
        self.button1 = tkinter.Button(
            root,
            text = "버튼 1",
            padx=40, pady=20,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=self.button1
        )
        self.button2 = tkinter.Button(
            root,
            text = "버튼 2",
            padx=40, pady=20,
            background=theme.color_background,
            fg=theme.color_on_background,
            borderwidth=1,
            font=theme.font(size=40),
            command=self.button2
        )

    def button1(self):
        controller.change_screen(end_screen.EndScreen(self.root, title="테스트 엔드 스크린", content="테스트 엔드 스크린 내용 입니다. " * 100))

    def button2(self):
        pass

    def show(self):
        self.appbar.place()
        self.button1.place(
            x=40, y=120+40,
            width=640, height=120
        )
        self.button2.place(
            x=40, y=120+40+160,
            width=640, height=120
        )

    def hide(self):
        self.appbar.place_forget()
        self.button1.place_forget()
        self.button2.place_forget()


test_window = tkinter.Tk()

test_window.geometry("720x1080")
test_window.title("테스트 윈도우")
test_window.resizable(False, False)
test_window.config(background=theme.color_background)
pyglet.font.add_file("res/NanumSquareNeo.ttf")
controller.init(test_window)
controller.change_screen(TestScreen(test_window))

test_window.mainloop()
"""