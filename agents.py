from crewai import Agent
from tools.search_tools import SearchTools
# from langchain_google_genai import ChatGoogleGenerativeAI
import os

class AINewsLetterAgents():
    # def __init__(self):
    #     self.model = ChatGoogleGenerativeAI(
    #             model="gemini-pro", 
    #             verbose=True, 
    #             temperature=0.1, 
    #             google_api_key=os.environ.get("GEMINI_API_KEY")
    #         )

    def editor_agent(self):
        return Agent(
            role='Editor',
            goal='觀查無人機航測河水底床地形推算的最新消息',
            # goal='Oversee the creation of the AI Newsletter'
            backstory="""憑藉對細節的敏銳觀察力和對敘事的熱情，你確保新聞通訊不僅提供資訊，還能吸引和激勵讀者。 """,
            # backstory="""With a keen eye for detail and a passion for storytelling, you ensure that the newsletter
            # not only informs but also engages and inspires the readers. """,
            allow_delegation=True,
            verbose=True,
            # llm=self.model,
            max_iter=15
        )

    def news_fetcher_agent(self):
        return Agent(
            role='NewsFetcher',
            goal='取得近五年最熱門的無人機航測河水底床地形推算新聞故事',
            # goal='Fetch the top AI news stories for the day',
            backstory="""作為一名數位偵探，你搜尋網路上最新且最具影響力的
            無人機航測河水底床地形推算發展，確保我們的讀者始終掌握最新資訊。""",
            # backstory="""As a digital sleuth, you scour the internet for the latest and most impactful developments
            # in the world of AI, ensuring that our readers are always in the know.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            # llm=self.model,
            allow_delegation=True,
        )

    def news_analyzer_agent(self):
        return Agent(
            role='NewsAnalyzer',
            goal='分析每個新聞故事並產生詳細的 Markdown 摘要',
            # goal='Analyze each news story and generate a detailed markdown summary',
            backstory="""憑藉敏銳的觀察力和簡化複雜資訊的能力，你提供了對
            無人機航測河水底床地形推算新聞故事的深入分析，使其對我們的觀眾
            來說既易於理解又引人入勝。""",
            # backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            # analyses of AI news stories, making them accessible and engaging for our audience.""",
            tools=[SearchTools.search_internet],
            verbose=True,
            # llm=self.model,
            allow_delegation=True,
        )

    def newsletter_compiler_agent(self):
        return Agent(
            role='NewsletterCompiler',
            goal='將分析過的新聞故事編譯成最終的新聞通訊格式',
            # goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""作為新聞通訊的最終編輯，你精心安排和格式化內容，
            確保一個連貫且視覺上吸引人的呈現方式，吸引我們的讀者。
            請確保遵循新聞通訊的格式指南，並在整個過程中保持一致性。""",
            # backstory="""As the final architect of the newsletter, you meticulously arrange and format the content,
            # ensuring a coherent and visually appealing presentation that captivates our readers. Make sure to follow
            # newsletter format guidelines and maintain consistency throughout.""",
            verbose=True,
            # llm=self.model,
        )
