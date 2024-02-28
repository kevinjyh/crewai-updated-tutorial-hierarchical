from datetime import datetime
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top AI news stories from the past 24 hours. The current time is {datetime.now()}.',
            agent=agent,
            async_execution=True,
            expected_output="""以繁體中文將過去24小時內的頂尖AI新聞故事標題、網址，以及每個故事的簡短摘要列表。 
                輸出範例: 
                [
                    {  'title': 'AI takes spotlight in Super Bowl commercials', 
                    'url': 'https://example.com/story1', 
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze each news story and ensure there are at least 5 well-formatted articles',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""以繁體中文呈現並針對每個新聞故事的 Markdown 格式分析，包括詳細的摘要、要點，以及 "為什麼這很重要" 的部分。
                應該至少有5篇文章，每篇都遵循適當的格式。
                輸出範例: 
                '## AI takes spotlight in Super Bowl commercials\n\n
                **The Rundown:
                ** AI made a splash in this year\'s Super Bowl commercials...\n\n
                **The details:**\n\n
                - Microsoft\'s Copilot spot showcased its AI assistant...\n\n
                **Why it matters:** While AI-related ads have been rampant over the last year, its Super Bowl presence is a big mainstream moment.\n\n'
            """
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter',
            agent=agent,
            context=context,
            expected_output="""一份完整的繁體中文新聞通訊，以 Markdown 格式呈現，風格和版面設計保持一致。
                輸出範例: 
                '# Top stories in AI today:\\n\\n
                - AI takes spotlight in Super Bowl commercials\\n
                - Altman seeks TRILLIONS for global AI chip initiative\\n\\n

                ## AI takes spotlight in Super Bowl commercials\\n\\n
                **The Rundown:** AI made a splash in this year\'s Super Bowl commercials...\\n\\n
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
                ## Altman seeks TRILLIONS for global AI chip initiative\\n\\n
                **The Rundown:** OpenAI CEO Sam Altman is reportedly angling to raise TRILLIONS of dollars...\\n\\n'
                **The details:**...\\n\\n
                **Why it matters::**...\\n\\n
            """,
            callback=callback_function
        )
