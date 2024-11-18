from . import controller
from .last_screen import end_screen
from .last_screen import gompangi_screen
from dataclasses import dataclass
from enum import Enum


# 쓰레기 대분류
class Division(Enum):
    ELECTRIC = "전자제품"
    FOOD = "음식물"
    LIVING = "생활 쓰레기"
    ETC = "기타"


# 연결 페이지
class GoPage(Enum):
    DEFAULT = lambda root, name: nav_default(root=root, name=name)  # 일반 쓰레기
    FOOD = lambda root, name: nav_food(root=root, name=name)  # 음식물 쓰레기
    PAPER = lambda root, name: nav_paper(root=root, name=name)  # 종이류
    GLASS = lambda root, name: nav_glass(root=root, name=name)  # 유리류
    METAL = lambda root, name: nav_metal(root=root, name=name)  # 금속류
    PLASTIC = lambda root, name: nav_plastic(root=root, name=name)  # 플라스틱
    BATTERY = lambda root, name: nav_battery(root=root, name=name)  # 전지류
    LIGHT = lambda root, name: nav_light(root=root, name=name)  # 형광등
    CLOTH = lambda root, name: nav_cloth(root=root, name=name)  # 의류
    SMALL_APPLIANCE = lambda root, name: nav_small_appliance(root=root, name=name)  # 소형 폐가전
    BIG_APPLIANCE = lambda root, name: nav_big_appliance(root=root, name=name)  # 대형 폐가전
    GOMPANGI = lambda root, name: nav_gompangi(root=root, name=name)  # 곰팡이가 피었나요?


@dataclass(frozen=True)
class TrashItem:
    name: str  # 쓰레기 이름
    search_keywords: list[str]  # 검색 키워드
    divisions: list[Division]  # 대분류
    go_page: GoPage  # 연결 페이지


