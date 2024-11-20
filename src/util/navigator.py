from dataclasses import dataclass
from enum import Enum
from typing import Union
from ui.last_screen import end_screen, gompangi_screen
from util import hangul, controller


# 쓰레기 대분류
class Division(Enum):
    FOOD = "음식물"
    ELECTRIC = "전자제품"
    LIVING = "생활 쓰레기"
    ETC = "기타"


# 쓰레기 소분류
class SubDivision(Enum):
    # 소분류 = (소분류 이름, 소속 대분류)
    ROOT_VEGETABLES = ("뿌리채소", Division.FOOD)
    WHOLE_VEGETABLES = ("통채소", Division.FOOD)
    NUCLEAR_FRUIT = ("핵과류", Division.FOOD)
    FRUITS = ("과일", Division.FOOD)
    CRUSTACEANS = ("갑각류", Division.FOOD)
    SEAFOOD = ("어패류", Division.FOOD)


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
            content="""1. 오염물질이 묻은 모든 종이류, 인쇄가 되어있는 모든 종이류, 코팅된 모든 종이류는 종량제 봉투에 담아 일반쓰레기로 배출합니다.
2. 박스를 포함한 골판지류의 경우 테이프와 송장 스티커 등의 이물질을 제거한 후 납작하게 접어서 배출합니다.
3. 신문, 책자류는 스프링을 포함한 종이 외의 다른 재질을 제거하고 배출하는 것이 바람직합니다.

유리류 배출방법
1. 깨지지 않은 유리병의 경우 물로 씻어 이물질을 제거하고 라벨을 떼어낸 후 배출합니다.
2. 깨진 유리병, 판유리, 조명기구용 유리류는 신문지에 감싸 종량제봉투에 담아 일반쓰레기로 배출합니다. """
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
            content="""1. 캔류(음류수 캔, 통조림 캔)
처리방법:
- 캔 내부를 깨끗하게 헹구고, 부착된 라벨은 제거 후 배출
- 종량제 봉투에 넣지 말고 분리수거함의 '캔류'에 배출.

2. 철제류(못, 철사, 옷걸이, 낡은 프라이팬, 냄비)
처리방법:
- 고철은 따로 분류하여 폐기
- 크기가 크고 무거운 경우 대형 폐기물 스티커를 부착 후 지정 장소에 배출

3. 비철금속류(구리 배관,전선 )
- 전문 재활용 업체 또는 고철 수집소에 가져다줌
- 소량의 경우 고철과 함께 묶어서 배출 가능

4. 알루미늄류(호일, 도시락용 알루미늄 용기, 일회용 접시)
- 기름기나 음식물이 묻은 경우 세척 후 배출
- 심하게 오염되거나 너무 얇아 재활용이 불가능한 겨우 일반 쓰레기로 폐기

주의사항
- 금속류는 분리배출 시 이물질 제거와 재질 분류가 필수
- 크기와 상태에 따라 일반 쓰레기 또는 대형 폐기물로 처리해야 할 수 있으니, 지역별 규정을 확인"""
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
            content="""1. 직선형 긴 형광등 (기본 형광등, 사무실 조명에 주로 사용)
처리 방법:
- 깨지지 않게 주의하여 배출.
- 가까운 폐형광등 수거함에 배출.

2. 특수 형광등 (자외선 램프, 식물 재배용 형광등, 살균램프)
처리 방법:
- 일부 특수 형광등(특히 UV 램프)은 일반 수거함이 아닌 전문 처리 업체를 통해 배출.
- 사용설명서를 확인하거나 지역 폐기물 처리 센터에 문의.

3. 깨진 형광등
처리 방법:
- 깨진 상태로는 재활용 불가.
- 신문지나 종이에 조각을 감싸고 밀폐된 봉투에 넣어 종량제 봉투로 배출.

주의사항
- 형광등 수거함은 아파트, 주민센터, 대형마트, 재활용센터 등에 비치.
- 형광등 내부에 포함된 수은은 유해물질이므로 깨뜨리지 않도록 주의."""
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


@dataclass
class TrashItem:
    name: str  # 쓰레기 이름
    divisions: list[Union[Division, SubDivision]]  # 대분류
    go_page: GoPage  # 연결 페이지
    @property
    def search_keywords(self) -> list[str]:
        return hangul.generate_search_keywords(self.name)


# 데이터셋
dataset = [
    # 음식물
    TrashItem(
        name="무",
        divisions=[SubDivision.ROOT_VEGETABLES],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="고구마",
        divisions=[SubDivision.ROOT_VEGETABLES],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="당근",
        divisions=[SubDivision.ROOT_VEGETABLES],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="배추",
        divisions=[SubDivision.WHOLE_VEGETABLES],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="상추",
        divisions=[SubDivision.WHOLE_VEGETABLES],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="시금치",
        divisions=[SubDivision.WHOLE_VEGETABLES],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="자두",
        divisions=[SubDivision.NUCLEAR_FRUIT],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="살구",
        divisions=[SubDivision.NUCLEAR_FRUIT],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="체리",
        divisions=[SubDivision.NUCLEAR_FRUIT],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="복숭아",
        divisions=[SubDivision.NUCLEAR_FRUIT],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="바나나",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="사과",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="귤",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="포도",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="딸기",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="새우",
        divisions=[SubDivision.CRUSTACEANS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="게",
        divisions=[SubDivision.CRUSTACEANS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="랍스터",
        divisions=[SubDivision.CRUSTACEANS],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="고등어",
        divisions=[SubDivision.SEAFOOD],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="연어",
        divisions=[SubDivision.SEAFOOD],
        go_page=GoPage.FOOD
    ),
    TrashItem(
        name="멸치",
        divisions=[SubDivision.SEAFOOD],
        go_page=GoPage.FOOD
    ),

    # SAMPLES
    TrashItem(
        name="플라스틱 병",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="신문지",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="형광등",
        divisions=[Division.LIVING, Division.ELECTRIC],
        go_page=GoPage.LIGHT
    ),
    TrashItem(
        name="헌 옷",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
    TrashItem(
        name="배터리",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.BATTERY
    ),
    TrashItem(
        name="전자레인지",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="냉장고",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.BIG_APPLIANCE
    ),
    TrashItem(
        name="유리병",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="알루미늄 캔",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="비닐봉지",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="깨진 접시",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="고장난 헤어드라이어",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="종이컵",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="고장난 충전기",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="플라스틱 뚜껑",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="나무젓가락",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="고장난 스마트폰",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="기저귀",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="종이 박스",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="고장난 시계",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="플라스틱 의자",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="부러진 유리잔",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="헌 신발",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
    TrashItem(
        name="고장난 컴퓨터",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.BIG_APPLIANCE
    ),
    TrashItem(
        name="마른 나뭇잎",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="플라스틱 빨대",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="철사",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="깨진 꽃병",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="과자 봉지",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="고장난 전기주전자",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="종이 서류",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="철제 스푼",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="헌 양말",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
    TrashItem(
        name="깨진 안경",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="못 쓰는 리모컨",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="부러진 의자",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="플라스틱 장난감",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="고장난 선풍기",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="종이 쇼핑백",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="깨진 창문",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="고장난 오디오",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="플라스틱 숟가락",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PLASTIC
    ),
    TrashItem(
        name="고장난 마우스",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="고장난 키보드",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.SMALL_APPLIANCE
    ),
    TrashItem(
        name="헌 가방",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.CLOTH
    ),
]
