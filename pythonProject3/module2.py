import os
import logging
import google.generativeai as genai
import markdown
from datetime import datetime
from dotenv import load_dotenv
import time

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('news_generator.log'),
        logging.StreamHandler()
    ]
)

# 加载环境变量
load_dotenv()

# 检查API密钥
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("未找到Gemini API密钥，请检查.env文件配置")

# 初始化Gemini
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    logging.info("Gemini API连接成功")
except Exception as e:
    logging.error(f"Gemini API初始化失败: {str(e)}")
    raise

def validate_content(content):
    """验证生成的内容是否符合要求"""
    if not content:
        logging.error("生成的内容为空")
        return False
    
    # 检查是否包含至少3条新闻
    news_items = [item for item in content.split('\n\n') if item.strip()]
    if len(news_items) < 3:
        logging.error(f"新闻条数不足3条，当前只有{len(news_items)}条")
        return False
    
    # 检查每条新闻是否以emoji开头
    valid_emojis = ['🤖', '📱', '💡', '🔬', '🎯', '🚀', '💻', '🔋', '🎮', '📊']
    for item in news_items:
        if not any(item.strip().startswith(emoji) for emoji in valid_emojis):
            logging.error(f"新闻未以正确的emoji开头: {item[:50]}...")
            return False
    
    return True

def generate_news(max_retries=3, retry_delay=5):
    """生成AI新闻内容"""
    for attempt in range(max_retries):
        try:
            prompt = """
            你是一名AI科技记者，请生成今日最重要的3条AI领域进展。

            严格按照以下格式生成每条新闻：
            1. 每条新闻必须以下列emoji之一开头（必须是第一个字符）：
               🤖📱💡🔬🎯🚀💻🔋🎮📊
            2. 每条新闻不超过100字
            3. 包含技术名称、公司/机构、影响分析
            4. 使用Markdown格式
            5. 每条新闻之间用一个空行分隔

            示例格式：
            🤖 [技术名称] - [公司/机构] 推出突破性进展。[简短描述]。这将[影响分析]。

            🚀 [技术名称] 由[公司/机构]开发。[简短描述]。预计将[影响分析]。

            💡 [公司/机构]发布[技术名称]。[简短描述]。专家认为这将[影响分析]。

            当前日期：{date}
            """.format(date=datetime.now().strftime("%Y-%m-%d"))

            logging.info("正在生成新闻内容...")
            response = model.generate_content(prompt)
            
            if response.text:
                content = response.text
                if validate_content(content):
                    return content
                else:
                    logging.warning("生成的内容未通过验证，重试中...")
                    time.sleep(retry_delay)
                    continue
            else:
                logging.error("生成的内容为空")
                continue
                
        except Exception as e:
            logging.error(f"生成新闻失败 (尝试 {attempt + 1}/{max_retries}): {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                return None

def save_to_html(content):
    """保存内容到HTML文件"""
    try:
        # 转换Markdown到HTML
        html_content = markdown.markdown(content)
        
        # 生成当前日期的文件名
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"news_{date_str}.html"
        
        # 创建archives目录
        try:
            os.makedirs("archives", exist_ok=True)
            logging.info("成功创建archives目录")
        except Exception as e:
            logging.error(f"创建archives目录失败: {str(e)}")
            raise
        
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>AI每日简报 - {date_str}</title>
            <meta charset="utf-8">
            <style>
                body {{ 
                    max-width: 800px; 
                    margin: auto; 
                    padding: 20px;
                    font-family: Arial, sans-serif;
                }}
                .news-item {{ 
                    margin-bottom: 30px; 
                    border-left: 3px solid #2196F3; 
                    padding-left: 15px; 
                }}
                .date {{ 
                    color: #666; 
                    font-size: 0.9em; 
                }}
            </style>
        </head>
        <body>
            <h1>🤖 AI每日简报</h1>
            <div class="date">{date_str}</div>
            <div class="content">
                {html_content}
            </div>
        </body>
        </html>
        """
        
        # 保存文件
        archive_path = os.path.join("archives", filename)
        try:
            with open(archive_path, "w", encoding="utf-8") as f:
                f.write(html_template)
            logging.info(f"成功保存到archives: {filename}")
            
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(html_template)
            logging.info("成功更新index.html")
            
        except Exception as e:
            logging.error(f"写入文件失败: {str(e)}")
            raise
            
    except Exception as e:
        logging.error(f"保存HTML失败: {str(e)}")
        raise

def main():
    """主函数"""
    try:
        logging.info("新闻生成器启动")
        news = generate_news()
        if news:
            save_to_html(news)
            print("简报已生成！打开index.html查看结果")
        else:
            print("生成简报失败，请检查日志")
    except Exception as e:
        logging.error(f"程序运行出错: {str(e)}")
        print("程序运行出错，请检查日志文件了解详细信息")

if __name__ == "__main__":
    main()