# 일반 쓰레기
def nav_default(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="일반 쓰레기",
            content=f"일반 쓰레기에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 음식물 쓰레기
def nav_food(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="음식물 쓰레기",
            content=f"음식물 쓰레기에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 종이류
def nav_paper(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="종이류",
            content=f"종이류 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 유리류
def nav_glass(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="유리류",
            content=f"유리류에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 금속류
def nav_metal(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="금속류",
            content=f"금속류에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 플라스틱
def nav_plastic(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="플라스틱",
            content=f"플라스틱에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 전지류
def nav_battery(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="전지류",
            content=f"전지류에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 형광등
def nav_light(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="형광등",
            content=f"형광등에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 의류
def nav_cloth(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="의류",
            content=f"의류에 대한 설명입니다. 또한 여기에 {name}에 대한 설명도 들어갈 것입니다." * 10
        )
    )

# 소형 폐가전
def nav_small_appliance(root, name: str):
    print("TODO")

# 대형 폐가전
def nav_big_appliance(root, name: str):
    print("TODO")

# 곰팡이가 피었나요?
def nav_gompangi(root, name: str):
    controller.change_screen(gompangi_screen.GompangiScreen(root, name))


dataset = [
    TrashItem(
        name="사과 껍질",
        search_keywords=["사", "사과", "사과 ", "사과 껍", "사과 껍질"],
        divisions=[Division.FOOD, Division.LIVING],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="플라스틱 병",
        search_keywords=["플", "플라", "플라스", "플라스틱", "플라스틱 ", "플라스틱 병"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="신문지",
        search_keywords=["신", "신문", "신문지"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="형광등",
        search_keywords=["형", "형광", "형광등"],
        divisions=[Division.LIVING, Division.ELECTRIC],
        go_page=GoPage.LIGHT
    ),
    TrashItem(
        name="헌 옷",
        search_keywords=["헌", "헌 ", "헌 옷"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
    TrashItem(
        name="배터리",
        search_keywords=["배", "배터", "배터리"],
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.BATTERY
    ),
    TrashItem(
        name="전자레인지",
        search_keywords=["전", "전자", "전자레", "전자레인", "전자레인지"],
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="냉장고",
        search_keywords=["냉", "냉장", "냉장고"],
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.BIG_APPLIANCE
    ),
    TrashItem(
        name="유리병",
        search_keywords=["유", "유리", "유리병"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="알루미늄 캔",
        search_keywords=["알", "알루", "알루미", "알루미늄", "알루미늄 ", "알루미늄 캔"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="비닐봉지",
        search_keywords=["비", "비닐", "비닐봉", "비닐봉지"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="과일 씨앗",
        search_keywords=["과", "과일", "과일 ", "과일 씨", "과일 씨앗"],
        divisions=[Division.FOOD, Division.LIVING],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="깨진 접시",
        search_keywords=["깨", "깨진", "깨진 ", "깨진 접", "깨진 접시"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="고장난 헤어드라이어",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 헤", "고장난 헤어", "고장난 헤어드", "고장난 헤어드라", "고장난 헤어드라이", "고장난 헤어드라이어"],
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="종이컵",
        search_keywords=["종", "종이", "종이컵"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="고장난 충전기",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 충", "고장난 충전", "고장난 충전기"],
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="플라스틱 뚜껑",
        search_keywords=["플", "플라", "플라스", "플라스틱", "플라스틱 ", "플라스틱 뚜", "플라스틱 뚜껑"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="나무젓가락",
        search_keywords=["나", "나무", "나무젓", "나무젓가", "나무젓가락"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="고장난 스마트폰",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 스", "고장난 스마", "고장난 스마트", "고장난 스마트폰"],
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="기저귀",
        search_keywords=["기", "기저", "기저귀"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="종이 박스",
        search_keywords=["종", "종이", "종이 ", "종이 박", "종이 박스"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="고장난 시계",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 시", "고장난 시계"],
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="플라스틱 의자",
        search_keywords=["플", "플라", "플라스", "플라스틱", "플라스틱 ", "플라스틱 의", "플라스틱 의자"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="부러진 유리잔",
        search_keywords=["부", "부러", "부러진", "부러진 ", "부러진 유", "부러진 유리", "부러진 유리잔"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="헌 신발",
        search_keywords=["헌", "헌 ", "헌 신", "헌 신발"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
    TrashItem(
        name="고장난 컴퓨터",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 컴", "고장난 컴퓨", "고장난 컴퓨터"],
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.BIG_APPLIANCE
    ),
    TrashItem(
        name="마른 나뭇잎",
        search_keywords=["마", "마른", "마른 ", "마른 나", "마른 나뭇", "마른 나뭇잎"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="플라스틱 빨대",
        search_keywords=["플", "플라", "플라스", "플라스틱", "플라스틱 ", "플라스틱 빨", "플라스틱 빨대"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="철사",
        search_keywords=["철", "철사"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="깨진 꽃병",
        search_keywords=["깨", "깨진", "깨진 ", "깨진 꽃", "깨진 꽃병"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="과자 봉지",
        search_keywords=["과", "과자", "과자 ", "과자 봉", "과자 봉지"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="고장난 전기주전자",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 전", "고장난 전기", "고장난 전기주", "고장난 전기주전", "고장난 전기주전자"],
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="종이 서류",
        search_keywords=["종", "종이", "종이 ", "종이 서", "종이 서류"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="철제 스푼",
        search_keywords=["철", "철제", "철제 ", "철제 스", "철제 스푼"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="헌 양말",
        search_keywords=["헌", "헌 ", "헌 양", "헌 양말"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
    TrashItem(
        name="깨진 안경",
        search_keywords=["깨", "깨진", "깨진 ", "깨진 안", "깨진 안경"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="못 쓰는 리모컨",
        search_keywords=["못", "못 ", "못 쓰", "못 쓰는", "못 쓰는 ", "못 쓰는 리", "못 쓰는 리모", "못 쓰는 리모컨"],
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="음식물 찌꺼기",
        search_keywords=["음", "음식", "음식물", "음식물 ", "음식물 찌", "음식물 찌꺼", "음식물 찌꺼기"],
        divisions=[Division.FOOD, Division.LIVING],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="부러진 의자",
        search_keywords=["부", "부러", "부러진", "부러진 ", "부러진 의", "부러진 의자"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="플라스틱 장난감",
        search_keywords=["플", "플라", "플라스", "플라스틱", "플라스틱 ", "플라스틱 장", "플라스틱 장난", "플라스틱 장난감"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="고장난 선풍기",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 선", "고장난 선풍", "고장난 선풍기"],
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="종이 쇼핑백",
        search_keywords=["종", "종이", "종이 ", "종이 쇼", "종이 쇼핑", "종이 쇼핑백"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="깨진 창문",
        search_keywords=["깨", "깨진", "깨진 ", "깨진 창", "깨진 창문"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="고장난 오디오",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 오", "고장난 오디", "고장난 오디오"],
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="플라스틱 숟가락",
        search_keywords=["플", "플라", "플라스", "플라스틱", "플라스틱 ", "플라스틱 숟", "플라스틱 숟가", "플라스틱 숟가락"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="과일 껍질",
        search_keywords=["과", "과일", "과일 ", "과일 껍", "과일 껍질"],
        divisions=[Division.FOOD, Division.LIVING],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="고장난 마우스",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 마", "고장난 마우", "고장난 마우스"],
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="고장난 키보드",
        search_keywords=["고", "고장", "고장난", "고장난 ", "고장난 키", "고장난 키보", "고장난 키보드"],
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="헌 가방",
        search_keywords=["헌", "헌 ", "헌 가", "헌 가방"],
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
]
