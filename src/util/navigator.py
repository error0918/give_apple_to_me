import tkinter
from dataclasses import dataclass
from enum import Enum
from typing import Union
from ui import select1, widget
from ui.last_screen import end_screen, ask_screen, electric_screen
from util import hangul, controller, theme


# 대분류
class Division(Enum):
    FOOD = "음식물"
    ELECTRIC = "전자제품"
    LIVING = "생활 쓰레기"
    ETC = "기타"


# 소분류
class SubDivision(Enum):
    # 소분류 = (소분류 이름, 소속 대분류)
    VEGETABLES = ("채소", Division.FOOD)
    FRUITS = ("과일", Division.FOOD)
    SEAFOOD = ("해산물", Division.FOOD)
    ETC_DOS = ("기타" ,  Division.FOOD)


# 연결 페이지
class GoPage(Enum):
    DEFAULT = lambda root, name: nav_default(root=root, name=name)  # 일반 쓰레기
    FOOD = lambda root, name: nav_food(root=root, name=name)  # 음식물 쓰레기
    NUCLEARSEED = lambda root, name: nav_default(root=root, name=name)  # 핵과류 씨 - 일반 쓰레기
    ROOT = lambda root, name: nav_root(root=root, name=name)  # 뿌리채소 - 일반 쓰레기
    PINE = lambda root, name: nav_pine(root=root, name=name)  # 파인애플 껍질/줄기 - 일반 쓰레기
    BONE = lambda root, name: nav_bone(root=root, name=name)  # 뼈류 - 일반 쓰레기
    PAPER = lambda root, name: nav_paper(root=root, name=name)  # 종이류
    GLASS = lambda root, name: nav_glass(root=root, name=name)  # 유리류
    METAL = lambda root, name: nav_metal(root=root, name=name)  # 금속류
    BATTERY = lambda root, name: nav_battery(root=root, name=name)  # 전지류
    LIGHT = lambda root, name: nav_light(root=root, name=name)  # 형광등
    APPLIANCE = lambda root, name: nav_appliance(root=root, name=name)  # 폐가전
    PHONE = lambda root, name: nav_phone(root=root, name=name) # 스마트폰
    GOMPANGI = lambda root, name: nav_gompangi(root=root, name=name)  # 곰팡이가 피었나요?



# 일반 쓰레기
def nav_default(root, name: str):
    def text_edit(text: tkinter.Text):
        text.tag_configure(
            tagName="highlight",
            foreground=theme.color_point,
            font=theme.font(size=35, bold=True)
        )
        text.insert("1.0", " 일반 쓰레기는 환경을 지키기 위한 마지막 책임입니다.\n\n")
        text.insert(tkinter.END, " 재활용이 불가능한 쓰레기만 담아 일반쓰레기 봉투에 넣고, 쓰레기 배출일에 맞춰 배출해 주세요.", "highlight")
        text.insert(tkinter.END, " 작은 습관이 모여 큰 변화를 만듭니다.")
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="일반 쓰레기",
            content=None,
            text_edit=text_edit
        )
    )

# 음식물 쓰레기
def nav_food(root, name: str):
    def text_edit(text: tkinter.Text):
        text.tag_configure(
            tagName="highlight",
            foreground=theme.color_point,
            font=theme.font(size=35, bold=True)
        )
        text.insert("1.0", " 음식물 쓰레기는 자연의 순환을 위한 소중한 자원입니다.\n\n")
        text.insert(tkinter.END, " 물기를 최대한 제거하고, 이물질을 골라낸 후 음식물 쓰레기 전용 봉투에 담아 지정된 장소에 배출해 주세요.", "highlight")
        text.insert(tkinter.END, "올바른 분리배출이 지구를 건강하게 만듭니다.")
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="음식물 쓰레기",
            content=None,
            text_edit=text_edit
        )
    )

# 핵과류 씨
def nav_nuclearseed(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="핵과류 씨",
            content=" 핵과류를 버릴 때에는 과육과 씨를 분리하여 배출해야 합니다. 과육은 음식물 쓰레기로 분류되어 음식물 쓰레기통에 버려야 하며, 씨는 일반 쓰레기로 분류되어 종량제 봉투에 담아 배출해야 합니다. "
        )
    )

