from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'從過去10年中獲取頂尖無人機航測推算河川水底地形數據的新聞故事。目前的時間是 {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""以繁體中文將過去10年內的頂尖無人機航測推算河川水底地形數據的新聞故事標題、網址，
                以及每個故事的簡短摘要列表。 
                輸出範例: 
                [
                    {  'title': '無人機正在河川測量中大放異彩', 
                    'url': 'https://example.com/story1', 
                    'summary': '無人機航測克服植被及河水以取得地形數值的技術是大熱門...'
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='分析每個新聞故事並確保至少有5篇格式良好的文章',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""以繁體中文呈現並針對每個新聞故事的 Markdown 格式分析，
                包括詳細的摘要、要點，以及 "為什麼這很重要" 的部分。
                應該至少有5篇文章，每篇都遵循適當的格式。
                輸出範例: 
                '## 無人機航測河川水底地形推算的技術正在大放異彩\n\n
                **摘要:
                ** 無人機航測河川水底地形推算的新技術不斷推陳出新...\n\n
                **詳細內容:**\n\n
                - 大彊UAV展示了航測無限可能...\n\n
                **為什麼重要:** 無人機雖然已經很普遍，但是如何克服水波起伏干擾河床地形測量仍是重要課題...\n\n'
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter',
            agent=agent,
            context=context,
            expected_output="""一份完整的繁體中文新聞通訊，以 Markdown 格式呈現，
                風格和版面設計保持一致。
                輸出範例: 
                '# 無人機航測的最夯新聞:\\n\\n
                - 無人機航測在水利工程領域搶眼表現\\n
                - 大彊尋求資金推動無人機航測辨識地形技術的提升\\n\\n

                ## 無人機在各大廣告中搶鏡\\n\\n
                **摘要:** 無人機在今年的超級碗廣告中大放異彩...\\n\\n
                **詳細內容:**...\\n\\n
                **為何重要::**...\\n\\n
                ## 大彊尋求資金推動無人機航測辨識地形技術的提升\\n\\n
                **摘要:** 無人機大廠擴大發展資金...\\n\\n'
                **詳細內容:**...\\n\\n
                **為何重要::**...\\n\\n
            """,
            callback=callback_function
        )
