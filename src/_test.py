import tkinter
import pyglet
import platform
from enum import Enum
from dataclasses import dataclass
from ui import theme
from ui import controller
from ui import screen
from ui import widget
from ui.last_screen import end_screen




































def decompose_hangul(char):
    """주어진 한글 음절을 초성, 중성, 종성의 인덱스로 분해합니다."""
    if not ('가' <= char <= '힣'):
        return None
    code_point = ord(char) - 0xAC00
    initial = code_point // (21 * 28)
    medial = (code_point % (21 * 28)) // 28
    final = code_point % 28
    return initial, medial, final

def compose_syllable(initial, medial, final=0):
    """초성, 중성, 종성의 인덱스를 조합하여 한글 음절을 생성합니다."""
    syllable_code = 0xAC00 + (initial * 21 * 28) + (medial * 28) + final
    return chr(syllable_code)

def combine_jong(jong1, cho2):
    """
    현재 음절의 종성과 다음 음절의 초성을 결합하여 복합 종성을 생성합니다.
    jong1: 호환성 종성 문자 (예: 'ㄱ')
    cho2: 호환성 초성 문자 (예: 'ㅅ')
    """
    combined_jong_mapping = {
        ('ㄱ', 'ㅅ'): 'ㄳ',
        ('ㄴ', 'ㅈ'): 'ㄵ',
        ('ㄴ', 'ㅎ'): 'ㄶ',
        ('ㄹ', 'ㄱ'): 'ㄺ',
        ('ㄹ', 'ㅁ'): 'ㄻ',
        ('ㄹ', 'ㅂ'): 'ㄼ',
        ('ㄹ', 'ㅅ'): 'ㄽ',
        ('ㄹ', 'ㅌ'): 'ㄾ',
        ('ㄹ', 'ㅍ'): 'ㄿ',
        ('ㄹ', 'ㅎ'): 'ㅀ',
        ('ㅂ', 'ㅅ'): 'ㅄ',
        # 필요에 따라 추가적인 조합을 여기에 추가할 수 있습니다.
    }
    return combined_jong_mapping.get((jong1, cho2), None)

def generate_search_keywords(word):
    """
    주어진 단어에서 검색 키워드를 생성합니다.
    """
    # 호환성 자모 목록 정의
    compat_cho_list = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
    compat_jong_list = ['', 'ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

    keywords = []
    buffer = []
    idx = 0
    length = len(word)

    while idx < length:
        char = word[idx]
        decomposition = decompose_hangul(char)

        if decomposition:
            initial, medial, final_index = decomposition
            compat_cho = compat_cho_list[initial]
            compat_jong = compat_jong_list[final_index] if final_index !=0 else ''

            # 1. 초성 추가
            buffer_initial = ''.join(buffer) + compat_cho
            if buffer_initial not in keywords:
                keywords.append(buffer_initial)

            # 2. 초성 + 중성 조합
            syllable_no_jong = compose_syllable(initial, medial)
            buffer.append(syllable_no_jong)
            current_buffer = ''.join(buffer)
            if current_buffer not in keywords:
                keywords.append(current_buffer)

            # 3. 초성 + 중성 + 종성 조합
            if final_index !=0:
                syllable_with_jong = compose_syllable(initial, medial, final_index)
                buffer[-1] = syllable_with_jong
                current_buffer = ''.join(buffer)
                if current_buffer not in keywords:
                    keywords.append(current_buffer)

            # 4. 종성과 다음 음절의 초성을 결합하여 복합 종성 처리
            if idx +1 < length:
                next_char = word[idx +1]
                next_decomposition = decompose_hangul(next_char)

                if next_decomposition:
                    next_initial, next_medial, next_final = next_decomposition
                    compat_cho2 = compat_cho_list[next_initial]
                    combined_jong = combine_jong(compat_jong, compat_cho2)

                    if combined_jong:
                        # 결합된 종성을 인덱스로 변환
                        if combined_jong in compat_jong_list:
                            combined_jong_index = compat_jong_list.index(combined_jong)
                            # 복합 종성을 사용하여 새로운 음절 생성
                            new_syllable = compose_syllable(initial, medial, combined_jong_index)
                            buffer_combined = ''.join(buffer[:-1] + [new_syllable])
                            if buffer_combined not in keywords:
                                keywords.append(buffer_combined)

                        # 종성을 결합하지 않은 경우 (예: '머ㄹ')
                        incomplete_syllable = ''.join(buffer[:-1] + [compat_jong] + [compat_cho2])
                        if incomplete_syllable not in keywords:
                            keywords.append(incomplete_syllable)
            idx +=1
        else:
            # 한글이 아닌 경우 그대로 추가
            buffer.append(char)
            current_buffer = ''.join(buffer)
            if current_buffer not in keywords:
                keywords.append(current_buffer)
            idx +=1

    return keywords

# 테스트 실행
if __name__ == "__main__":
    words = ["랍스터", "복숭아", "머리"]
    for word in words:
        print(f"{word}: {generate_search_keywords(word)}")

























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