# 뿌리채소
def nav_root(root, name: str):
    widget.toast(root, text="채소의 뿌리와 껍질, 대 등은 일반 쓰레기로 분류됩니다. 해당 부분에는 소화능력을 떨어트리는 성분이 있기 때문입니다.")
    nav_default(root, name)

# 파인애플
def nav_pine(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="파인애플",
            content="파인애플의 과육은 음식물 쓰레기로 분류되지만, 다른 과일들과 달리 파인애플의 껍질과 줄기는 음식물 쓰레기로 분류되지 않습니다. 일반 쓰레기로 취급하여 종량제 봉투에 담아 배출해야 합니다."
        )
    )

# 뼈
def nav_bone(root, name: str):
    widget.toast(root, text="생선 및 육류의 뼈는 일반쓰레기로 분류됩니다. 뼈는 동물의 사료로 재생산할 때 적합하지 않은 재료이기 때문입니다.")
    nav_default(root, name)

# 종이류
def nav_paper(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="종이류",
            content="기름 등 오염 물질이 묻어 있거나 인쇄물 혹은 코팅 처리된 종이는 모두 종량제 봉투에 담아 일반쓰레기로 배출합니다. 박스를 포함한 골판지류의 경우 테이프와 송장 스티커 등의 이물질을 제거한 후 납작하게 접어서 배출합니다. 신문, 책자 등은 스프링을 포함한 종이 외의 다른 부속품을 제거하고 배출하는 것이 바람직합니다."
        )
    )

# 유리류
def nav_glass(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="유리류",
            content="깨지지 않은 유리병의 경우 물로 씻어 이물질을 제거하고 라벨을 떼어낸 후 배출합니다. 깨진 유리병, 판유리, 조명기구용 유리류는 신문지에 감싸 종량제 봉투에 담아 일반 쓰레기로 배출합니다."
        )
    )

# 금속류
def nav_metal(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="금속류",
            content="캔류의 경우 내부를 깨끗하게 헹구고, 부착된 라벨은 제거하여 배출합니다. 못, 철사, 옷걸이, 낡은 프라이팬, 냄비 등의 철제류의 경우 고철은 따로 분류하여 폐기하고, 크기가 크고 무거운 경우에는 대형 폐기물 스티커를 부착 후 지정 장소에 배출합니다. 이때 지역별 규정을 참고 바랍니다. 구리 배관이나 전선 등의 경우 전문 재활용 업체에 문의 후 배출합니다. 포일, 도시락용 알루미늄 용기, 일회용 접시 등의 경우 묻어있는 기름과 음식물을 세척하여 배출하고, 심하게 오염되거나 너무 얇아 재활용이 불가능한 경우에는 일반 쓰레기로 폐기합니다."
        )
    )

# 전지류
def nav_battery(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="전지류",
            content="건전지, 보조배터리, 리튬이온 배터리 등의 소형전지류는 제품에서 분리하여 폐전지류 전용 수거함에 배출해야 합니다. 유해물질이 유출될 수 있으므로 전지류에 붙어있는 배선 등은 임의로 제거하지 않는 것이 좋습니다."
        )
    )

# 형광등
def nav_light(root, name: str):
    controller.change_screen(
        end_screen.EndScreen(
            root,
            title="형광등",
            content="직선형의 긴, 흔히 볼 수 있는 형광등은 깨지지 않게 주의하여 가까운 폐형광등 수거함에 배출합니다. 폐형광등 수거함은 아파트 단지 내나 주민센터, 대형마트 등에 설치되어 있습니다. 그 외 자외선 램프나 살균 램프, 식물 재배용 형광등은 전문 처리 업체를 통해 배출하거나 지역 폐기물 처리 센터에 문의하여 처리합니다. 형광등이 이미 깨졌다면 재활용이 불가능하므로 신문지 등으로 조각을 감싸 봉투에 1차 밀폐 후 종량제 봉투에 담아 배출합니다. 형광등 내부에 포함된 수은은 유해물질이므로 직접 닿지 않도록 주의하십시오."
        )
    )


# 폐가전
def nav_appliance(root, name: str):
    controller.change_screen(
        electric_screen.ElectricScreen(
            root,
            depot_type=electric_screen.DepotType.APPLIANCE
        )
    )

# 폐휴대폰
def nav_phone(root, name: str):
    controller.change_screen(
        electric_screen.ElectricScreen(
            root,
            depot_type=electric_screen.DepotType.PHONE
        )
    )

# 곰팡이가 피었나요?
def nav_gompangi(root, name: str):
    def command_no():
        nav_food(root, name)
    def command_yes():
        widget.toast(root, text="상하거나 곰팡이가 핀 쓰레기는 일반 쓰레기로 분류됩니다.")
        nav_default(root, name=name)
    controller.change_screen(
        ask_screen.AskScreen(
            root,
            title="음식물 확인",
            content="잠깐! 곰팡이가 피었나요?",
            command_no=command_no,
            command_yes=command_yes,
            command_back=lambda : controller.change_screen(select1.Select1(root))
        )
    )


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
        divisions=[SubDivision.VEGETABLES],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="달걀 껍질",
        divisions=[SubDivision.ETC_DOS],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="고구마",
        divisions=[SubDivision.VEGETABLES],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="당근",
        divisions=[SubDivision.VEGETABLES],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="배추",
        divisions=[SubDivision.VEGETABLES],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="상추",
        divisions=[SubDivision.VEGETABLES],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="시금치",
        divisions=[SubDivision.VEGETABLES],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="자두",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.NUCLEARSEED
    ),
    TrashItem(
        name="살구",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.NUCLEARSEED
    ),
    TrashItem(
        name="체리",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.NUCLEARSEED
    ),
    TrashItem(
        name="복숭아",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.NUCLEARSEED
    ),
    TrashItem(
        name="바나나",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="파인애플",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.PINE
    ),
    TrashItem(
        name="사과",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="귤",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="포도",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="딸기",
        divisions=[SubDivision.FRUITS],
        go_page=GoPage.GOMPANGI
    ),
    TrashItem(
        name="갑각류 껍데기",
        divisions=[SubDivision.SEAFOOD],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="생선 뼈",
        divisions=[SubDivision.SEAFOOD],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="닭 뼈",
        divisions=[SubDivision.ETC_DOS],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="티백",
        divisions=[SubDivision.ETC_DOS],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="원두 찌꺼기",
        divisions=[SubDivision.ETC_DOS],
        go_page=GoPage.DEFAULT
    ),

    TrashItem(
        name="신문지",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="폐식용유",
        divisions=[SubDivision.ETC_DOS],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="금속 병뚜껑",
        divisions=[Division.LIVING],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="전기 면도기",
        divisions=[Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="카드보드(피자 박스 등)",
        divisions=[Division.LIVING],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="코팅 처리된 종이",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="인쇄지",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="못",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="옷걸이",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="철제 냄비",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="일회용 알루미늄 접시",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="쿠킹 포일",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="통조림 캔",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="구리 전선",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="기름 묻은 종이",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="형광등",
        divisions=[Division.LIVING, Division.ELECTRIC],
        go_page=GoPage.LIGHT
    ),
    TrashItem(
        name="건전지",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.BATTERY
    ),
    TrashItem(
        name="전자레인지",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="냉장고",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.APPLIANCE
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
        name="접시",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="헤어드라이어",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="종이컵",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="충전기",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="나무젓가락",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.DEFAULT
    ),
    TrashItem(
        name="스마트폰",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.PHONE
    ),
    TrashItem(
        name="종이박스",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.PAPER
    ),
    TrashItem(
        name="전자 시계",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="부러진 유리잔",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.GLASS
    ),
    TrashItem(
        name="컴퓨터",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="철사",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="전기포트",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="철제 스푼",
        divisions=[Division.LIVING, Division.ETC],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="리모컨",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="선풍기",
        divisions=[Division.ELECTRIC, Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="마우스",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="키보드",
        divisions=[Division.ELECTRIC, Division.ETC],
        go_page=GoPage.APPLIANCE
    ),
    TrashItem(
        name="금속 병뚜껑",
        divisions=[Division.LIVING],
        go_page=GoPage.METAL
    ),
    TrashItem(
        name="커피 머신",
        divisions=[Division.LIVING],
        go_page=GoPage.APPLIANCE
    ),
]